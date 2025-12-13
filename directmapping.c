#include <stdio.h>

#define CACHE_LINES 8     // cache has 8 lines
#define BLOCK_SIZE 4      // each block has 4 words
#define MAX_ADDRESS 65535 // 16-bit address max

int cache[CACHE_LINES];
int tag[CACHE_LINES];
int valid[CACHE_LINES];

int main() {
    unsigned short address;
    int blockNumber, index, tagValue, offset;
    int hits = 0, misses = 0;
    int choice;

    // Initialize cache
    for (int i = 0; i < CACHE_LINES; i++) {
        valid[i] = 0;
    }

    while (1) {
        printf("\n--- DIRECT MAPPED CACHE SIMULATION ---");
        printf("\n1. Enter memory address");
        printf("\n2. Exit");
        printf("\nEnter choice: ");
        scanf("%d", &choice);

        if (choice == 2)
            break;

        if (choice != 1) {
            printf("Invalid choice!\n");
            continue;
        }

        printf("Enter a 16-bit memory address (0 to 65535): ");
        scanf("%hu", &address);

        if (address > MAX_ADDRESS) {
            printf("Invalid address!\n");
            continue;
        }

        blockNumber = address / BLOCK_SIZE;
        index = blockNumber % CACHE_LINES;
        tagValue = blockNumber / CACHE_LINES;
        offset = address % BLOCK_SIZE;

        printf("\nAddress Details:");
        printf("\n----------------");
        printf("\nAddress        : %hu", address);
        printf("\nBlock Number   : %d", blockNumber);
        printf("\nCache Line     : %d", index);
        printf("\nTag            : %d", tagValue);
        printf("\nOffset         : %d\n", offset);

        if (valid[index] && tag[index] == tagValue) {
            printf("CACHE HIT at line %d\n", index);
            hits++;
        } else {
            printf("CACHE MISS! Loading block %d into line %d\n", blockNumber, index);
            cache[index] = blockNumber;
            tag[index] = tagValue;
            valid[index] = 1;
            misses++;
        }

        printf("\nCurrent Cache State:\n");
        printf("--------------------\n");
        for (int i = 0; i < CACHE_LINES; i++) {
            if (valid[i])
                printf("Line %d -> Block %d (Tag %d)\n", i, cache[i], tag[i]);
            else
                printf("Line %d -> EMPTY\n", i);
        }

        printf("\nTotal Hits   : %d", hits);
        printf("\nTotal Misses : %d\n", misses);
    }

    printf("\nSimulation Ended.\n");
    return 0;
}
