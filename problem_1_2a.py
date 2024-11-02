import random
from math import pi
import time

def sample_pi(n):
    """Perform n steps of Monte Carlo simulation for estimating Pi/4.
    Returns the number of successes."""
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s

def compute_pi(steps):
    """Computes pi and prints results with detailed timing analysis"""
    # Start timing initialization (serial)
    init_start = time.perf_counter()
    random.seed(1)
    n_total = steps
    init_end = time.perf_counter()
    init_time = init_end - init_start

    # Time the Monte Carlo calculation (potentially parallel)
    calc_start = time.perf_counter()
    s_total = sample_pi(n_total)
    calc_end = time.perf_counter()
    calc_time = calc_end - calc_start

    # Time the final calculations and output (serial)
    final_start = time.perf_counter()
    pi_est = (4.0 * s_total) / n_total
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi - pi_est))
    final_end = time.perf_counter()
    final_time = final_end - final_start

    # Calculate total and serial times
    total_time = init_time + calc_time + final_time
    serial_time = init_time + final_time
    serial_fraction = serial_time / total_time

    # Print timing analysis
    print("\nTiming Analysis:")
    print(f"Initialization time (serial): {init_time:.6f} seconds")
    print(f"Calculation time (parallel): {calc_time:.6f} seconds")
    print(f"Final computation time (serial): {final_time:.6f} seconds")
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Serial time: {serial_time:.6f} seconds")
    print(f"Serial fraction: {serial_fraction:.6f}")

    return serial_fraction

if __name__ == "__main__":
    steps = 10000000  # Using a larger number for more accurate timing
    serial_fraction = compute_pi(steps)