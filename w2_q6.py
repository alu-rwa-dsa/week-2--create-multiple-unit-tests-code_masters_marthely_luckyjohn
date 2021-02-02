
#Authors: Lucky John Mbikeshimana , Nguimeya Marthely, Irene Mutamuliza


#Question 6: Removing white spaces in a text.

def Remove_Space():


    original_text = input("Please enter a text with white spaces: ")
    print(" ".join(original_text.split()))


Remove_Space()


#Time Complexity: O(1)

#Space Complexity: O(1)


import unittest

class TestQuestion6(unittest.TestCase):

    def test_remove_space(self):

        text1 = "This   is    the                worst                     sentence."
        text2 = "This is the worst sentence."

        self.assertEqual(Remove_Space(text1), text2)




