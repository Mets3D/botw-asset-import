import bpy, math
from .timer import Timer

class PixelImage:
    """Store some pixels either from raw data or a Blender image, 
    then make available some info about the pixel data, calculated only
    only when first requested, and then cached."""

    cache = {}

    @classmethod
    def from_blender_image(cls, bpy_img: bpy.types.Image, ignore_cache=False):
        if bpy_img.name in cls.cache and not ignore_cache:
            return cls.cache[bpy_img.name]

        instance = cls()
        instance.width = bpy_img.size[0]
        instance.height = bpy_img.size[1]
        instance.bpy_img = bpy_img
        cls.cache[bpy_img.name] = instance

        return instance

    @classmethod
    def from_pixels(cls, width, height, pixels):
        instance = cls()
        instance.width = width
        instance.height = height
        instance.pixels = pixels
        return instance

    def __init__(self):
        self.bpy_img = None
        self.width = 0
        self.height = 0
        self._pixels = []
        self.pixels_rgba = []

    def crop_to_square_content(self):
        """
        Crops the image to a square by removing empty rows/columns while 
        ensuring the final image remains square. Useful for asset thumbnails.
        """
        if not self.pixels_rgba:
            return  # No pixels to process
        
        w, h = self.width, self.height

        # Convert 1D pixel list into a 2D list (rows of pixels)
        pixel_rows = [self.pixels_rgba[i * w:(i + 1) * w] for i in range(h)]

        # Find the bounding box of non-transparent pixels
        min_x, max_x = w, 0
        min_y, max_y = h, 0

        for y, row in enumerate(pixel_rows):
            for x, pixel in enumerate(row):
                if pixel[3] > 0:  # If alpha > 0 (not transparent)
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)

        # If the image is fully transparent, return an empty square
        if max_x < min_x or max_y < min_y:
            self.width = self.height = 0
            self.pixels_rgba = []
            return

        # Calculate the bounding box width and height
        content_width = max_x - min_x + 1
        content_height = max_y - min_y + 1

        # Determine the square size
        square_size = max(content_width, content_height)

        # Expand the bounding box to make it square
        extra_w = (square_size - content_width) // 2
        extra_h = (square_size - content_height) // 2

        start_x = max(0, min_x - extra_w)
        end_x = min(w, start_x + square_size)

        start_y = max(0, min_y - extra_h)
        end_y = min(h, start_y + square_size)

        # Extract the square pixels
        cropped_grid = [row[start_x:end_x] for row in pixel_rows[start_y:end_y]]

        # Update image data
        self.width = square_size
        self.height = square_size
        pixels_rgba = [pixel for row in cropped_grid for pixel in row]
        if len(pixels_rgba) < square_size*square_size:
            # Pad empty pixels if we're missing any to fill out the full square with data.
            pixels_rgba += [(0, 0, 0, 0)] * (square_size*square_size - len(pixels_rgba))
        self.pixels_rgba = pixels_rgba

    def downscale_to_fit(self, max_size=256):
        """
        Downscale the image so that its width and height do not exceed max_size.
        The aspect ratio is preserved.
        """
        if self.width <= max_size and self.height <= max_size:
            return  # No need to downscale

        # Compute scale factor (preserving aspect ratio)
        scale_factor = min(max_size / self.width, max_size / self.height)
        new_width = max(1, math.floor(self.width * scale_factor))
        new_height = max(1, math.floor(self.height * scale_factor))

        # Downscale using nearest-neighbor sampling
        downsampled_pixels = []
        for y in range(new_height):
            orig_y = int(y / scale_factor)
            for x in range(new_width):
                orig_x = int(x / scale_factor)
                downsampled_pixels.append(self.pixels_rgba[orig_y * self.width + orig_x])

        # Update image properties
        self.width = new_width
        self.height = new_height
        self.pixels_rgba = downsampled_pixels

    @property
    def pixels(self):
        return [channel for pixel in self.pixels_rgba for channel in pixel]

    @property
    def pixels_rgba(self):
        if not self._pixels_rgba:
            with Timer("Pixel cache", self.bpy_img.name if self.bpy_img else ""):
                # NOTE: Careful! Accessing bpy_img.pixels is very slow! Do this only when needed!
                if self.bpy_img:
                    pixels = self.bpy_img.pixels[:]
                else:
                    pixels = self._pixels
                self._pixels_rgba = [tuple(pixels[i:i+4]) for i in range(0, len(pixels), 4)]
        return self._pixels_rgba

    @pixels_rgba.setter
    def pixels_rgba(self, value):
        # If we change the pixels, reset all the cached values.
        self._is_single_color = None
        self._has_green = None
        self._has_blue = None
        self._has_alpha = None
        self._all_channels_match = None

        self._pixels_rgba = value

    @property
    def is_single_color(self):
        if self._is_single_color == None:
            self._is_single_color = all([p==self.pixels_rgba[0] for p in self.pixels_rgba])
        return self._is_single_color

    @property
    def has_red(self):
        if self._has_red == None:
            self._has_red = any([p[0] for p in self.pixels_rgba])
        return self._has_red

    @property
    def has_green(self):
        if self._has_green == None:
            self._has_green = any([p[1] for p in self.pixels_rgba])
        return self._has_green

    @property
    def has_blue(self):
        if self._has_blue == None:
            self._has_blue = any([p[2] for p in self.pixels_rgba])
        return self._has_blue

    @property
    def has_alpha(self):
        if self._has_alpha == None:
            self._has_alpha = any([p[3] != 1 for p in self.pixels_rgba])
        return self._has_alpha

    @property
    def all_channels_match(self):
        if self._all_channels_match == None:
            self._all_channels_match = all([p[0]==p[1]==p[2]==p[3] for p in self.pixels_rgba])
        return self._all_channels_match