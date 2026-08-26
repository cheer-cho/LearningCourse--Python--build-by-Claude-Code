import sys


def run(argv):
    if not argv:
        print("error: provide at least one number")
        return 1

    numbers = []
    for raw in argv:
        try:
            numbers.append(float(raw))
        except ValueError:
            print(f"error: invalid number: {raw}")
            return 1

    count = len(numbers)
    total = sum(numbers)
    average = total / count

    print(f"count: {count}")
    print(f"total: {total}")
    print(f"average: {average}")
    return 0


def main():
    sys.exit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
