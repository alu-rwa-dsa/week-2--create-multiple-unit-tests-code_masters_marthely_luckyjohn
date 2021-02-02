
#Authors: Lucky John Mbikeshimana , Nguimeya Marthely, Irene Mutamuliza


#Question 7: Creating a Dictionary with number of occurences.


def Creating_A_Dictionary(the_string):




    new_dictionary = {}

    for i in range(len(the_string)):

        new_ones = {the_string[i] : i}
        new_dictionary.update (new_ones)
            

    print (new_dictionary)


Creating_A_Dictionary("LuckyJohn")


#Time Complexity: O(n)
#Space Complexity: O(n)

import unittest

class testing_Creating_A_Disctonary(unittest.TestCase):

    def create_dictornary(self):

        test_dictionary = {'L': 0, 'u': 1, 'c': 2, 'k': 3, 'y': 4, 'J': 5, 'o': 6, 'h': 7, 'n': 8}

        self.assertEqual(Creating_A_Dictionary("LuckyJohn"), test_dictionary)






