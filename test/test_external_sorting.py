import unittest
import os

from source.external_sorting import ExternalSorting


class TestExternalSorting(unittest.TestCase):
    def setUp(self):
        # Force to have it in 1K = 1 line
        size_in_bytes_of_each_partial = 1
        self.file_name = 'test_external_sorting_unsorted.partial'
        self.external_sorting = ExternalSorting(
            chunk_size=size_in_bytes_of_each_partial,
            file_name=self.file_name
        )

    def test_same_amount_of_partials_generated_than_calculated(self):
        # Here we are breaking the OOP and abusing of the lack of real private methods in Python
        # We are calling a "private" method in order to get the number of files it should be splitted
        calculated_partial_files = self.external_sorting._get_number_of_partial_files(self.file_name)
        self.external_sorting.sort()
        self.assertEquals(calculated_partial_files, 2)

