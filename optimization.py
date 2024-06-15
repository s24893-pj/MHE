import random


def goal_function(subset: list, target: int) -> int:
    return abs(sum(subset) - target)


def goal_function_for_genetic(problem: list, subset: list, target: int) -> int:
    return sum(problem) - abs(sum(subset) - target)


def random_solution(subset: list) -> list:
    random_sol = []
    for _ in subset:
        random_sol.append(random.choice([True, False]))
    return random_sol


def random_neighbour(solution: list) -> list:
    neighbourhood = []
    i = random.randint(0, len(solution) - 1)
    for j, x in enumerate(solution):
        if j == i:
            neighbourhood.append(not x)
        else:
            neighbourhood.append(x)
    return neighbourhood


def get_neighbourhood(solution: list) -> list:
    neighbourhood = []
    for i, x in enumerate(solution):
        neighbour = solution.copy()
        neighbour[i] = not x
        neighbourhood.append(neighbour)
    return neighbourhood


def solution_converter(solution, subset):
    converted_solution = []
    for i in range(len(subset)):
        if solution[i]:
            converted_solution.append(subset[i])

    return converted_solution


def best_neighbour(subset: list, neighbourhood: list, target: int) -> list:
    best_val = float('inf')
    best_neigh = None
    for neighbour in neighbourhood:
        neighbour_value = goal_function(solution_converter(neighbour, subset), target)
        if neighbour_value < best_val:
            best_neigh = neighbour
            best_val = neighbour_value

    return best_neigh
