

# Merge File is the class where the responsibility of merging the partial files into
# a sorted merged one
class MergeFile:

    # When creating an instance of this object we will pass the amount of partial files.
    # The reason of this is to be able to merge those files
    # NOTE: This is a naive approach and assumes the folder only contains the correct files
    def __init__(self, partial_files_list: list):
        self.partial_files_list = partial_files_list
        self.number_of_partial_files = len(self.partial_files_list)

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
    #
    # Algorithm:
    #   We get all the partial files open and we read the first lines of all of those files
    #   We put all the lines in a dict structure. As all the partials are sorted the next step is to find
    #   The smallest one among those lines.
    #   Once we find the smallest one, we remove it form the dict and dump into the sorted file.
    #   After this step we provision again the dictionary with the next line of that file (if we didn't reach EOF).
    #   This loop will end when all the files are consumed.
    #
    def merge(self):
        sorted_file = open('sorted_big_file.txt', 'w')
        # Get all the file handlers of the partial files
        list_of_partial_file_handlers = self._create_file_handlers_for_partial_files()

        # Loop for merging.
        # On each iteration we will be writing one line
        # That line will be always the smallest string of all the pre-loaded lines on the dictionary.
        while self._load_dict_of_first_lines_of_each_partial(list_of_partial_file_handlers):
            line_to_write = self._pop_line_from_dict_of_first_lines(self._find_smaller_item_in_dictionary())
            sorted_file.write(line_to_write)

        sorted_file.close()

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

    # This method will be the one removing the values from the dictionary
    # The purpose is that once we need this line we pop it out of the dict
    # to write it into the merged file.
    def _pop_line_from_dict_of_first_lines(self, index: int) -> str:
        # We save the string (line)
        line_str = self.dict_of_first_lines_of_each_partial[index]
        # We mark it as None so the method '_load_dict_of_first_lines_of_each_partial' can load the next
        # line (if there is next).
        self.dict_of_first_lines_of_each_partial[index] = None
        return line_str

    # Here is where the N Way Merge takes place.
    # In order to select the smaller (Alphabetically higher) index of the dictionary
    # The implementation is as easy as iterating through the dictionary and compare each of them
    # To find the smallest one
    def _find_smaller_item_in_dictionary(self) -> int:
        min_item_index = -1
        str = None

        for i in range(len(self.dict_of_first_lines_of_each_partial)):
            # We compare each value against the minimum and we carry on until we find another that is
            # smaller until the end of the dictionary
            if self.dict_of_first_lines_of_each_partial[i] is not None:
                if str is None or self.dict_of_first_lines_of_each_partial[i] < str:
                    str = self.dict_of_first_lines_of_each_partial[i]
                    min_item_index = i
        return min_item_index

