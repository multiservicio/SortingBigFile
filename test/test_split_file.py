import unittest
import source

from source.split_file import SplitFile


class TestSplitFile(unittest.TestCase):
    def setUp(self):
        size_in_bytes_of_each_partial = 10 * 1024
        self.split_object = SplitFile('test_split_unsorted.txt', size_in_bytes_of_each_partial)

    def test_split_file_in_partial_sorted_files(self):
        self.split_object.split()
