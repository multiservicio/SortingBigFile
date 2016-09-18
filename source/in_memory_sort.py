

# In Memory Sort is a Class intented to sort the lines that fit into memory.
# For this example Bubble Sort is the selected for its simplicity on the implementation
class InMemorySort:

    # Static method since there is no need to instanciate an object
    # Bubble Sort is one of the basic sorting algorithm
    # https://en.wikipedia.org/wiki/Bubble_sort
    @staticmethod
    def bubble_sort(data: list) -> list:
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

