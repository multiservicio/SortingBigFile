from source.external_sorting import ExternalSorting

# Main input of the program
if __name__ == '__main__':
    # We will use 1 MB of memory to sort in memory
    memory_to_use = 1 * 1024 * 1024

    # File to sort
    file = 'unsorted.txt'

    external_sorting = ExternalSorting(
        chunk_size=memory_to_use,
        file_name=file
    )

    print("Memory to use: ", memory_to_use)
    external_sorting.sort()
