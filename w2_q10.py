#Authors: Lucky John Mbikeshimana , Nguimeya Marthely, Irene Mutamuliza



#Question 10


def ListOfIntegers(the_integer):
   # the_integer = int(input("Enter a number: "))


    list2 = []


    for i in range(the_integer):
        number = 1 +i

        for j in range(number):
            list2.append(number)

    
    print(list2)


ListOfIntegers(5)


#Time complexity: O(n^2)

#Space complexity: O(n)

import unittest

class Test_ListOfIntegers(unittest.TestCase):

    def ListOfIntegers(self):

        test_list2 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

        self.assertEqual(ListOfIntegers(5), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])