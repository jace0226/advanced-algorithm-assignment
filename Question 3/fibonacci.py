# Handles the recursive calculation of the nth Fibonacci number.

def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using naive recursion.

    Time Complexity: O(2^N) - Exponential
    Space Complexity: O(N) - Recursion stack depth

    Mathematical Definition:
        Fib(0) = 0
        Fib(1) = 1
        Fib(n) = Fib(n-1) + Fib(n-2) for n > 1
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case: call fibonacci for (n-1) and (n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_with_op_count(n: int) -> tuple[int, int]:
    """
    Calculates the nth Fibonacci number and counts total primitive operations.
    Returns tuple: (result, operation_count)
    """
    op_count = [0]  # Use list to mutate count inside inner recursive function

    def _fib(k: int) -> int:
        op_count[0] += 1  # Operation count: base case evaluation / comparison
        if k <= 0:
            return 0
        if k == 1:
            return 1

        op_count[0] += 1  # Operation count: addition operator (+)
        return _fib(k - 1) + _fib(k - 2)

    result = _fib(n)
    return result, op_count[0]