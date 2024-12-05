# CSC 110
# Project 5 - Test File
# Hwansu Kim (Billy)
# 10/27/21

import unittest
import project5hwansu


class FunctionTest(unittest.TestCase):

    def test_empRating(self):
        self.assertEqual("Probation",         project5hwansu.empRating(1))
        self.assertEqual("Probation",         project5hwansu.empRating(2))

        self.assertEqual("Needs Improvement", project5hwansu.empRating(3))
        self.assertEqual("Needs Improvement", project5hwansu.empRating(4))

        self.assertEqual("Acceptable",        project5hwansu.empRating(5))
        self.assertEqual("Acceptable",        project5hwansu.empRating(6))
        self.assertEqual("Acceptable",        project5hwansu.empRating(7))

        self.assertEqual("Good",              project5hwansu.empRating(8))
        self.assertEqual("Good",              project5hwansu.empRating(9))

        self.assertEqual("Excellent",         project5hwansu.empRating(10))

        self.assertEqual("ERROR",             project5hwansu.empRating(0))
        self.assertEqual("ERROR",             project5hwansu.empRating(0.99999))
        self.assertEqual("ERROR",             project5hwansu.empRating(1.5))
        self.assertEqual("ERROR",             project5hwansu.empRating(10.00001))
        self.assertEqual("ERROR",             project5hwansu.empRating(11))

    def test_pctToNsc(self):
        self.assertEqual(0,    project5hwansu.pctToNsc(0))
        self.assertEqual(0,    project5hwansu.pctToNsc(65))

        self.assertEqual(1.0,  project5hwansu.pctToNsc(66))
        self.assertEqual(3.9,  project5hwansu.pctToNsc(95))

        self.assertEqual(4.0,  project5hwansu.pctToNsc(96))
        self.assertEqual(4.0,  project5hwansu.pctToNsc(99.9999))
        self.assertEqual(4.0,  project5hwansu.pctToNsc(100))

        self.assertEqual(-9.9, project5hwansu.pctToNsc(-0.0000001))
        self.assertEqual(-9.9, project5hwansu.pctToNsc(-999))
        self.assertEqual(-9.9, project5hwansu.pctToNsc(100.000001))
        self.assertEqual(-9.9, project5hwansu.pctToNsc(999))

    def test_isDivisibleBy5or7or11(self):
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(5))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(7))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(11))

        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(35))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(55))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(77))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(385))

        self.assertEqual(False, project5hwansu.isDivisibleBy5or7or11(1))
        self.assertEqual(False, project5hwansu.isDivisibleBy5or7or11(4))
        self.assertEqual(False, project5hwansu.isDivisibleBy5or7or11(6))
        self.assertEqual(False, project5hwansu.isDivisibleBy5or7or11(8))

        self.assertEqual(False, project5hwansu.isDivisibleBy5or7or11(5.001))
        self.assertEqual(False, project5hwansu.isDivisibleBy5or7or11(4.999))

        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(10))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(0))
        self.assertEqual(True,  project5hwansu.isDivisibleBy5or7or11(-5))

    def test_commission(self):
        self.assertEqual(0,           project5hwansu.commission("Trainee",       0,    0,   1))
        self.assertEqual(0,           project5hwansu.commission("Associate",     0,    0,  23))
        self.assertEqual(0,           project5hwansu.commission("Lead",          0,    0,  23.999))
        self.assertEqual(0,           project5hwansu.commission("Manager",       0,    0, 120))

        self.assertEqual(202,         project5hwansu.commission("Trainee",   10000, 5000,  24))
        self.assertEqual(204,         project5hwansu.commission("Trainee",   10000, 5000,  48))
        self.assertEqual(206,         project5hwansu.commission("Trainee",   10000, 5000, 120))

        self.assertEqual(550,         project5hwansu.commission("Associate", 10000, 5000,  23))
        self.assertAlmostEqual(555.5, project5hwansu.commission("Associate", 10000, 5000,  47), 1)
        self.assertEqual(561,         project5hwansu.commission("Associate", 10000, 5000, 119))
        self.assertAlmostEqual(566.5, project5hwansu.commission("Associate", 10000, 5000, 121), 1)

        self.assertEqual(700,         project5hwansu.commission("Lead",      10000, 5000,  20))
        self.assertEqual(707,         project5hwansu.commission("Lead",      10000, 5000,  36))
        self.assertEqual(714,         project5hwansu.commission("Lead",      10000, 5000, 100))
        self.assertEqual(721,         project5hwansu.commission("Lead",      10000, 5000, 200))

        self.assertEqual(900,         project5hwansu.commission("Manager",   10000, 5000,   5))
        self.assertEqual(909,         project5hwansu.commission("Manager",   10000, 5000,  24))
        self.assertEqual(918,         project5hwansu.commission("Manager",   10000, 5000,  48))
        self.assertEqual(927,         project5hwansu.commission("Manager",   10000, 5000, 120))

        self.assertEqual(0,           project5hwansu.commission("Janitor", 10000, 5000, 120))
        self.assertEqual(0,           project5hwansu.commission("",          10000, 5000, 120))
        self.assertEqual(0,           project5hwansu.commission(100,         10000, 5000, 120))
        self.assertEqual(0,           project5hwansu.commission(0.01,        10000, 5000, 120))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(FunctionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()