import random
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