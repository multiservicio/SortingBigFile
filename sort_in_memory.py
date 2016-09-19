# Help script that will use solely built in and in memory sorting
# This is intented to create a reference file to verify the correctness of our implementation
f = open('unsorted.txt', 'r')
lines = f.readlines()
lines.sort()
fout = open('all_native.txt', 'w')
fout.write(''.join(lines))
fout.close()
