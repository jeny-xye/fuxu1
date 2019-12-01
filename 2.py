""" 
HW03 : Fraction Calculation
Author: XinYi Ye
Date: 09/17/2019
"""
import unittest
class Fraction:
    """ Fraction class: support addition, substraction, multiplication, division and some 
        simple calculation
    """
    def __init__(self, num , denom):      
        """ set num and denom,raise ValueError when denom = 0"""
        self.num = num    
        #  
        self.denom = denom
        if denom == 0:
            raise ValueError('0 is an invalid denominator') 
    def __str__(self):
        """ string to display fraction"""
        return(f"{self.num} / {self.denom}")    
    def __add__(self, other):
        """ addition: add two fractions"""
        bottom = self.denom * other.denom
        top = self.num * other.denom +  self.denom * other. num
        return Fraction(top,bottom) 
    def __sub__(self,other): 
        """ substraction of two fractions"""
        bottom = self.denom * other.denom
        top = self.num * other.denom - self.denom * other.num
        return Fraction(top,bottom) 
    def __mul__(self,other):
        """ multiplication of two fractions"""
        bottom = self.denom * other.denom
        top = self.num * other.num
        return Fraction(top,bottom) 
    def __truediv__(self,other):
        """ division of two fractions"""
        bottom = self.denom * other.num
        top = self.num * other. denom
        return Fraction(top,bottom)
    def __eq__(self,other):
        """ return True if two fractions are equivalent"""
        if self.denom * other.num == self.num * other.denom:
            return True
        else:
            return False
    def __ne__(self,other):
        """ return True if two fractions are not equivalent"""
        if self.denom * other.num != self.num * other.denom:
            return True
        else:
            return False
    def __lt__(self,other):
        """ return True when the first fraction is less than the second fraction"""
        if self.num * other.denom - self.denom * other.num < 0:
            return True
        else:
            return False
    def __le__(self,other):
        """ return True when the first fraction is less than or equal to the second fraction"""
        if self.num * other.denom - self.denom * other.num <= 0:
            return True
        else:
            return False
    def __gt__(self,other):
        """ return True when the first fraction is greater than the second fraction"""
        if self.num * other.denom - self.denom * other.num > 0:
            return True
        else:
            return False
    def __ge__(self,other):
        """ return True when the first fraction is greater than or equal to the second fraction"""
        if self.num * other.denom - self.denom * other.num >= 0:
            return True
        else:
            return False
       
class TestFraction(unittest.TestCase):
    """ TestFraction: test cases"""
    def test_init(self):
        """ verify the numerator and denominator are set properly"""
        m = Fraction(1,2)
        self.assertEqual(m.num,1)
        self.assertEqual(m.denom,2)
        with self.assertRaises(ValueError):
            Fraction(3,0)
            Fraction(3.4,0)
    def test__str(self):
        """ verify that __str__ works properly"""
        m1 = Fraction(2,3)
        self.assertEqual(str(m1),'2 / 3')
    def test__add(self):
        """ test fraction addition """
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,2)
        self.assertTrue((m1 + m1) == Fraction(12,9))
        self.assertTrue((m1 + m2) == Fraction(17,12))
        self.assertTrue((m2 + m1) == Fraction(17,12))
        self.assertTrue(((m1 + m2) + m3) == Fraction(46,24))
    def test__sub(self):
        """ test fraction substraction"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,2)
        self.assertTrue((m1 -m1) == Fraction(0,1))
        self.assertTrue((m1 - m2) == Fraction(-1,12))
        self.assertTrue((m2 - m1) == Fraction(1,12))
        self.assertTrue(((m1 - m2) - m3) == Fraction(-14,24)) 
    def test__mul(self):
        """ test fraction multiplication"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,2)
        self.assertTrue((m1 * m1) == Fraction(4,9))
        self.assertTrue((m1 * m2) == Fraction(6,12))
        self.assertTrue((m2 * m1) == Fraction(6,12))
        self.assertTrue(((m1 * m2) * m3) == Fraction(6,24))
    def test__truediv(self):
        """ test fraction division"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,2)
        self.assertTrue((m1 / m1) == Fraction(1,1))
        self.assertTrue((m1 / m2) == Fraction(8,9))
        self.assertTrue((m2 / m1) == Fraction(9,8))
        self.assertTrue(((m1 / m2) / m3) == Fraction(16,9))
    def test__eq(self):
        """ test whether fractions are equivalent"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,1)
        self.assertFalse(m1 == m2)
        self.assertTrue(m1 == m1)
        self.assertFalse(m2 == m1)
        self.assertTrue((m1 / m3) == m1)
    def test__ne(self):
        """ test fractions are not equivalent"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,1)
        self.assertTrue(m1 != m2)
        self.assertTrue(m2 != m1)
        self.assertFalse(m1 != m1)
        self.assertTrue((m1 * m3) != m2)
    def test__lt(self):
        """ test whether the first fraction is less than the second fraction"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(1,2)
        self.assertFalse(m1 < m1)
        self.assertTrue(m1 < m2)
        self.assertFalse(m2 < m1)
        self.assertFalse(m3 < m3)
        self.assertTrue(m1 < (m2+ m3))
    def test__le(self):
        """ test whether the first fraction is less than or equal to the second fraction"""
        m1 = Fraction(2,3)
        m2 = Fraction(3,4)       
        m3 = Fraction(2,3)
        self.assertTrue(m1 <= m1)
        self.assertTrue(m1 <= m2)
        self.assertFalse(m2 <= m1)
        self.assertTrue((m1 - m3) <= m2)
    def test__gt(self):
        """ test whether the first fraction is greater than the second fraction"""
        m1 = Fraction(1,4)
        m2 = Fraction(2,3) 
        m3 = Fraction(1,4)
        self.assertTrue(m2 > m1)
        self.assertFalse(m1 > m2)
        self.assertFalse(m1 > m1)
        self.assertFalse(m1 > m3)
    def test__ge(self):
        """ test whether the first fraction is greater than or equal to the second fraction"""
        m1 = Fraction(1,4)
        m2 = Fraction(2,3) 
        self.assertTrue(m1 >= m1)
        self.assertTrue(m2 >= m1)
        self.assertFalse(m1 >= m2)
        self.assertTrue((m1 + m2) >= m2)
if __name__ == "__main__":
    """ main function """
    unittest.main(exit = False, verbosity=2)


