import time, math

def cal_factorial(number):
    start_time = time.time_ns()
    factorial_result = math.factorial(number)
    end_time = time.time_ns()
    print(f"{number}! calculated. Time taken: {end_time - start_time} ns")

def test_without_multithreading(round_number):
    print(f"\n--- Round {round_number} ---")
    start_all_time = time.time_ns()

    for number in [50, 100, 200]:
        cal_factorial(number)

    end_all_time = time.time_ns()
    total_time = end_all_time - start_all_time
    print(f"Total time for 3 factorials: {total_time} ns")
    return total_time

# Run 10 rounds and record results
overall_time = [test_without_multithreading(i + 1) for i in range(10)]
total_overall_time = sum(overall_time)
# Calculate average
average_time = sum(overall_time) / len(overall_time)

print("\n========== Summary (Without Multithreading) ==========")
print(f"Total accumulated time (10 rounds): {total_overall_time} ns")
print(f"\nAverage time (without multithreading): {average_time} ns")
