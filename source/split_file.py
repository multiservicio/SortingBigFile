from in_memory_sort import InMemorySort


# Split the given file into a smaller-sorted one.
# This will load into memory the file (so it must fit into memory)
# and perform in memory sort.
class SplitFile:

    # Class variable that defines the naming for this partial files
    PARTIAL_FILE_NAME = 'split_{0}.partial'

    # When creating an instance of this object we will pass the file name
    def __init__(self, file_name):
        self.file_name = file_name

    # Main functionality of this class. To split given file into smaller sorted ones
    # In order to split and sort we will doing the following
    # Read a bunch of lines (until the given chunk size, typically the amount of memory to use)
    def split(self, chunk_size):
        # Since over this file we do not need any other operation than read
        file = open(self.file_name, 'r')

        # Now we will start reading the chunks of lines
        # Read lines
        # Sort those lines
        # Store the lines in a partial file
        # Do it for all lines
        do_we_continue = True
        partial_file_number = 0
        while do_we_continue:
            block_of_lines = file.readlines(chunk_size)

            # We reached the end of the file
            if not block_of_lines:
                do_we_continue = False

            # Sort the lines in memory using --- sorting algorithm
            sorted_lines = InMemorySort.sort(block_of_lines)
            # block_of_lines.sort()

            # Save into partial file the sorted lines
            self._dump_into_partial_file(sorted_lines, partial_file_number)

            # Increment the partial file number, in this way we will have all the
            # Partial files numbered
            partial_file_number += 1

    # Private method that will dump the chunk of lines into a file
    # The names of such files is defined in the class variable PARTIAL_FILE_NAME
    # Been of the format:
    #   split_0.partial -> Containing the first block of lines
    def _dump_into_partial_file(self, chunk_of_lines, partial_file_identifier):
        # As we know that the variable is string we can substitute the value
        # https://docs.python.org/3.4/library/stdtypes.html#str.format
        file = open(self.PARTIAL_FILE_NAME.format(partial_file_identifier), 'w')
        file.write(chunk_of_lines)
        file.close()
