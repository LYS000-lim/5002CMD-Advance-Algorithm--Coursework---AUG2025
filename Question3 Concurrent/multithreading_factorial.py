import time, threading, math

# Function to calculate the factorial of a given number
def cal_factorial(n):
    start_time = time.time_ns()
    factorial_result = math.factorial(n)
    end_time = time.time_ns()
    print(f"{n}! calculated. Time taken: {end_time - start_time} ns")

# Function to test factorial calculations using multithreading
def test_multithreading(round_number):
    print(f"\n--- Round {round_number} ---")
    start_all_time = time.time_ns()
    threads = []

    for n in [50, 100, 200]:
        t = threading.Thread(target=cal_factorial, args=(n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_all_time = time.time_ns()
    total_time = end_all_time - start_all_time
    print(f"Total time for 3 threads: {total_time} ns")
    return total_time

# Run 10 rounds and store total times
overall_time = [test_multithreading(i + 1) for i in range(10)]
total_overall_time = sum(overall_time)
# Calculate average
average_time = sum(overall_time) / len(overall_time)

print("\n========== Summary (With Multithreading) ==========")
print(f"Total accumulated time (10 rounds): {total_overall_time} ns")
print(f"\nAverage time (multithreading): {average_time} ns")
