from ex07_fizzbuzz_plus import fizzbuzz, fizzbuzz_run, times_table


def test_fizzbuzz_multiple_of_three():
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_multiple_of_five():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_multiple_of_fifteen():
    assert fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_plain_number():
    assert fizzbuzz(7) == "7"


def test_fizzbuzz_run_short():
    assert fizzbuzz_run(5) == "1, 2, Fizz, 4, Buzz"


def test_fizzbuzz_run_single():
    assert fizzbuzz_run(1) == "1"


def test_fizzbuzz_run_through_fizzbuzz():
    assert fizzbuzz_run(15).endswith("13, 14, FizzBuzz")


def test_times_table_three():
    assert times_table(3) == "1 2 3\n2 4 6\n3 6 9"


def test_times_table_one():
    assert times_table(1) == "1"


def test_times_table_two():
    assert times_table(2) == "1 2\n2 4"
