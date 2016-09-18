import unittest

from source.merge_file import MergeFile


class TestMergeFile(unittest.TestCase):
    def setUp(self):
        self.merge_file = MergeFile(
            partial_files_list=['test_partial0.partial', 'test_partial1.partial']
        )

    def test_merge(self):
        expected_sorted_file = [
            "anapaestically arabitol patulous liquidator butadiene underprize glomerulonephritis hugeness obliquate sixer alizarate jonvalize cuirassier hurroo sedulousness masterlessness\n",
            "codify microtomist roadless underlevel indictable sobber marline viridine amenia phrenicectomy metabasis mongrelly bacilliform teacherlike travertine inveigher\n"
        ]
        self.merge_file.merge()
        sorted_file = open('sorted_big_file.txt').readlines()
        self.assertEquals(expected_sorted_file, sorted_file)
