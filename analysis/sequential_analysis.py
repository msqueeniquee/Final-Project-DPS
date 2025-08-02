import time

# sorting data
def sort_data(data):
    sorted_data = sorted(data)
    return sorted_data

# filtering data with threshold = 500
def filter_data(data, threshold=500):
    filtered = []
    for d in data:
        if d > threshold:
            filtered.append(d)
    return filtered

# sorting without thread 
def sequential_sort(data):
    start = time.time()
    result = sort_data(data)
    end = time.time()
    print(f"[Sequential - Sorting] Execution Time: {end - start:.4f} seconds")
    return result

# filtering without thread
def sequential_filter(data):
    start = time.time()
    result = filter_data(data)
    end = time.time()
    print(f"[Sequential - Filtering] Execution Time: {end - start:.4f} seconds")
    return result
