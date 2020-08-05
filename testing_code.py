

results = (('Morganne', 50), ('Florida', 48))


def show_results(results):
    print(f"RESULTS: LINE 10: {results}")
    if not isinstance(results, tuple):
        return
    for i, result in enumerate(results):
        print(f"{i}. {result[0]}, {result[1]}")


show_results(results)