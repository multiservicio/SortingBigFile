import os

from merge_file import MergeFile
from split_file import SplitFile


# External Sort Algorithm class
# This class is meant to be the simplest implementation of the external sort algortithm
# References to the Wikipedia article -> https://en.wikipedia.org/wiki/External_sorting
class ExternalSorting:

    # When creating an instance of this object we must specify the size of the chunk
    # Been the chunk the amount of "lines" of our big file.
    def __init__(self, chunk_size):
        self.chunk_size = chunk_size

    # Sort is the public method that performs the literal sorting algorightm.
    # In this case the flow is the following
    # We split the big file into smaller files (that they can fit on memory).
    # They need to fit in memory so we can sort each "piece" faster
    # Then we have to merge all this files until we have again a single final file
    # That is sorted.
    def sort(self, file_name):
        # First we need to know how big is the file and then calculate the number of "divisions" of it
        # We will put this into a "private" method
        number_of_partial_files = self._get_number_of_partial_files(file_name, self.chunk_size)

        # Next will be the actual split of the big file.
        # Each partial file will be already sorted within itself.
        split_files = SplitFile(file_name)
        split_files.split()

        # Now we have the file already divided in number_of_partial_files and each of the partials
        # are already sorted within themselves.
        # Next is time to merge all those files into the final sorted one.
        # In order to merge there are several possible strategies.
        # According to https://en.wikipedia.org/wiki/Merge_algorithm we can use K way merging strategy
        merged_file = MergeFile()
        merged_file.merge()

    # This "private" method will return the number of partial files we will split our big file.
    # In order to know that number we need to know the maximum number of lines we can handle in memory
    # and the size of the current file. (for this we will use built in OS library)
    def _get_number_of_partial_files(self, file_name, chunk_size):
        # Reference to OS stat and size -> https://docs.python.org/2/library/os.html#os.stat
        file_size = os.stat(file_name).st_size

        # The total number of partial files will be the size of the file divided by the total amount of lines
        # (in this case memory available to perform the in memory sorting)
        # Plus 1. This +1 is intended for TODO
        number_of_partial_files = (file_size / chunk_size) + 1

        return number_of_partial_files
