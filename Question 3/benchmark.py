# Implements multithreaded and sequential benchmark calculations across 10 rounds

import time
import threading
from fibonacci import fibonacci

# Target Fibonacci values specified by coursework brief
TARGET_NUMBERS = [35, 38, 40]

def run_single_thread(n: int, results_dict: dict, timestamps_dict: dict, thread_id: int):
    """
    Worker function executed inside individual threads.
    Records start time (t_start), computes Fib(n), records end time (t_end).
    """
    t_start = time.perf_counter_ns()
    res = fibonacci(n)
    t_end = time.perf_counter_ns()

    # Store results in synchronized dictionaries using thread_id as key
    results_dict[thread_id] = (n, res)
    timestamps_dict[thread_id] = (t_start, t_end)

def run_multithreaded_round() -> tuple[list[tuple[int, int]], int]:
    """
    Executes 1 round of Fib(35), Fib(38), and Fib(40) using 3 separate threads.

    Returns:
        results: list of tuples (n, fib_result)
        elapsed_nanoseconds: T = t2 - t1
        where:
            t1 = start time of thread that started FIRST
            t2 = end time of thread that finished LAST
    """
    results_dict = {}
    timestamps_dict = {}
    threads = []

    # 1. Create 3 separate threads (1 thread for each Fibonacci number)
    for i, num in enumerate(TARGET_NUMBERS):
        t = threading.Thread(
            target=run_single_thread,
            args=(num, results_dict, timestamps_dict, i)
        )
        threads.append(t)

    # 2. Start all threads sequentially
    for t in threads:
        t.start()

    # 3. Wait for all 3 threads to complete execution (join)
    for t in threads:
        t.join()

    # 4. Calculate overall elapsed time: T = t2 - t1
    # t1: earliest start time across all threads
    start_times = [timestamps_dict[i][0] for i in range(len(TARGET_NUMBERS))]
    # t2: latest end time across all threads
    end_times = [timestamps_dict[i][1] for i in range(len(TARGET_NUMBERS))]

    t1 = min(start_times)
    t2 = max(end_times)
    elapsed_nanoseconds = t2 - t1

    # Extract ordered results
    results = [results_dict[i] for i in range(len(TARGET_NUMBERS))]
    return results, elapsed_nanoseconds

def run_sequential_round() -> tuple[list[tuple[int, int]], int]:
    """
    Executes 1 round of Fib(35), Fib(38), and Fib(40) sequentially on a single thread.

    Returns:
        results: list of tuples (n, fib_result)
        elapsed_nanoseconds: total execution time in nanoseconds
    """
    results = []
    t1 = time.perf_counter_ns()

    for num in TARGET_NUMBERS:
        res = fibonacci(num)
        results.append((num, res))

    t2 = time.perf_counter_ns()
    elapsed_nanoseconds = t2 - t1

    return results, elapsed_nanoseconds

def benchmark_multithreaded(rounds: int = 10):
    """Runs 10 benchmark rounds using multithreading."""
    print("=== Fibonacci Computation (With Multithreading) ===")
    round_times = []

    for r in range(1, rounds + 1):
        results, t_ns = run_multithreaded_round()
        round_times.append(t_ns)

        # Format output string: Fib(35)-9227465, Fib(38)-39088169, Fib(40)-102334155 | T 1,532,847,210 ns
        res_str = ", ".join([f"Fib({n})-{val}" for n, val in results])
        print(f"Round {r:2d}: {res_str} | T {t_ns:,} ns")

    avg_time = sum(round_times) / rounds
    print(f"Average T (With Multithreading)   : {int(avg_time):,} ns\n")
    return avg_time

def benchmark_sequential(rounds: int = 10):
    """Runs 10 benchmark rounds without multithreading (Sequential)."""
    print("=== Fibonacci Computation (Without Multithreading) ===")
    round_times = []

    for r in range(1, rounds + 1):
        results, t_ns = run_sequential_round()
        round_times.append(t_ns)

        res_str = ", ".join([f"Fib({n})-{val}" for n, val in results])
        print(f"Round {r:2d}: {res_str} | T {t_ns:,} ns")

    avg_time = sum(round_times) / rounds
    print(f"Average T (Without Multithreading): {int(avg_time):,} ns\n")
    return avg_time