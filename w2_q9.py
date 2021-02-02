#Authors: Lucky John Mbikeshimana , Nguimeya Marthely, Irene Mutamuliza


# Week 2
# Question 9

def list_handle(listA, listB):
    if len(listA) > len(listB):
        return set(listA).difference(listB)
    else:
        return set(listB).difference(listA)


listA = [6, 7, 8, 9, 10]
listB = [6, 7, 9, 10]

missing_el = list(list_handle(listA, listB))

print(*missing_el)

# Time Complexity: o(1)
# Space Complexity: o(1)

# Performing Unit Tests

import unittest


class TestQuestion9(unittest.TestCase):

    def test_text_handle(self):
        t_list1 = [1, 2, 3, 4]
        t_list2 = [1, 3, 4]
        self.assertEqual(list_handle(t_list1, t_list2), {2})

