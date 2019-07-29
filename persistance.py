import matplotlib.pyplot as plt
import random
from sympy.ntheory import factorint
import itertools

threads = 12
range_m = 100000000000000000
overall_high = 0
smallest = [0, 10, 25, 39, 77, 679, 6788, 68889, 2677889, 26888999, 3778888999, 277777788888899]


def per_score(n, steps=0, verbose=False):
    if verbose:
        print("n: " + str(n))
    if mod_size(n) == 1:
        # print("[*] Score: " + str(steps))
        return steps
    else:
        digits = [int(x) for x in str(n)]
        result = 1

        for digit in digits:
            result *= digit

        if verbose:
            return per_score(result, steps + 1, verbose=True)
        else:
            return per_score(result, steps + 1)


def mod_size(k):
    return len("%i" % k)


def check_range(m):
    current_high = -1
    for i in range(m):
        temp_score = per_score(i)
        if temp_score > current_high:
            print("[*] New Highscore is: " + str(temp_score) + ", with the number: " + str(i))
            current_high = temp_score
        elif i % 10000000000000 == 0:
            print("[+] Scanned " + str(i/m * 100) + "% of given number range")
        else:
            pass


def check_per(n, high=overall_high):
    temp_score = per_score(n)
    if temp_score > high:
        return temp_score
    else:
        pass


def list_per(iterations):
    listper = []
    list_val = []
    accuracy_steps = int(iterations / 100000)

    for i in range(1, iterations, accuracy_steps):
        rand_num = i + random.randint(0, accuracy_steps)
        listper.append(per_score(rand_num))
        list_val.append(rand_num)

    print(list_val[listper.index(max(listper))])
    plt.plot(listper)
    plt.show()


def prime_fac_smallest():
    for n in smallest:
        factors = factorint(n)
        print(factors)


def verbose_smallest():
    for n in smallest:
        per_score(n, verbose=True)
        print("---------------------")


def per_score_list(n):
    per_list = []
    per_list.append(n)
    while True:
        if len(str(n)) == 1:
            break

        n = persist_number(n)
        per_list.append(n)

    return per_list


def persist_number(n):
    digits = [int(x) for x in str(n)]
    result = 1

    for digit in digits:
        result *= digit

    return result


def return_parents(n):
    factor_dict = factorint(n)
    factors = []
    for i in factor_dict:
        factors.append(str(i))
    parents_iter = []
    for parent in itertools.permutations(factors):
        parents_iter.append(parent)
    parents = []
    for parent in parents_iter:
        result = ""
        for element in parent:
            result += element
        parents.append(int(result))
    return parents


if __name__ == '__main__':
    per_27777 = per_score_list(277777788888899)
    for n in per_27777:
        print(n)
        print(factorint(n))
        print("----------------")
    # print(per_score_list(3778888999))
    # print(per_score_list(26888999))

    # print(factorint(277777788888899))
    # print(return_parents(277777788888899))
