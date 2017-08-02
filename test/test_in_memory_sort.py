import unittest
import source

from source.in_memory_sort import InMemorySort


class TestInMemorySort(unittest.TestCase):
    def setUp(self):
        self.test_chunk_of_lines = [
            "promotrix curialism walk triploidite diluvion toddle nucleoalbumin disestablishmentarian redberry lapsi Hitchiti gladsome prehatred hatchettine herem unworthily",
            "vociferousness subterrene pseudoperspective nonfuroid apogaeic ratchment coltpixie temporale betrothed enzymatic undergraduate palp screwmatics Cystopteris Tragopogon ramroddy",
            "nesquehonite pah damewort acnemia papyrology cantilena hacked anagrammatist santir Ribhus ichnomancy marrowy tidehead Pteropidae Coniferae dayflower",
        ]
        self.expected_sorted_lines = [
            "nesquehonite pah damewort acnemia papyrology cantilena hacked anagrammatist santir Ribhus ichnomancy marrowy tidehead Pteropidae Coniferae dayflower",
            "promotrix curialism walk triploidite diluvion toddle nucleoalbumin disestablishmentarian redberry lapsi Hitchiti gladsome prehatred hatchettine herem unworthily",
            "vociferousness subterrene pseudoperspective nonfuroid apogaeic ratchment coltpixie temporale betrothed enzymatic undergraduate palp screwmatics Cystopteris Tragopogon ramroddy"
        ]

    def test_bubble_sort(self):
        sorted_lines = InMemorySort._bubble_sort(self.test_chunk_of_lines)
        self.assertEqual(self.expected_sorted_lines, sorted_lines)
