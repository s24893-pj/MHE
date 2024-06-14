import random
from algoritms import *

subset = [3, 3, 5, 6, 8, 11, 12]
target = 20


def solution_converter(solution, subset):
    converted_solution = []
    for i in range(len(subset)):
        if solution[i]:
            converted_solution.append(subset[i])

    return converted_solution


# solution = random_solution(subset)
# neighbourhood = get_neighbourhood(solution)
# print(f"sol = {solution}, neighbourhood = {neighbourhood} ")
# print(full_search(subset, target))
# genetic = solution_converter(genetic_algorithm(subset, target, 5, two_point_crossover, multi_mutation, 5,
#                                                0.01, 50), subset)
#
# print(f'genetic: {genetic}')
# # test = [random_solution(subset) for _ in range(150)]
#
# # # print(test)
# #
# # print(evaluate(test, subset, target))
# # print(min(evaluate(test, subset, target)))