########################################################################
##
## CS 101 Lab
## Program 13
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: Create unittests for basic math functions.
##
## ALGORITHM: 
##      1. Add a group of numbers and test.
##      2. Average a group of numbers and test.
##      3. Find the median of a group of numbers and test.
## 
## ERROR HANDLING:
##      1. Raises ValueError if attempting to find the median of an empty list.
##      
## OTHER COMMENTS:
##      
##
########################################################################

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):

        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")

    def test_total_returns_0(self):

        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0')

    def test_average_one(self):

        result = Grades.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.33333, 5, 'The average function should return 5.33333')

    def test_average_two(self):

        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12.0000, 4, 'The average function should return 12.0000')

    def test_average_returns_nan(self):

        result = Grades.average([])
        self.assertIs(result, math.nan, 'The average function should return math.nan')

    def test_median_one(self):

        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2, 'The median function should return 2')

    def test_median_one(self):

        result = Grades.median([1, 2, 3, 5])
        self.assertEqual(result, 2.5, 'The median function should return 2.5')

    def test_median_error(self):

        with self.assertRaises(ValueError):
            results = Grades.median([])

unittest.main()
