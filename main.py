import random
from algoritms import full_search


def goal_function(subset: list, target: int) -> int:
    return abs(sum(subset) - target)


def random_solution(subset: list) -> list:
    random_sol = []
    for _ in subset:
        random_sol.append(random.choice([True, False]))
    return random_sol


def get_neighbourhood(solution: list) -> list:
    neighbourhood = []
    i = random.randint(0, len(solution) - 1)
    for j, x in enumerate(solution):
        if j == i:
            neighbourhood.append(not x)
        else:
            neighbourhood.append(x)
    return neighbourhood


subset = [3, 3, 5, 6, 8, 11, 12]
target = 10

solution = random_solution(subset)
neighbourhood = get_neighbourhood(solution)
print(f"sol = {solution}, neighbourhood = {neighbourhood} ")
print(full_search(goal_function, subset, target))
