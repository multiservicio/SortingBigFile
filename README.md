# External Sort Exercise

## Motivation

External sorting is a term for a class of sorting algorithms that can handle massive amounts of data. Problem: You have a very large text file, so it does not fit in memory, with text lines. Sort the file into an output file where all the lines are sorted in alphabetic order, taking into account all words per line. The lines themselves do not need to be sorted and are not to be modified. Lines are considered to be average in length so edge cases such as a file with just two very large lines should still work but it is OK if performance suffers in that case.

Use any common programming language you like for the first approach. Please use standard libraries only, no batch or stream processing frameworks. Be as efficient as possible and do not use standard library sorting routines, write your own (remember, also no Github, StackOverflow or externally provided sorting solutions). Provide a rationale for your approach. Design schemes are welcome. Expectations: make sure you generate a 300MB or 400MB text file and sort it before handing over your assignment code

## External Sorting Algorithm

The file are big enought to not fit in memory so they need to be splitted into smaller ones that can be managed (sorted) on memory for efficiency and performance. 

Steps:

- Given a large file
- Divide the file into a smaller ones (for this step we need to take in consideration the memory). In our implementation the memory usage is hardcoded in the file ```sort_big_file.py```.  In case of change just modify if directly. 
- Those smaller files can be, then, sorted in memory. As our exercise do not allow to use built in sorting funcions we will need to implement our sorting strategy. In a first iteration of the code we implemented [Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort) and then while running tests with test file the times where very big (around 10 minutes for sorting ~160 MB file). Then we implemented [Quick Sort](https://en.wikipedia.org/wiki/Quicksort) strategy and it reduced the time until something less than 1 minute (over the same test file)
- Once we have splitted the file into smaller sorted ones is time to merge them again into a final sorted file. In this case we will use the [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort) approach and exactly the algorithm that is described in the Wikipedia article about [External Sorting](https://en.wikipedia.org/wiki/External_sorting) with the K Way Merging strategy. 




## Execution of the program

**Requirements:**

- Python 3.4 (as we are using certain syntax from the newer version [Typing](https://docs.python.org/3/library/typing.html))

In order to generate a random file we can use this small bash line
 
```ruby -e 'a=STDIN.readlines;3000000.times do;b=[];16.times do; b << a[rand(a.size)].chomp end; puts b.join(" "); end' < /usr/share/dict/words > unsorted.txt```

Then we execute the entry point

```python sort_big_file.py```


## Bibliography
- https://en.wikipedia.org/wiki/External_sorting
- https://www.youtube.com/watch?v=ATK74YSzwxg
- http://pages.cs.wisc.edu/~jignesh/cs564/notes/lec07-sorting.pdf
- https://inst.eecs.berkeley.edu/~cs186/sp08/notes/08-Sorting.pdf
- https://en.wikipedia.org/wiki/Merge_algorithm
- https://en.wikipedia.org/wiki/Quicksort
- https://en.wikipedia.org/wiki/Merge_sort
- https://en.wikipedia.org/wiki/Bubble_sort


## Author
Pedro Díaz (name dot surname at kiosked dot com)

