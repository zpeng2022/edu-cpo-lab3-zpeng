import unittest
import math
from hypothesis import given
import hypothesis.strategies as st
from DynamicArray import DynamicArray, cons, remove, length, isMember, reverse, to_list, from_list
from DynamicArray import find, filter_the_value, map_the_value, reduce, iterator_element, next_element
from DynamicArray import empty, concat


class TestDynamicArray(unittest.TestCase):
    def test_cons_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        l2 = cons(1, cons(None, emp))
        self.assertEqual(str(emp), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(emp, l1)
        self.assertNotEqual(emp, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(None, cons(1, emp)))

    @given(st.binary(), st.binary())
    def test_cons_binary(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        list1 = [a, b]
        self.assertEqual(to_list(l1), list1)

    @given(st.text(), st.text())
    def test_cons_text(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        list1 = [a, b]
        self.assertEqual(to_list(l1), list1)

    @given(st.none(), st.none())
    def test_cons_none(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        list1 = [a, b]
        self.assertEqual(to_list(l1), list1)

    @given(st.floats(), st.floats())
    def test_cons_floats(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        list1 = [a, b]
        self.assertEqual(to_list(l1), list1)

    def test_remove_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        l2 = cons(1, cons(None, emp))
        self.assertEqual(str(remove(l1, 1)), "[None]")
        self.assertEqual(str(remove(l2, 1)), "[None]")

    @given(st.text(), st.text())
    def test_remove_text(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        list1 = []
        if a != b:
            list1 = [a]
        self.assertEqual(to_list(remove(l1, b)), list1)

    @given(st.floats(), st.floats())
    def test_remove_text(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        list1 = []
        if a != b:
            list1 = [a]
        if math.isnan(a) and math.isnan(b):
            list1 = []
        self.assertEqual(to_list(remove(l1, b)), list1)

    def test_length_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        self.assertEqual(length(emp), 0)
        self.assertEqual(length(l1), 2)

    @given(st.floats(), st.floats())
    def test_length_floats(self, a, b):
        emp = DynamicArray()
        l1 = cons(b, cons(a, emp))
        self.assertEqual(length(emp), 0)
        self.assertEqual(length(l1), 2)

    @given(st.binary(), st.binary())
    def test_length_binary(self, a, b):
        emp = DynamicArray()
        l1 = cons(b, cons(a, emp))
        self.assertEqual(length(emp), 0)
        self.assertEqual(length(l1), 2)

    def test_isMember_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        self.assertFalse(isMember(emp, None))
        self.assertTrue(isMember(l1, None))
        self.assertTrue(isMember(l1, 1))
        self.assertFalse(isMember(l1, 2))

    @given(st.binary(), st.binary())
    def test_isMember_binary(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        self.assertFalse(isMember(emp, None))
        self.assertTrue(isMember(l1, b))
        self.assertTrue(isMember(l1, a))
        self.assertFalse(isMember(l1, None))

    def test_reverse_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        l2 = cons(1, cons(None, emp))
        self.assertEqual(l1, reverse(l2))

    @given(st.floats(), st.floats())
    def test_reverse_floats(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        l2 = cons(b, cons(a, emp))
        self.assertEqual(l1, reverse(l2))

    @given(st.text(), st.text())
    def test_reverse_text(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        l2 = cons(b, cons(a, emp))
        self.assertEqual(l1, reverse(l2))

    def test_tolist_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        self.assertEqual(to_list(l1), [None, 1])

    @given(st.floats(), st.floats())
    def test_tolist_floats(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        lst = [a, b]
        self.assertEqual(to_list(l1), lst)

    def test_fromlist_unittest(self):
        emp = DynamicArray()
        l1 = cons(None, cons(1, emp))
        self.assertEqual(l1, from_list([None, 1]))

    @given(st.floats(), st.floats())
    def test_fromlist_floats(self, a, b):
        emp = DynamicArray()
        l1 = cons(a, cons(b, emp))
        self.assertEqual(l1, from_list([a, b]))

    def test_find_unittest(self):
        emp = DynamicArray()
        l1 = cons(8, cons(4, cons(2, emp)))
        self.assertEqual(find(l1, lambda x: x % 2 == 0), [8, 4, 2])

    @given(st.integers(), st.integers(), st.integers())
    def test_find_integers(self, a, b, c):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        lst = []
        if a % 2 == 0:
            lst.append(a)
        if b % 2 == 0:
            lst.append(b)
        if c % 2 == 0:
            lst.append(c)
        self.assertEqual(find(l1, lambda x: x % 2 == 0), lst)

    def test_filter_the_value_unittest(self):
        emp = DynamicArray()
        l1 = cons(8, cons(3, cons(2, emp)))
        l2 = cons(8, cons(2, emp))
        self.assertEqual(filter_the_value(l1, lambda x: x % 2 == 0), l2)

    @given(st.integers(), st.integers(), st.integers())
    def test_filter_the_value_integers(self, a, b, c):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        l2 = DynamicArray()
        if c % 2 == 0:
            l2 = cons(c, l2)
        if b % 2 == 0:
            l2 = cons(b, l2)
        if a % 2 == 0:
            l2 = cons(a, l2)
        self.assertEqual(filter_the_value(l1, lambda x: x % 2 == 0), l2)

    def test_map_unittest(self):
        emp = DynamicArray()
        l1 = cons(8, cons(3, cons(2, emp)))
        l2 = cons(9, cons(4, cons(3, emp)))
        self.assertEqual(map_the_value(l1, lambda x: x + 1), l2)

    @given(st.integers(), st.integers(), st.integers())
    def test_map_integers(self, a, b, c):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        l2 = cons(a + 1, cons(b + 1, cons(c + 1, emp)))
        self.assertEqual(map_the_value(l1, lambda x: x + 1), l2)

    def test_reduce_unittest(self):
        emp = DynamicArray()
        l1 = cons(8, cons(3, cons(2, emp)))
        l2 = cons(10, cons(5, cons(4, emp)))

        self.assertEqual(reduce(l1, lambda x, state: x + 1 + state, 1), l2)

    @given(st.integers(), st.integers(), st.integers())
    def test_reduce_integers(self, a, b, c):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        initial_state = 1
        l2 = cons(a + 1 + initial_state, cons(b + 1 + initial_state, cons(c + 1 + initial_state, emp)))
        self.assertEqual(reduce(l1, lambda x, state: x + 1 + state, initial_state), l2)

    def test_iterator_unittest(self):
        emp = DynamicArray()
        l1 = cons(8, cons(3, cons(2, emp)))
        l2 = iterator_element(l1)
        self.assertEqual(next_element(l2), 8)
        self.assertEqual(next_element(l2), 3)
        self.assertEqual(next_element(l2), 2)

    @given(st.integers(), st.integers(), st.integers())
    def test_iterator_integers(self, a, b, c):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        l2 = iterator_element(l1)
        self.assertEqual(next_element(l2), a)
        self.assertEqual(next_element(l2), b)
        self.assertEqual(next_element(l2), c)

    def test_empty_unittest(self):
        emp = DynamicArray()
        l1 = cons(8, cons(3, cons(2, emp)))
        self.assertEqual(empty(l1), emp)

    @given(st.floats(), st.floats(), st.floats())
    def test_empty_unittest(self, a, b, c):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        self.assertEqual(empty(l1), emp)

    def test_concat_unittset(self):
        emp = DynamicArray()
        l1 = cons(8, cons(3, cons(2, emp)))
        l2 = cons(9, cons(4, cons(3, emp)))
        list1 = []
        list1.extend(to_list(l1))
        list2 = to_list(l2)
        list1.extend(list2)
        l3 = from_list(list1)
        self.assertEqual(concat(l1, l2), l3)

    @given(st.integers(), st.integers(), st.integers()
        , st.integers(), st.integers(), st.integers())
    def test_concat_integers(self, a, b, c, d, e, f):
        emp = DynamicArray()
        l1 = cons(a, cons(b, cons(c, emp)))
        l2 = cons(d, cons(e, cons(f, emp)))
        list1 = []
        list1.extend(to_list(l1))
        list2 = to_list(l2)
        list1.extend(list2)
        l3 = from_list(list1)
        self.assertEqual(concat(l1, l2), l3)
