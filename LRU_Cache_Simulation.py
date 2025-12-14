from collections import deque

class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = []               # Stores cache blocks
        self.access_order = deque()   # Tracks usage order for LRU
        self.hits = 0
        self.misses = 0

    def access_block(self, block, step):
        if block in self.cache:
            self.hits += 1
            hit_miss = "HIT"
            # Update access order
            self.access_order.remove(block)
            self.access_order.append(block)
        else:
            self.misses += 1
            hit_miss = "MISS"
            if len(self.cache) < self.cache_size:
                self.cache.append(block)
            else:
                # Replace least recently used block
                lru_block = self.access_order.popleft()
                self.cache.remove(lru_block)
                self.cache.append(block)
            self.access_order.append(block)
        
        # Print in tabular format
        print(f"{step:<5} {block:<15} {hit_miss:<10} {self.cache}")

    def get_hit_ratio(self):
        total_accesses = self.hits + self.misses
        return self.hits / total_accesses if total_accesses else 0

# -------------------- Main Program --------------------
def main():
    print("\nLRU Cache Memory Simulation\n")
    cache_size = int(input("Enter cache size: "))
    reference_sequence = list(map(int, input("Enter memory reference sequence (space separated): ").split()))

    cache = LRUCache(cache_size)

    print("\nSimulation Start\n")
    print(f"{'Step':<5} {'Accessed Block':<15} {'Hit/Miss':<10} {'Cache Content'}")
    print("-" * 50)

    for i, block in enumerate(reference_sequence, start=1):
        cache.access_block(block, i)

    print("\nSimulation Complete")
    print("-" * 50)
    print(f"{'Total Hits':<20}: {cache.hits}")
    print(f"{'Total Misses':<20}: {cache.misses}")
    print(f"{'Hit Ratio':<20}: {cache.get_hit_ratio():.2f}")
    print("-" * 50)

if __name__ == "__main__":
    main()
