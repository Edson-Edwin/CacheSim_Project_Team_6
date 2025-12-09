import random

CACHE_LINES = 4
cache = [{'valid': 0, 'tag': None} for _ in range(CACHE_LINES)]
fifo_queue = []   # tracks replacement order for FIFO

def display_cache():
    print("\nCache State:")
    print("Line\tValid\tTag")
    for i, line in enumerate(cache):
        print(f"{i}\t{line['valid']}\t{line['tag']}")
    print()

def search_cache(tag):
    for i, line in enumerate(cache):
        if line['valid'] == 1 and line['tag'] == tag:
            return i
    return -1

def replace_block(tag):
    # If cache not full, use next free line
    if len(fifo_queue) < CACHE_LINES:
        line = len(fifo_queue)
    else:
        # FIFO replacement
        line = fifo_queue.pop(0)
    fifo_queue.append(line)

    cache[line]['valid'] = 1
    cache[line]['tag'] = tag
    return line

def access_memory(block):
    tag = block  # fully associative → tag = block number

    print(f"Accessing block {block}")

    line = search_cache(tag)

    if line != -1:
        print(f"→ HIT at line {line}")
    else:
        print("→ MISS, loading block...")
        line = replace_block(tag)
        print(f"→ Block loaded into line {line}")

    display_cache()

# Example accesses
access_memory(3)
access_memory(7)
access_memory(3)
access_memory(15)
access_memory(7)
access_memory(1)

