import unittest


def classify_number(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return str(numero)


def list_fizzbuzz_range(limite):
    listFizzBuzz = []
    for numero in range(1, limite + 1):
        listFizzBuzz.append(classify_number(numero))
    return listFizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(classify_number(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(classify_number(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(classify_number(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(classify_number(7), "7")

    def test_list_fizzbuzz_range(self):
        self.assertEqual(list_fizzbuzz_range(5), ["1", "2", "Fizz", "4", "Buzz"])


if __name__ == "__main__":
    unittest.main()