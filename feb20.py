import time

try:
    import numpy as np
except ImportError:
    raise SystemExit("NumPy is required to run this script.")

N = 1_000_000

if __name__ == "__main__":
    # Measure list creation time
    t0 = time.perf_counter()
    py_list = list(range(N))
    t1 = time.perf_counter()
    list_create = t1 - t0

    # Measure NumPy array creation time
    t0 = time.perf_counter()
    np_array = np.arange(N, dtype=np.int64)
    t1 = time.perf_counter()
    array_create = t1 - t0

    # Measure sum operation on Python list
    t0 = time.perf_counter()
    list_sum = sum(py_list)
    t1 = time.perf_counter()
    list_sum_time = t1 - t0

    # Measure sum operation on NumPy array
    t0 = time.perf_counter()
    array_sum = np_array.sum()
    t1 = time.perf_counter()
    array_sum_time = t1 - t0

    # Measure scalar multiplication on Python list
    t0 = time.perf_counter()
    list_mul = [x * 2 for x in py_list]
    t1 = time.perf_counter()
    list_mul_time = t1 - t0

    # Measure scalar multiplication on NumPy array
    t0 = time.perf_counter()
    array_mul = np_array * 2
    t1 = time.perf_counter()
    array_mul_time = t1 - t0

    print(f"List creation time: {list_create:.6f} seconds")
    print(f"NumPy array creation time: {array_create:.6f} seconds")
    print(f"Python list sum time: {list_sum_time:.6f} seconds")
    print(f"NumPy array sum time: {array_sum_time:.6f} seconds")
    print(f"Python list scalar multiplication time: {list_mul_time:.6f} seconds")
    print(f"NumPy array scalar multiplication time: {array_mul_time:.6f} seconds")
    print()
    print("Observations:")
    print("1. NumPy array operations are much faster for large numerical data, especially for reduction and vectorized arithmetic.")
    print("2. Python lists are slower for element-wise numeric operations because they use Python-level loops and boxed objects.")
    print("3. NumPy array creation can be faster or comparable to list creation, and arrays use contiguous memory for efficient computation.")
