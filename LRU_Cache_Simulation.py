from collections import deque

class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = []               # Stores the cache blocks
        self.access_order = deque()   # Tracks usage order (for LRU)
        self.hits = 0
        self.misses = 0

    def access_block(self, block):
        if block in self.cache:
            self.hits += 1
            print(f"Accessing {block}: HIT")
            # Update access order
            self.access_order.remove(block)
            self.access_order.append(block)
        else:
            self.misses += 1
            print(f"Accessing {block}: MISS")
            if len(self.cache) < self.cache_size:
                self.cache.append(block)
            else:
                # Remove least recently used block
                lru_block = self.access_order.popleft()
                print(f"Replacing block {lru_block} with {block}")
                self.cache.remove(lru_block)
                self.cache.append(block)
            self.access_order.append(block)

        print(f"Cache Content: {self.cache}\n")

    def get_hit_ratio(self):
        total_accesses = self.hits + self.misses
        return self.hits / total_accesses if total_accesses else 0

# -------------------- Main Program --------------------
def main():
    print("LRU Cache Memory Simulation\n")
    cache_size = int(input("Enter cache size: "))
    reference_sequence = list(map(int, input("Enter memory reference sequence (space separated): ").split()))

    cache = LRUCache(cache_size)

    print("\nSimulation Start\n")
    for block in reference_sequence:
        cache.access_block(block)

    print("Simulation Complete")
    print(f"Total Hits: {cache.hits}")
    print(f"Total Misses: {cache.misses}")
    print(f"Hit Ratio: {cache.get_hit_ratio():.2f}")

if __name__ == "__main__":
    main()
