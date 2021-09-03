# -*- coding: utf-8 -*-
"""
Troy Ascher
Class: CS 521 - Fall 2
Date:Sat Dec 12 10:29:40 2020
Homework Problem #
Description of Problem:


#80 Character Limit -----------------------------------------------------------
"""

class Likert(int):
    """
    This class is for objects that represent a Likert scale, which is a
    scale of integers from min to max. It defaults to a scale from 1 - 7
    """

    __scale_bottom = 1 # private attribute 

    # For this program, the lowest value on on a Likert scale should always be 1.

    def __init__(self, value=4, maximum=7):
        """
        Initiliazes instances
        """

        if not (isinstance(maximum, int)) or not (isinstance(value, int)):
            raise NotIntegerError("Value and maximum need to be integers.")
        
        self.max_int = maximum # 1st public attribute
        
        if not (self.__scale_bottom <= value <= maximum):
            raise InvalidRangeError(f"Value should be from {self.__scale_bottom} to {self.max_int}")
        
        self.value_int = value # 2nd public attribute
    

    def __str__(self):
        """prints the name of the instance and range of the likert scale"""
        return f"This is the value {self.value_int} on a Likert"\
            f" scale from {self.__scale_bottom} to {self.max_int}"
    
    
    def __repr__(self):
        """ Official representation of Likert class."""
        return f"Likert: {self.value_int}, scale: {self.__scale_bottom} -> "\
            f"{self.max_int}"
    
    def __lt__(self, other):
        """ allows comparison of self to an integer and only an 
        integer.
        """
        val_1 = int(self.value_int)
        val_2 = int(other)
        if val_1 < val_2:
          return True
        else:
          return False


    def __le__(self, other):
        
        """ allows comparison of self to an integer and only an 
        integer.
        """
        val_1 = int(self.value_int)
        val_2 = int(other)
        if val_1 <= val_2:
            return True
        else:
            return False


    def __set_scale_bottom(self, value): # The private method
        """ 
        A private method to change the scale bottom for a particular instance.
        """
        
        if not (isinstance(value, int)):
            raise NotIntegerError("Value must be be integer.")
            
        self._Likert__scale_bottom = value
        return f"The scale bottom will be updated to {value} if method is run."

    
    def print_scale(self): # Required puiblic method. 
        """
        A public method that takes the name of the instance and
        prints the range of the likert scale for that instance by returning
        the lowests value and the highest value

        """
        return f"The Likert scale is from {self.__scale_bottom} to {self.max_int}"

            
class NotIntegerError(Exception):
    """
    This is a custom exception for objects that are not integers.
    """
    pass


class InvalidRangeError(Exception):
    """
    This is a custom exception for objects that are out of range.
    """
    pass


if __name__ == "__main__":
    
    test_int_1 = 3
    print(test_int_1)
    
    # pass integer directly into class
    test_likert_1 = Likert(test_int_1)
    print(test_likert_1)
    test_int_2 = 5
    print(test_int_2)
    test_likert_2 = Likert(test_int_2, 9)
    
    test_1_bool = test_int_2 < 5
    
    test_2_bool = test_int_1 <= test_int_2
    
    print(test_likert_1.print_scale())
    
    print(test_likert_1._Likert__set_scale_bottom(4))
    print(test_likert_1)
    print(test_likert_1.print_scale())
    print(test_likert_2)
    print(test_likert_2.print_scale())
    
    repr(test_likert_1)