import random


# In Memory Sort is a Class intented to sort the lines that fit into memory.
# For this example Bubble Sort is the selected for its simplicity on the implementation
class InMemorySort:
    # We want to hide the implementation of the sorting algorithm so we will just "expose" this method
    # and here we will decide which algorithm to use.
    @staticmethod
    def sort(data: list) -> list:
        InMemorySort._quick_sort(
            list_of_strings=data,
            first_index=0,
            last_index=len(data) -1
        )
        return data

    # Static method since there is no need to instanciate an object
    # Bubble Sort is one of the basic sorting algorithm
    # https://en.wikipedia.org/wiki/Bubble_sort
    @staticmethod
    def _bubble_sort(data: list) -> list:
        print('In bubble sort... sorting:', len(data))
        for interval in range(len(data) - 1, 0, -1):
            # Range(interval) represents the index values from beginning to the interval of the list
            for index in range(interval):
                # If pos[0] bigger (alphabetically) than pos[0 + 1]
                if data[index] > data[index + 1]:
                    # Then swap positions
                    temp = data[index]
                    data[index] = data[index + 1]
                    data[index + 1] = temp

        return data

    # Quick sort algorithm -> https://en.wikipedia.org/wiki/Quicksort
    @staticmethod
    def _quick_sort(list_of_strings: list, first_index: int, last_index: int):
        #print('In quick sort... sorting:', len(list_of_strings))
        if first_index < last_index:
            pivot = InMemorySort._quick_sort_partition(list_of_strings, first_index, last_index)
            InMemorySort._quick_sort(list_of_strings, first_index, pivot - 1)
            InMemorySort._quick_sort(list_of_strings, pivot + 1, last_index)

    @ staticmethod
    def _quick_sort_partition(list_of_strings: list, first_index: int, last_index: int) -> int:
        pivot = first_index + random.randrange(last_index - first_index + 1)
        InMemorySort._swap_indexes(list_of_strings, pivot, last_index)
        for i in range(first_index, last_index):
            if list_of_strings[i] <= list_of_strings[last_index]:
                InMemorySort._swap_indexes(list_of_strings, i, first_index)
                first_index += 1

        InMemorySort._swap_indexes(list_of_strings, first_index, last_index)
        return first_index

    @staticmethod
    def _swap_indexes(list_of_strings: list, index_a: int, index_b: int):
        temp = list_of_strings[index_a]
        list_of_strings[index_a] = list_of_strings[index_b]
        list_of_strings[index_b] = temp