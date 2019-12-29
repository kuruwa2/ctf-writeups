import sys


class Random:
    seed = 0

    @staticmethod
    def srand(array):
        Random.seed = array[0]
        i = 1
        while Random.seed <= 0 and i < len(array):
            Random.seed = array[i]
            i += 1
        if Random.seed <= 0:
            Random.seed = (-1)*Random.seed + 1

    @staticmethod
    def rand(x, y):
        Random.seed += 1
        i = x + Random.seed % (y - x + 1)
        return i


def median(a, b, c):
    return a if (a <= b if a >= c else a >= b) else b if (b <= a if b >= c else b >= a) else c


def sort(a, lb, rb, d):
    if lb >= rb:
        return
    l = lb
    r = rb
    pivot = median(a[l], a[r], a[Random.rand(l, r)])
    while True:
        while a[l] < pivot:
            l += 1
        while a[r] > pivot:
            r -= 1
        if r <= l:
            break
        a[l] ^= a[r]
        a[r] ^= a[l]
        a[l] ^= a[r]
        l += 1
        r -= 1
    sort(a, lb, l - 1, d+1)
    sort(a, r + 1, rb, d+1)


def main():
    array = [i for i in range(100)]
    array[0] = 100
    if len(array) > sys.getrecursionlimit():
        print('\nSorry, can\'t sort arrays of such size :(')
        exit()
    Random.srand(array)
    try:
        sort(array, 0, len(array) - 1, 0)
    except RecursionError:
        print(open('./emergency_instructions.txt', 'r').read())
        exit()
    print('Sorted array:\n' + str(array))


if __name__ == "__main__":
    main()
