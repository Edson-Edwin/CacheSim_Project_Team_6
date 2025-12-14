# LFU Page Replacement Algorithm with Hit/Miss Count and Hit Ratio

cache = []        # stores pages
frequency = []    # frequency counters
cache_size = int(input("Enter cache size: "))

reference_string = list(map(str, input("Enter access sequence (space separated): ").split()))

page_faults = 0
page_hits = 0

print("\n--- LFU Simulation ---")

for page in reference_string:

    print(f"\nAccessing: {page}")

    # CASE 1: HIT
    if page in cache:
        index = cache.index(page)
        frequency[index] += 1
        page_hits += 1
        print("Status: HIT")

    else:
        # MISS / PAGE FAULT
        page_faults += 1
        print("Status: MISS / FAULT")

        if len(cache) < cache_size:
            cache.append(page)
            frequency.append(1)

        else:
            # Remove page with lowest frequency
            min_freq = min(frequency)
            remove_index = frequency.index(min_freq)

            removed_page = cache[remove_index]
            print(f"Removing (LFU): {removed_page}")

            cache[remove_index] = page
            frequency[remove_index] = 1

    print("Cache   :", cache)
    print("Freq    :", frequency)

# ---- Final Summary ----
total = len(reference_string)
hit_ratio = page_hits / total

print("\n--- SUMMARY ---")
print("Total Hits  :", page_hits)
print("Total Misses:", page_faults)
print("Hit Ratio   :", round(hit_ratio, 4))