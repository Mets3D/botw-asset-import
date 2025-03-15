import time
from collections import defaultdict

class Timer:
    """A simple class to help measure performance.
    
    Example use:
    ```
    for img in images:
        with Timer(category="Pixel caching"):
            cache_img(img)

    Timer.summarize(reset=True)
    ```

    Output:
    `Pixel caching 3.61283791237`

    So instead of timing a function once, it times the total amount that your program 
    spent in functions of the same category, regardless of how many times they ran.
    """
    instances = []

    def __init__(self, category="N/A", name="Elapsed time"):
        self.category = category
        self.name = name
        self.start = 0
        self.elapsed = 0
        type(self).instances.append(self)

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        # print(f"{self.name}: {self.elapsed:.2f} seconds")

    @classmethod
    def summarize(cls, reset=True):
        categories = defaultdict(int)
        for inst in cls.instances:
            categories[inst.category] += inst.elapsed

        for name, duration in categories.items():
            print(name, duration)

        if reset:
            cls.instances = []