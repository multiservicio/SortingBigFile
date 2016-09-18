import os

from source.merge_file import MergeFile
from source.split_file import SplitFile


# External Sort Algorithm class
# This class is meant to be the simplest implementation of the external sort algorithm
# References to the Wikipedia article -> https://en.wikipedia.org/wiki/External_sorting
class ExternalSorting:

    # When creating an instance of this object we must specify the size of the chunk
    # Been the chunk the amount of memory use to chop our big file.
    def __init__(self, chunk_size: int, file_name: str, partial_file_name: str = 'split_{0}.partial'):
        self.chunk_size = chunk_size
        self.file_name = file_name
        self.partial_file_name = partial_file_name

    # Sort is the public method that performs the literal sorting algorithm.
    # In this case the flow is the following
    # We split the big file into smaller files (that they can fit on memory).
    # They need to fit in memory so we can sort each "piece" faster
    # Then we have to merge all this files until we have again a single final file
    # That is sorted.
    def sort(self):

        # Next will be the actual split of the big file.
        # Each partial file will be already sorted within itself.
        split_files = SplitFile(
            file_name=self.file_name,
            chunk_size=self.chunk_size,
            partial_file_name=self.partial_file_name
        )
        print('Splitting files...')
        split_files.split()

        # First we need to know how big is the file and then calculate the number of "divisions" of it
        # We will put this into a "private" method
        number_of_partial_files = split_files.get_amount_of_partial_files()

        # Now we generate a list of all the files that are set to be merge
        partial_files = self._create_list_of_partial_files(
            number_of_partial_files=number_of_partial_files
        )

        # Now we have the file already divided in number_of_partial_files and each of the partials
        # are already sorted within themselves.
        # Next is time to merge all those files into the final sorted one.
        # In order to merge there are several possible strategies.
        # According to https://en.wikipedia.org/wiki/Merge_algorithm we can use K way merging strategy
        merged_file = MergeFile(
            partial_files_list=partial_files
        )
        print('Merging files...')
        merged_file.merge()

    # This "private" method will return the number of partial files we will split our big file.
    # In order to know that number we need to know the maximum number of 'lines' we can handle in memory
    # and the size of the current file. (for this we will use built in OS library)
    # The calculation will be the size of the file divided by the data we can/want to store in memory for the
    # sort of each of the partial files
    def _get_number_of_partial_files(self, file_name: str):
        # Reference to OS stat and size -> https://docs.python.org/2/library/os.html#os.stat
        file_size = os.stat(file_name).st_size

        # The total number of partial files will be the size of the file divided by memory we want/can use
        # Plus 1 for the rest (in case is the division is not exact)
        number_of_partial_files = (file_size / self.chunk_size) + 1

        return int(number_of_partial_files)

    # This "private" method will provide a list of the names of all the generated partial
    # Files. The purpose of this is to pass this list to the merge step so it knows
    # Which files to merge
    def _create_list_of_partial_files(self, number_of_partial_files: int) -> list:
        partial_files_list = []
        for i in range(number_of_partial_files):
            partial_files_list.append(self.partial_file_name.format(i))

        return partial_files_list
