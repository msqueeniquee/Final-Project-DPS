import pandas as pd
import time

from analysis.sequential_analysis import sequential_sort, sequential_filter
from analysis.thread_analysis import thread_sort, thread_filter
from analysis.multiprocessing_analysis import multiprocessing_sort, multiprocessing_filter
from visualization.visualize_results import show_table, show_graph

# data trip_duration taken from nyc_taxi_trip_duration.csv
trip_duration = []

def run_tests():
    results = {
        "sizes": [25, 50, 75, 100],
        "Sorting": {"Sequential": [], "Threading": [], "Multiprocessing": []},
        "Filtering": {"Sequential": [], "Threading": [], "Multiprocessing": []}
    }

    percentages = [0.25, 0.5, 0.75, 1.0]

    for p in percentages:
        size = int(len(trip_duration) * p)
        sample = trip_duration[:size]
        print(f"\n===== Dataset Size: {int(p*100)}% ({size} rows) =====")

        # Sorting
        start = time.time()
        sequential_sort(sample)
        results["Sorting"]["Sequential"].append(round(time.time() - start, 4))

        start = time.time()
        thread_sort(sample)
        results["Sorting"]["Threading"].append(round(time.time() - start, 4))

        start = time.time()
        multiprocessing_sort(sample)
        results["Sorting"]["Multiprocessing"].append(round(time.time() - start, 4))

        # Filtering
        start = time.time()
        sequential_filter(sample)
        results["Filtering"]["Sequential"].append(round(time.time() - start, 4))

        start = time.time()
        thread_filter(sample)
        results["Filtering"]["Threading"].append(round(time.time() - start, 4))

        start = time.time()
        multiprocessing_filter(sample)
        results["Filtering"]["Multiprocessing"].append(round(time.time() - start, 4))

    show_table(results)
    show_graph(results)


if __name__ == "__main__":
    df = pd.read_csv("data/train.csv", usecols=["trip_duration"])
    trip_duration = df["trip_duration"].tolist()
    print(f"Total Records: {len(trip_duration)} rows")
    run_tests()
