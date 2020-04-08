from typing import Dict,List
import unittest

from HW09_Rohan_Ratwani import Repository

class Test(unittest.TestCase):
    """Helps to test all the functions"""
    def test_data_for_Student(self):
        """This function is used to test data_for_student function's output"""
        stevens: Repository = Repository("R:\Stevens\Sem-2\SSW-810\HW_09_Rohan_Ratwani")
        calculated: List = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                            ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                            ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                            ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
                            ['10183', 'Chapman, O', ['SSW 689']],
                            ['11399', 'Cordova, I', ['SSW 540']],
                            ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                            ['11658', 'Kelly, P', ['SSW 540']],
                            ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                            ['11788', 'Fuller, E', ['SSW 540']]]

        calculated1: List = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                            ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                            ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                            ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
                            ['10183', 'Chapman, O', ['SSW 689']],
                            ['211399', 'Cordova, I', ['SSW 540']],
                            ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                            ['11658', 'Kelly, P', ['SSW 540']],
                            ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                            ['11788', 'Fuller, E', ['SSW 540']]]

        self.assertEqual(stevens.student_pretty_table(), calculated)
        self.assertNotEqual(stevens.student_pretty_table(), calculated1)

    def test_data_for_Instructor(self):
        """This function is used to test data_for_instructor function's output"""
        stevens: Repository = Repository("R:\Stevens\Sem-2\SSW-810\HW_09_Rohan_Ratwani")
        calculated: List = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                            ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
                            ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                            ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                            ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                            ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
                            ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                            ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        calculated1: List = [['987656', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                            ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
                            ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                            ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                            ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                            ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
                            ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                            ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                            ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]


        self.assertEqual(stevens.instructor_pretty_table(), calculated)
        self.assertNotEqual(stevens.instructor_pretty_table(), calculated1)





if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
