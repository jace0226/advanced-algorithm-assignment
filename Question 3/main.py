# Runs 10-round benchmarks for both Multithreaded and Sequential approaches.

from benchmark import benchmark_multithreaded, benchmark_sequential
from fibonacci import fibonacci_with_op_count

def main():

    # Step 1: Demonstrate Primitive Operation Count for Big-O Analysis
    print("--- 1. Primitive Operation Count Demonstration ---")
    for test_n in [5, 10, 15]:
        val, ops = fibonacci_with_op_count(test_n)
        print(f"Fib({test_n:2d}) = {val:<8d} | Operations counted: {ops}")
    print()

    # Step 2: Perform 10-round Benchmark (With Multithreading)
    avg_multi = benchmark_multithreaded(rounds=10)

    # Step 3: Perform 10-round Benchmark (Without Multithreading)
    avg_seq = benchmark_sequential(rounds=10)

    # Step 4: Summary Comparison & Observation Output
    diff = avg_seq - avg_multi
    percentage = (diff / avg_seq) * 100

    print("=== Performance Comparison Summary ===")
    print(f"Average Sequential Time   : {int(avg_seq):,} ns")
    print(f"Average Multithreaded Time : {int(avg_multi):,} ns")

    if percentage > 0:
        print(f"Observation: Multithreading reduced execution time by approximately {percentage:.2f}%.")
    else:
        print(f"Observation: Multithreading did NOT reduce execution time due to Python's GIL (Global Interpreter Lock).")

if __name__ == "__main__":
    main()