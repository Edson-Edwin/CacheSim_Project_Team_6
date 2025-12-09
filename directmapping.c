#include <stdio.h>

#define CACHE_LINES 8     // cache has 8 lines
#define BLOCK_SIZE 4      // each block has 4 words

int cache[CACHE_LINES];
int tag[CACHE_LINES];
int valid[CACHE_LINES];

int main() {
    int address, blockNumber, index, tagValue, offset;

    for (int i = 0; i < CACHE_LINES; i++) {
        valid[i] = 0;
    }

    while (1) {
        printf("\nEnter a 16-bit memory address (0 to 65535): ");
        scanf("%d", &address);

        blockNumber = address / BLOCK_SIZE;
        index = blockNumber % CACHE_LINES;
        tagValue = blockNumber / CACHE_LINES;
        offset = address % BLOCK_SIZE;

        printf("\nAddress: %d", address);
        printf("\nBlock Number: %d", blockNumber);
        printf("\nIndex (Cache Line): %d", index);
        printf("\nTag: %d", tagValue);
        printf("\nOffset (Word in block): %d\n", offset);

        if (valid[index] && tag[index] == tagValue) {
            printf("CACHE HIT at line %d!\n", index);
        } else {
            printf("CACHE MISS! Loading block %d into line %d...\n", blockNumber, index);
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
