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
    """Computes pi and prints results"""
    ### TODO: Add/change code below
    random.seed(1)

    # Measure serial section
    start_serial = time.time()

    n_total = steps
    s_total = sample_pi(n_total)

    end_serial = time.time()
    serial_time = end_serial - start_serial

    pi_est = (4.0 * s_total) / n_total
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi - pi_est))

    # Since the entire function is serial in this simple implementation,
    serial_fraction = 1.0  # All computation is serial

    ### TODO: Add/change code above
    return serial_fraction


if __name__ == "__main__":
    ### NOTE: The main clause will not be graded
    ### TODO: Add/change test case to your convenience
    steps = 1000

    serial_fraction = compute_pi(steps)
    print(f"Serial fraction of the computation: {serial_fraction}")
