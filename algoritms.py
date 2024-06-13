def generate_all_subsets(subset: list) -> list:
    all_subsets = []
    for i in range(1 << len(subset)):
        current_subset = [subset[j] for j in range(len(subset)) if (i & (1 << j))]
        all_subsets.append(current_subset)
    return all_subsets


def full_search(goal_function, subset: list, target: int) -> list:
    all_subsets = generate_all_subsets(subset)
    best_solution = []
    best_value = float('inf')

    for current_subset in all_subsets:
        current_value = goal_function(current_subset, target)
        if current_value < best_value:
            best_value = current_value
            best_solution = current_subset

    return best_solution
