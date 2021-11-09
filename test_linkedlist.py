import unittest, random
from linkedlist import cons, empty_list

sample_length = 100


class TestLinkedList(unittest.TestCase):
    def test_sample_ints_preserved(self):
        arr = random.sample(range(0, 2 ** 63 - 1), sample_length)
        ll = empty_list()
        for i in range(sample_length - 1, -1, -1):
            ll = cons(arr[i], ll)
        arr_iter = iter(arr)
        for e in ll:
            self.assertEqual(next(arr_iter), e)

    def test_empty_list(self):
        ep = empty_list()
        self.assertFalse(ep.has_tail)
        self.assertTrue(ep.is_empty)
        self.assertEqual([], ep.to_list())

    def test_cons(self):
        ep = empty_list()
        self.assertEqual(42, cons(42, ep).head)
        self.assertTrue(cons(37, ep).tail.is_empty)
        self.assertFalse(cons(98, ep).is_empty)
        self.assertEqual([42], cons(42, ep).to_list())
        self.assertEqual(None, cons(None, ep).head)
        self.assertTrue(cons(None, ep).tail.is_empty)
        self.assertFalse(cons(None, ep).is_empty)
        self.assertEqual([None], cons(None, ep).to_list())

    def test_eq_id(self):
        a_list = empty_list()
        self.assertTrue(a_list == a_list)
        a_list = cons(5, a_list)
        self.assertTrue(a_list == a_list)
        a_list = cons(23, a_list)
        self.assertTrue(a_list == a_list)
        self.assertTrue(cons(311, a_list).tail == cons(272, a_list).tail)

    def test_eq_empty(self):
        self.assertEqual(empty_list(), empty_list())

    def test_eq(self):
        self.assertEqual(cons(1, empty_list()), cons(1, empty_list()))
        ep = empty_list()
        self.assertEqual(cons(2, ep), cons(2, ep))

    def test_eq_random_sample(self):
        l1, l2 = empty_list(), empty_list()

        for e in random.sample(range(0, 2 ** 63 - 1), sample_length):
            l1, l2 = cons(e, l1), cons(e, l2)
        self.assertEqual(l1, l2)
        self.assertEqual(cons(None, l1), cons(None, l2))
        self.assertEqual(cons(True, l1), cons(True, l2))
