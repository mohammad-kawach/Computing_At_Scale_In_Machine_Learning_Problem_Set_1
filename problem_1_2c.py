import multiprocessing  # See https://docs.python.org/3/library/multiprocessing.html
import random
from math import pi
import time

def sample_pi(n, seed):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of successes."""
    ### TODO: Add/change code below
    random.seed(seed)  # Use the provided seed for reproducibility
    ### TODO: Add/change code above
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s

def parallel_sample_pi(args):
    steps_per_worker, seed = args
    return sample_pi(steps_per_worker, seed)

def compute_pi(steps, num_workers, seed):
    """ Return value should be the time measured for the execution """
    ### TODO: Add/change code below
    random.seed(seed)
    steps_per_worker = steps // num_workers
    
    # Use different seeds for each worker to ensure repeatability
    seeds = [seed + i for i in range(num_workers)]
    
    with multiprocessing.Pool(num_workers) as pool:
        start_time = time.time()
        results = pool.map(parallel_sample_pi, [(steps_per_worker, seed) for seed in seeds])
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
    steps = 1000
    num_workers = 2
    seed = 1
    measured_time = compute_pi(steps, num_workers, seed)
    print(f"Measured time: {measured_time}")
