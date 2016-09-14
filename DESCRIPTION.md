# Very large file sorting


Hint: External sorting is a term for a class of sorting algorithms that can handle massive amounts of data.

Problem: You have a *very* large text file, so it does not fit in memory, with text lines. Sort the file into an output file where all the lines are sorted in alphabetic order, taking into account all words per line. 
The lines themselves do not need to be sorted and are not to be modified. 
Lines are considered to be average in length so edge cases such as a file with just two very large lines should still work but it is OK if performance suffers in that case.


Boundary: Use any programming language you like for first approach, but we require the deliverable to be in Java/Scala so it can be tested on any common JVM. Please use standard libraries only, no batch or stream processing frameworks. Be as efficient as possible while avoiding using standard library sorting routines. Provide a rationale for your approach. Design schemas are welcome.


Please note that the file.txt that we use to measure the performance of the result is generated via:  ```ruby -e 'a=STDIN.readlines;5000000.times do;b=[];16.times do; b << a[rand(a.size)].chomp end; puts b.join(" "); end' < /usr/share/dict/words > file.txt```

Please upload code to your bitbucket.org account so we can checkout from there. Please add also our collaborators:  dvpablo, paugay,  alexramirez, tomoki_kamo and pnikosis.


-------


Very large file sorting
-------------------------
External sorting is a term for a class of sorting algorithms that can handle massive amounts of data.
Problem: You have a *very* large text file, so it does not fit in memory, with text lines. Sort the file into an output file where all the lines are sorted in alphabetic order, taking into account all words per line. The lines themselves do not need to be sorted and are not to be modified. Lines are considered to be average in length so edge cases such as a file with just two very large lines should still work but it is OK if performance suffers in that case.

Use any common programming language you like for the first approach. Please use standard libraries only, no batch or stream processing frameworks. Be as efficient as possible and do not use standard library sorting routines, write your own (remember, also no Github, StackOverflow or externally provided sorting solutions). Provide a rationale for your approach. Design schemes are welcome.
Expectations: make sure you generate a 300MB or 400MB text file and sort it before handing over your assignment code

Deadline: 1 week

You can send a ZIP file