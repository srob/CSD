def generate(maxValue):
    if maxValue >= 2:
        s = maxValue + 1
        flags = [True] * s
        flags[0] = flags[1] = False
        for i in range(2, int(s**0.5) + 1):
            if flags[i]:
                for j in range(2 * i, s, i):
                    flags[j] = False  # not prime

        # count the number of primes
        count = sum(flags)
        primes = [0] * count
        # move the primes into the result
        j = 0
        for i in range(s):
            if flags[i]:
                primes[j] = i
                j += 1
        return primes
    else:
        return []

import unittest
class TestPrimes(unittest.TestCase):
    def test_up_to_1(self):
        self.assertEqual(generate(1), [])

    def test_up_to5(self):
        self.assertEquals(generate(5), [2, 3, 5])

    def test_up_to10(self):
        self.assertEquals(generate(10), [2,3,5,7])

if __name__ == '__main__':
    unittest.main()