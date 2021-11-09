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
