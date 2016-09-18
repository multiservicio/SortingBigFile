

# Merge File is the class where the responsibility of merging the partial files into
# a sorted merged one
class MergeFile:

    # When creating an instance of this object we will pass the amount of partial files.
    # The reason of this is to be able to merge those files
    # NOTE: This is a naive approach and assumes the folder only contains the correct files
    def __init__(self, partial_files_list: list):
        self.partial_files_list = partial_files_list
        self.number_of_partial_files = len(self.partial_files_list)
        self.sorted_file = None

        # We create a dict with the same amount of entries as partial files
        # In this dict we will be loading always the first line of each partial
        # This first lines will be always the "smaller" item of the partial
        # since they are sorted.
        self.dict_of_first_lines_of_each_partial = {
            i: None for i in range(self.number_of_partial_files)
        }

        # This will be the unique list of files that are "totally" processed. Meaning that
        # All its lines are already in the merged file
        self.exhausted_files = set()

    # This is the main method. Here is implemented the merging of the partial files into
    # a single one.
    def merge(self):
        pass

    # This method will create an array of file handlers
    # it will contain all the partial files handlers
    def _create_file_handlers_for_partial_files(self) -> list:
        handler_list = []
        for i in range(self.number_of_partial_files):
            handler_list.append(
                open(self.partial_files_list[i], 'r')
            )
        return handler_list

    # This method keeps the dictionary always with all the first lines of all the partial files
    # that still have lines.
    # E.g: if we have 3 partial lines this dict will consist of 3 items and in each index it will be
    # the first line of each file always meanwhile we do not reach EOF.
    def _load_dict_of_first_lines_of_each_partial(self, list_of_file_handlers: list) -> bool:
        for i in range(self.number_of_partial_files):
            # We check that the dict entry is None (no line assigned yet) and that the file still has
            # lines to sort.
            if self.dict_of_first_lines_of_each_partial[i] is None and i not in self.exhausted_files:
                # Assign first line of the file to the dict position
                line_read = list_of_file_handlers[i].readline()
                # If there is no empty line
                if line_read:
                    self.dict_of_first_lines_of_each_partial[i] = line_read
                else:
                    # Here we are marking the file as exhausted (ended).
                    self.exhausted_files.add(i)

            # This means that all the files are processed hence we do not have any more lines to sort.
            if self.number_of_partial_files == len(self.exhausted_files):
                return False
            else:
                return True



