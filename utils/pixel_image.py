import bpy
from .timer import Timer
from statistics import mean

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
        instance._pixels = pixels
        return instance

    def __init__(self):
        self.bpy_img = None
        self.width = 0
        self.height = 0
        self._pixels = []
        self.pixels_rgba = []

    def crop_to_square_content(self) -> bool:
        """
        Crops the image to a square by removing empty rows/columns while 
        ensuring the final image remains square. Useful for asset thumbnails.
        """
        if not self.pixels_rgba:
            return False  # No pixels to process

        # Convert 1D pixel list into a 2D list (rows of pixels)
        pixel_rows = [self.pixels_rgba[h * self.width:(h+1) * self.width] for h in range(self.height)]

        # Find the bounding box of non-transparent pixels
        min_x, max_x = self.width, 0
        min_y, max_y = self.height, 0

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
            return False

        # Calculate the bounding box width and height
        content_width = max_x - min_x
        content_height = max_y - min_y

        # Determine the square size
        square_size = max(content_width, content_height)
        if square_size == self.width:
            return False

        for i in range(max(0, square_size - self.width)):
            for row in pixel_rows:
                row.append((0, 0, 0, 0))
        extra_height = max(0, square_size - self.height)
        for y in range(extra_height):
            pixel_rows.append([(0, 0, 0, 0) for x in range(max(self.width, square_size))])

        # Extract the square pixels
        pixel_rows = [row[min_x:max_x] for row in pixel_rows[min_y:max_y]]

        row_of_nothing = [(0, 0, 0, 0) for x in range(len(pixel_rows[0]))]
        for i in range(square_size-content_height):
            if i % 2 == 0:
                pixel_rows.insert(0, row_of_nothing)
            else:
                pixel_rows.append(row_of_nothing)

        for i in range(square_size-content_width):
            for row in pixel_rows:
                if i % 2 == 0:
                    row.insert(0, (0, 0, 0, 0))
                else:
                    row.append((0, 0, 0, 0))

        # Update image data
        self.width = square_size
        self.height = square_size
        pixels_rgba = [pixel for row in pixel_rows for pixel in row]
        self.pixels_rgba = pixels_rgba
        return True

    def downscale_to_fit(self, max_size=256):
        """
        Downscale the image so that its width and height do not exceed max_size.
        The aspect ratio is preserved.
        """

        if self.width == 0 or self.height == 0:
            return
        if self.width <= max_size and self.height <= max_size:
            return
        scale = min([max_size / self.width, max_size / self.height])

        if scale >= 1:
            return

        new_width = int(self.width * scale)
        new_height = int(self.height * scale)

        # Downscale using nearest-neighbor sampling
        downsampled_pixels = []
        for y in range(new_height):
            orig_y = int(y / scale)
            for x in range(new_width):
                orig_x = int(x / scale)
                downsampled_pixels.append(self.pixels_rgba[orig_y * self.width + orig_x])

        # Update image properties
        self.width, self.height = new_width, new_height
        self.pixels_rgba = downsampled_pixels

    @property
    def pixels(self):
        return [channel for pixel in self.pixels_rgba for channel in pixel]

    @property
    def pixels_rgba(self):
        try: 
            if self.bpy_img:
                self.bpy_img.name
        except ReferenceError:
            # Image has been removed.
            return []
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
        self._average_color = None

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
    def average_color(self):
        if self._average_color == None:
            filtered_colors = [(r, g, b) for r, g, b, a in self.pixels_rgba if a == 1.0]

            # Compute the average RGB
            if filtered_colors:
                self._average_color = tuple(map(mean, zip(*filtered_colors)))
            else:
                self._average_color = (0, 0, 0)  # Default if no valid colors

        return self._average_color

    @property
    def all_channels_match(self):
        if self._all_channels_match == None:
            self._all_channels_match = all([p[0]==p[1]==p[2]==p[3] for p in self.pixels_rgba])
        return self._all_channels_match