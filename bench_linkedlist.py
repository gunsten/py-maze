import time
import timeit
import random
from linkedlist import cons, empty_list


def append_to_list(smpl):
    ls = list()
    for e in smpl:
        ls.append(e)
    return ls

def cons_to_list(smpl):
    ls = empty_list()
    for e in smpl:
        ls = cons(e, ls)
    return ls

for exp in range(0, 7):
    sample_length: int = 10 ** exp
    print("Benching for sample of length {}".format(sample_length))
    smpl = random.sample(range(0, 2 ** 63 - 1), sample_length)

    print("Append: ")
    before = time.time()
    append_to_list(smpl)
    app_time = time.time() - before
    print(app_time)
    #print(timeit.timeit("append_to_list(smpl)", setup="from __main__ import append_to_list, smpl"))

    print("Cons: ")
    before = time.time()
    cons_to_list(smpl)
    cons_time = time.time() - before
    print(cons_time)
    print("Diff (s):  {}".format(int(app_time-cons_time)))
    print("Diff (ms): {}".format(int((app_time - cons_time)*1000)))
    print("Diff (us): {}".format(int((app_time - cons_time) * 1000000)))
    #print(timeit.timeit("cons_to_list(smpl)", setup="from __main__ import cons_to_list, smpl"))

    print("Pop from array:")
    arr = smpl.copy()
    before = time.time()
    while len(arr) > 0:
        arr.pop()
    arr_pop_time = time.time() - before
    print(arr_pop_time)

    print("Unhead from linkedlist:")
    ls = cons_to_list(smpl)
    before = time.time()
    while not ls.is_empty:
        ls = ls.tail
    unhead_time = time.time() - before
    print(unhead_time)

    print("Diff (s):  {}".format(int(arr_pop_time - unhead_time)))
    print("Diff (ms): {}".format(int((arr_pop_time - unhead_time) * 1000)))
    print("Diff (us): {}".format(int((arr_pop_time - unhead_time) * 1000000)))
