from collections import deque

class FullyAssociativeCache:
    def __init__(self, cache_size, policy="FIFO"):
        self.cache_size = cache_size
        self.policy = policy.upper()
        self.cache = deque()
        self.hits = 0
        self.misses = 0

    def access_block(self, block):
        print(f"\nMemory Block Referenced: {block}")

        # Cache HIT
        if block in self.cache:
            self.hits += 1
            print("Status : HIT")

            # LRU update
            if self.policy == "LRU":
                self.cache.remove(block)
                self.cache.append(block)

        # Cache MISS
        else:
            self.misses += 1
            print("Status : MISS")

            # Cache replacement if full
            if len(self.cache) == self.cache_size:
                removed = self.cache.popleft()
                print(f"Evicted Block : {removed}")

            self.cache.append(block)

        print(f"Cache Content : {list(self.cache)}")

    def hit_ratio(self):
        total = self.hits + self.misses
        return self.hits / total if total != 0 else 0

    def display_summary(self):
        print("\n========== CACHE SUMMARY ==========")
        print(f"Cache Size     : {self.cache_size}")
        print(f"Policy Used    : {self.policy}")
        print(f"Total Hits     : {self.hits}")
        print(f"Total Misses   : {self.misses}")
        print(f"Hit Ratio      : {self.hit_ratio():.2f}")
        print("==================================")

# ---------------- MAIN PROGRAM ----------------

def main():
    cache_size = int(input("Enter cache size: "))
    policy = input("Enter replacement policy (FIFO / LRU): ").strip()

    cache = FullyAssociativeCache(cache_size, policy)

    sequence = list(map(int, input("Enter memory block sequence: ").split()))

    print("\n----- Cache Simulation Started -----")

    for block in sequence:
        cache.access_block(block)

    cache.display_summary()

if __name__ == "__main__":
    main()
