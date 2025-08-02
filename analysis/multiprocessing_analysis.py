import time
from multiprocessing import Pool
from analysis.sequential_analysis import sort_data, filter_data

# sorting using multiprocessing with pool
def multiprocessing_sort(data, num_processes=4):
    start = time.time()
    chunk = len(data) // num_processes
    parts = []

    for i in range(num_processes):
        part = data[i * chunk:(i + 1) * chunk]
        parts.append(part)

    with Pool(num_processes) as pool:
        result_parts = pool.map(sort_data, parts)

    final = []
    for r in result_parts:
        final.extend(r)
    final.sort()

    end = time.time()
    print(f"[Multiprocessing - Sorting] Execution Time: {end - start:.4f} seconds")
    return final

# filtering using multiprocessing with pool
def multiprocessing_filter(data, num_processes=4):
    start = time.time()
    chunk = len(data) // num_processes
    parts = []

    for i in range(num_processes):
        part = data[i * chunk:(i + 1) * chunk]
        parts.append(part)

    with Pool(num_processes) as pool:
        result_parts = pool.map(filter_data, parts)

    final = []
    for r in result_parts:
        final.extend(r)

    end = time.time()
    print(f"[Multiprocessing - Filtering] Execution Time: {end - start:.4f} seconds")
    return final
