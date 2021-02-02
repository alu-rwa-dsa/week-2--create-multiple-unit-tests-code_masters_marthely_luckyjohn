
#Authors: Lucky John Mbikeshimana , Nguimeya Marthely, Irene Mutamuliza

def Splitting_Lists():

    list_of_list = input("Enter a list of lists: ")
    
    #We are inputting ['[[1,', '2,', '3],', '[4,', '5,', '6],', '[7,', '8,', '9]]'] for this case.

    splitted = list_of_list.split()

    print("The splitted list is: ",splitted)

    


Splitting_Lists()

#Time Complexity: O(1)
#Space Complexity: O(n)

import unittest

class Test_Splitting_Lists(unittest.TestCase):

    def Splitting_Lists(self):

        test_splitted_list = ['[[1,', '2,', '3],', '[4,', '5,', '6],', '[7,', '8,', '9]]']

        self.assertEqual(Splitting_Lists(), test_splitted_list)
