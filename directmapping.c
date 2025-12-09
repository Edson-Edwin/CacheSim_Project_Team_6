#include <stdio.h>

#define CACHE_LINES 8     // cache has 8 lines
#define BLOCK_SIZE 4      // each block has 4 words
#define MEMORY_BLOCKS 32  // total memory blocks

int cache[CACHE_LINES];   // stores block numbers
int tag[CACHE_LINES];     // stores tag values
int valid[CACHE_LINES];   // valid bits

int main() {
    int address, blockNumber, index, tagValue, offset;

    // initialize cache
    for (int i = 0; i < CACHE_LINES; i++) {
        valid[i] = 0;     // cache empty
    }

    while (1) {
        printf("\nEnter a 16-bit memory address (0 to 65535): ");
        scanf("%d", &address);

        // calculate block number
        blockNumber = address / BLOCK_SIZE;

        // direct mapping
        index = blockNumber % CACHE_LINES;
        tagValue = blockNumber / CACHE_LINES;
        offset = address % BLOCK_SIZE;

        printf("\nAddress: %d", address);
        printf("\nBlock Number: %d", blockNumber);
        printf("\nIndex (Cache Line): %d", index);
        printf("\nTag: %d", tagValue);
        printf("\nOffset (Word in block): %d\n", offset);

        // check if block is already in cache
        if (valid[index] && tag[index] == tagValue) {
            printf("CACHE HIT at line %d!\n", index);
        } else {
            printf("CACHE MISS! Loading block %d into line %d...\n", blockNumber, index);

            // load into cache
            cache[index] = blockNumber;
            tag[index] = tagValue;
            valid[index] = 1;
        }

        printf("\nCurrent Cache State:\n");
        for (int i = 0; i < CACHE_LINES; i++) {
            if (valid[i])
                printf("Line %d -> Block %d (Tag %d)\n", i, cache[i], tag[i]);
            else
                printf("Line %d -> EMPTY\n", i);
        }
    }

    return 0;
}
