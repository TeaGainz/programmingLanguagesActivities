def count_even_odd(start, max_num, interval):
    even_count = 0
    odd_count = 0
    series = []

    for num in range(start, max_num, interval):
        series.append(num)
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return series, even_count, odd_count

def main():
    start = int(input("Enter start number: "))
    max_num = int(input("Enter a max number: "))
    interval = int(input("Enter the interval between numbers: "))

    series, even_count, odd_count = count_even_odd(start, max_num, interval)

    print("\nSeries numbers =", ' '.join(map(str, series)))
    print(f"\nNumber of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")

if __name__ == "__main__":
    main()