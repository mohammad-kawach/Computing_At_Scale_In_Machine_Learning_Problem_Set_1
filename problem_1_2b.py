import multiprocessing
import random
from math import pi
import time


def sample_pi(n):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of successes."""
    random.seed()
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1.0:
            s += 1
    return s


def parallel_sample_pi(steps_per_worker):
    return sample_pi(steps_per_worker)


def compute_pi(steps, num_workers):
    """ Return value should be the time measured for the execution """
    ### TODO: Add/change code below
    random.seed(1)
    steps_per_worker = steps // num_workers

    with multiprocessing.Pool(num_workers) as pool:
        start_time = time.time()
        results = pool.map(parallel_sample_pi, [steps_per_worker] * num_workers)
        end_time = time.time()

    s_total = sum(results)
    pi_est = (4.0 * s_total) / steps
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (steps, s_total, pi_est, pi - pi_est))

    ### TODO: Add/change code above
    measured_time = end_time - start_time
    return measured_time


if __name__ == "__main__":
    ### NOTE: The main clause will not be graded
    ### TODO: Add/change test case to your convenience
    num_workers_list = [1, 2, 4, 8]
    steps = 1000000
    times = []

    for num_workers in num_workers_list:
        measured_time = compute_pi(steps, num_workers)
        times.append(measured_time)

    print(f"Measured times for different worker counts: {times}")

    import matplotlib.pyplot as plt


    def plot_speedup(num_workers_list, times, serial_fraction):
        theoretical_speedup = [1 / (serial_fraction + (1 - serial_fraction) / n) for n in num_workers_list]
        measured_speedup = [times[0] / t for t in times]

        plt.figure(figsize=(10, 6))
        plt.plot(num_workers_list, theoretical_speedup, label='Theoretical Speedup', marker='o')
        plt.plot(num_workers_list, measured_speedup, label='Measured Speedup', marker='o')
        plt.xlabel('Number of Workers')
        plt.ylabel('Speedup')
        plt.title('Speedup of Monte Carlo Simulation for Pi Estimation')
        plt.legend()
        plt.grid(True)
        plt.show()


    serial_fraction = 1.0  # Adjust based on actual serial fraction measured
    plot_speedup(num_workers_list, times, serial_fraction)
