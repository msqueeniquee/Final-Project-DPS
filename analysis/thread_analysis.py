import time
import threading
from threading import Lock
from analysis.sequential_analysis import sort_data, filter_data

def thread_sort(data, num_threads=4):
    start_time = time.time()
    size = len(data)
    chunk = size // num_threads
    data_parts = [data[i * chunk:(i + 1) * chunk] for i in range(num_threads)]

    results = []
    threads = []
    lock = Lock()

    def worker(part):
        sorted_part = sort_data(part)
        with lock:
            results.append(sorted_part)

    # run all threads
    for part in data_parts:
        t = threading.Thread(target=worker, args=(part,))
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

    # combine results
    final_result = []
    for r in results:
        final_result.extend(r)

    final_result.sort()

    end_time = time.time()
    print(f"[Threading - Sorting] Execution Time: {end_time - start_time:.4f} seconds")
    return final_result

def thread_filter(data, num_threads=4):
    start_time = time.time()
    size = len(data)
    chunk = size // num_threads
    data_parts = [data[i * chunk:(i + 1) * chunk] for i in range(num_threads)]

    results = []
    threads = []
    lock = Lock()

    def worker(part):
        filtered_part = filter_data(part)
        with lock:
            results.append(filtered_part)

    for part in data_parts:
        t = threading.Thread(target=worker, args=(part,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    final_result = []
    for r in results:
        final_result.extend(r)

    end_time = time.time()
    print(f"[Threading - Filtering] Execution Time: {end_time - start_time:.4f} seconds")
    return final_result
