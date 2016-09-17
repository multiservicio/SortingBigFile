

# Merge File is the class where the responsibility of merging the partial files into
# a sorted merged one
class MergeFile:

    # When creating an instance of this object we will pass the amount of partial files.
    # The reason of this is to be able to merge those files
    # NOTE: This is a naive approach and assumes the folder only contains the correct files
    def __init__(self, total_amount_of_partial_files: int, partial_file_name: str = 'split_{0}.partial'):
        self.partial_files = total_amount_of_partial_files
        self.partial_file_name = partial_file_name

    # This is the main method. Here is implemented the merging of the partial files into
    # a single one.
    def merge(self):
        pass
