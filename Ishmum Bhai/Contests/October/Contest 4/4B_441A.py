from typing import List


def solution(n: int, a: int, b: int, list1: List[int], list2: List[int]):

    res = [2] * n

    for i in a:
        res[i - 1] = 1

    print(*res)


def take_input():
    n, a, b = map(int, input().split())

    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    solution(n, a, b, list1, list2)


take_input()
