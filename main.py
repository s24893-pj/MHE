import json
import random
from algoritms import *
import argparse

with open('problem.json', 'r') as f:
    data = json.load(f)

subset = data['set']
target = data['target']

parser = argparse.ArgumentParser(description='Projekt na zaliczenie MHE - subset_sum_problem')
parser.add_argument('Algoritm type', choices=['f_s', 'h_c', 'h_c_r', 'g1', 'g2', 'g3', 'g4'], help='Wybierz algorytm')
parser.add_argument('--population_size')
parser.add_argument('--max_gen')
parser.add_argument('--mutation_probability')

population_size
cross_method
mutation_method
max_gen
mutation_probability

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
