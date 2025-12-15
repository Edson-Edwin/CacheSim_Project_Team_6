class FIFOCache:
    def __init__(self, size):
        self.size = size
        self.cache = []
        self.hits = 0
        self.misses = 0

    def refer(self, block):
        # If block is already in cache → HIT
        if block in self.cache:
            self.hits += 1
        
        else: 
            # MISS
            self.misses += 1

            # If cache is full → remove first inserted (FIFO)
            if len(self.cache) == self.size:
                self.cache.pop(0)

            # Insert the new block
            self.cache.append(block)

        # Display cache status
        print(f"Reference: {block}  → Cache: {self.cache}") 

    def results(self):
        print("\n--- FINAL RESULTS ---")
        print("Total Hits   :", self.hits)
        print("Total Misses :", self.misses)
        total = self.hits + self.misses
        print("Hit Ratio    :", round(self.hits / total, 2))
        

cache_size = 3
reference_string = [1, 2, 3, 2, 4, 1, 5, 2]

fifo = FIFOCache(cache_size)

for ref in reference_string:
    fifo.refer(ref)

fifo.results()
