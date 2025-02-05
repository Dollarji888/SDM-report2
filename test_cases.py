#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        def test_boundary_value (self):
                self.assertEqual (-1, calc(0,500))
                self.assertEqual (500, calc(1,500))
                self.assertEqual (24975, calc(25,999))
                self.assertEqual (-1, calc(25,1000))

        
        def test_equivalence (self): 
                self.assertEqual (-1, calc(-500,450))
                self.assertEqual (80000, calc(200,400))
                self.assertEqual (-1, calc(240, 2500))
                self.assertEqual (-1, calc(1000,1200))

        
        def test_others (self):
                self.assertEqual (-1, calc(600,0))
                self.assertEqual (-1, calc(1000,500))
                self.assertEqual (-1, calc("080",181))  
                self.assertEqual (-1, calc("",""))  
                self.assertEqual (-1, calc(0,0))  
                self.assertEqual (-1, calc("Hello","World")) 
                self.assertEqual (-1, calc("21ab15",3)) 
                self.assertEqual (-1, calc("２０",24))  

                                            
