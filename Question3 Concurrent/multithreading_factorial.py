import time, threading, math

def cal_factorial(number):
    start_time = time.time_ns()
    factorial_result = math.factorial(number)
    end_time = time.time_ns()
    print(f"{number}! calculated. Time taken: {end_time - start_time} ns")

def test_multithreading():
    start_all_time = time.time_ns()
    thread = []

    for n in [50, 100, 200]:
        t = threading.Thread(target=cal_factorial, args=(n,))
        thread.append(t)
        t.start()

    for t in thread:
        t.join()

    end_all_time = time.time_ns()
    total_time = end_all_time - start_all_time
    print(f"\nTotal time for 3 threads: {total_time} ns")
    return total_time

overall_time = [test_multithreading() for num in range(10)]
average_time = sum(overall_time) / len(overall_time)
print(f"\nAverage time (multithreading): {average_time} ns")
