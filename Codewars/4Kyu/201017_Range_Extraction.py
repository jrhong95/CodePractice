import unittest


def solution(args):
    numlist, tmp = [], []
    for n in args:
        if tmp == []:
            tmp.append(n)
        else:
            if tmp[-1] == n - 1:
                tmp.append(n)
            else:
                if len(tmp) != 2:
                    numlist.append(tmp)
                else:
                    for num in tmp:
                        numlist.append([num])
                tmp = [n]
    if len(tmp) != 2:
        numlist.append(tmp)
    else:
        for num in tmp:
            numlist.append([num])
    return ",".join(str(nums[0]) if len(nums) == 1 else f"{nums[0]}-{nums[-1]}" for nums in numlist)


class Test_Solution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')


if __name__ == '__main__':
    unittest.main()