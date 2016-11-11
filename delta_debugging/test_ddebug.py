
from unittest import TestCase, main
from ddebug import get_partitions, delta_debug
from stringsearch import no_rats
from sudoku import draw_sudoku
from test_sudoku import create_random_constraints, test_sudoku


class PartitionTests(TestCase):

    def test_get_partitions(self):
        data = "ABCDEFG"
        result = get_partitions(data, 2)
        result.sort()
        self.assertEqual(result, ["ABC", "DEFG"])
        result = get_partitions(data, 3)
        self.assertEqual(result, ["CDEFG", "ABEFG", "ABCD"])
        result = get_partitions(data, 4)
        self.assertEqual(result, ["BCDEFG", "ADEFG", "ABCFG", "ABCDE"])


class DeltaDebugTests(TestCase):

    def test_ddebug_string(self):
        s = "this is a long string with a big rat inside"
        result = delta_debug(s, no_rats)
        self.assertEqual(result, 'rat')

    def test_ddebug_string_nofail(self):
        s = "string without failure"
        self.assertRaises(AssertionError, delta_debug, s, no_rats)

    def test_ddebug_sudoku(self):
        constraints = [(1,1,9), (1,2,3), (8,8,7), (2,2,9)]
        minimal = delta_debug(constraints, test_sudoku)
        self.assertEqual(minimal, [(1,1,9), (2,2,9)]) 

    def test_ddebug_sudoku_duplicate_pos(self):
        constraints = [(1,1,9), (1,1,8), (8,8,7), (2,2,5)]
        minimal = delta_debug(constraints, test_sudoku)
        self.assertEqual(minimal, [(1,1,9), (1,1,8)]) 

    def test_ddebug_sudoku_complex(self):
        constraints = [(1,1,1), (2,1,2), (3,1,3), (4,2,1), (5,2,2), (6,2,3), (7,3,7), (8,3,8), (9,3,9)]
        minimal = delta_debug(constraints, test_sudoku)

    def test_ddebug_sudoku_random(self):
        for i in range(10):
            constraints = create_random_constraints()
            if test_sudoku(constraints) == 'FAIL':
                print("run #", i)
                print(i, "#constraints:", len(constraints))
                minimal = delta_debug(constraints, test_sudoku)
                print(draw_sudoku(constraints))
                print(draw_sudoku(minimal))
                print(minimal)

if __name__ == '__main__':
    main()