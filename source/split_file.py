from source.in_memory_sort import InMemorySort


# Split the given file into a smaller-sorted one.
# This will load into memory the file (so it must fit into memory)
# and perform in memory sort.
class SplitFile:

    # When creating an instance of this object we will pass the file name
    # File name of the file to split
    # Chunk size (in Bytes) of the amount of bytes to read each time
    # This should be big enough and fit in memory
    # Partial file name for the new created partial sorted files
    def __init__(self, file_name: str, chunk_size: int, partial_file_name: str = '_split_{0}.partial'):
        self.file_name = file_name
        self.chunk_size = chunk_size
        self.partial_file_name = partial_file_name
        self.partial_files_count = 0

    # Main functionality of this class. To split given file into smaller sorted ones
    # In order to split and sort we will doing the following
    def split(self):
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
            # Chunk size is the size to read from the file 'at once'
            # this is size hint
            # More info -> http://stackoverflow.com/questions/14541010/pythons-function-readlinesn-behavior
            block_of_lines = file.readlines(self.chunk_size)

            # If we did not reach the end of the file yet
            if block_of_lines:
                # Sort the lines in memory using Bubble Sort sorting algorithm
                sorted_lines = InMemorySort.sort(block_of_lines)

                # Save into partial file the sorted lines
                self._dump_into_partial_file(sorted_lines, partial_file_number)

                # Increment the partial file number, in this way we will have all the
                # Partial files numbered
                partial_file_number += 1

            else:
                do_we_continue = False
        # We store the amount of partial files
        self.partial_files_count = partial_file_number

    # Return the amount of partial files generated
    def get_amount_of_partial_files(self) -> int:
        return self.partial_files_count

    # Private method that will dump the chunk of lines into a file
    # The names of such files is defined in the class variable PARTIAL_FILE_NAME
    # Been of the format:
    #   split_0.partial -> Containing the first block of lines
    def _dump_into_partial_file(self, chunk_of_lines: list, partial_file_identifier: str):
        # As we know that the variable is string we can substitute the value
        # https://docs.python.org/3.4/library/stdtypes.html#str.format
        print('Writing into partial file:', partial_file_identifier)
        file = open(self.partial_file_name.format(partial_file_identifier), 'w')

        # Note: on writing we use the empty string and join since the input is a list
        # And we need to write it in the file as lines.
        file.write(''.join(chunk_of_lines))
        file.close()
