import sys
import random
import utils

sys.path.append("../code/")

import num, sym, config, utils, cols, data

eg = {}
fails = 0


def test_the():
    print("-" * 50)
    return True, "PASS"


def test_sym():
    print("-" * 50)
    s = sym.Sym()
    for c in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(c)
    mode, entropy = s.mid(), s.div()
    entropy = (1000 * entropy) // 1 / 1000
    status = "PASS" if mode == "a" and 1.37 <= entropy and entropy <= 1.38 else "FAIL"
    return True, status


def test_num():
    print("-" * 50)
    n = num.Num(capacity=100)
    for i in range(1, 101):
        n.add(i)
    mid, div = n.mid(), n.div()
    status = "PASS" if 50 <= mid and mid <= 52 and 29 < div and div < 31 else "FAIL"
    return True, status


def test_bignum():
    print("-" * 50)
    n = num.Num(capacity=32)
    for i in range(1, 1001):
        n.add(i)
    status = "PASS" if len(n._has) == 32 else "FAIL"
    print(n.nums())
    return True, status


def runs(k):
    old_settings = config.settings
    if not eg[k]:
        return False
    status, message = eg[k]()
    if k == "LIST":
        message = "PASS"
    utils.print_result(message, k, status)
    config.settings = old_settings
    return status


def bad():
    print("-" * 50)
    try:
        print(eg["someting"]["that"]["doesn't"]["exist!"])
        return True, "PASS"
    except Exception as e:
        utils.dump_error(e)
        return False, "CRASH"


def all():
    global fails
    print("-" * 50)
    for k in list()[1]:
        if k != "ALL":
            if not runs(k):
                fails += 1
    return True, "PASS"


def list():
    return True, sorted(eg.keys())


def ls():
    print("\nExamples of python3 main.py -e...")
    for k in list()[1]:
        print(f"\t{k}")
    return True, "PASS"


def test_data():
    d = data.Data("../data/file.csv")
    for i, col in d.cols.x.items():
        print("COL", col)
    return True, "PASS"


def test_stats():
    d = data.Data("../data/file.csv")
    # div = cols.data()
    # mid = cols.mid()
    print(d.cols.all)
    print("xmid", d.stats( fun = "mid", places = 2 ))
    print("ymid", d.stats( fun = "mid", places = 2))
    print("xdiv", d.stats( fun = "div", places = 3))
    print("ydiv", d.stats( fun = "div", places = 3))
    return True, "PASS"


eg["BAD"] = bad
eg["ALL"] = all
eg["LIST"] = list
eg["LS"] = ls
eg["bignum"] = test_bignum
# eg["csv"] = test_csv
eg["data"] = test_data
eg["num"] = test_num
eg["stats"] = test_stats
eg["the"] = test_the
eg["sym"] = test_sym
fails = 0
