import matplotlib.pyplot as plt
from tabulate import tabulate

def show_table(results):
    sizes = results['sizes']
    print("\n===== EXECUTION TIME TABLE (seconds) =====")

    sorting_table = []
    filtering_table = []

    for i, size in enumerate(sizes):
        sorting_table.append([
            f"{size}%",
            results['Sorting']['Sequential'][i],
            results['Sorting']['Threading'][i],
            results['Sorting']['Multiprocessing'][i]
        ])
        filtering_table.append([
            f"{size}%",
            results['Filtering']['Sequential'][i],
            results['Filtering']['Threading'][i],
            results['Filtering']['Multiprocessing'][i]
        ])

    print("\n--- Sorting ---")
    print(tabulate(sorting_table, headers=["Size", "Sequential", "Threading", "Multiprocessing"], tablefmt="grid"))
    print("\n--- Filtering ---")
    print(tabulate(filtering_table, headers=["Size", "Sequential", "Threading", "Multiprocessing"], tablefmt="grid"))

def show_graph(results):
    sizes = results['sizes']

    # Sorting
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, results['Sorting']['Sequential'], marker='o', label='Sequential')
    plt.plot(sizes, results['Sorting']['Threading'], marker='o', label='Threading')
    plt.plot(sizes, results['Sorting']['Multiprocessing'], marker='o', label='Multiprocessing')
    plt.title("Execution Time Comparison - Sorting")
    plt.xlabel("Dataset Size (%)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Filtering
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, results['Filtering']['Sequential'], marker='o', label='Sequential')
    plt.plot(sizes, results['Filtering']['Threading'], marker='o', label='Threading')
    plt.plot(sizes, results['Filtering']['Multiprocessing'], marker='o', label='Multiprocessing')
    plt.title("Execution Time Comparison - Filtering")
    plt.xlabel("Dataset Size (%)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
