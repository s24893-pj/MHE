import json
import random
from algoritms import *
import argparse

with open('problem.json', 'r') as f:
    data = json.load(f)

subset = data['set']
target = data['target']

parser = argparse.ArgumentParser(description='Projekt na zaliczenie MHE - subset_sum_problem')
parser.add_argument('algorithm_type', default='a', choices=['f_s', 'h_c', 'h_c_r', 'g1', 'g2', 'g3', 'g4',
                                                            'exp'],
                    help='Wybierz algorytm')
parser.add_argument('--population_size', type=int, default=10, help='Population size')
parser.add_argument('--max_gen', type=int, default=20, help='max generation')
parser.add_argument('--mutation_probability', type=float, default=0.01, help='mutation probability')
parser.add_argument('--max_no_imp', type=int, default=10, help='iterations')
parser.add_argument('--iterations', type=int, default=10, help='iterations')

first_cross = single_point_crossover
second_cross = two_point_crossover
first_mutation = simple_mutation
second_mutation = multi_mutation

args = parser.parse_args()

if args.algorithm_type == 'f_s':
    algorithm = full_search(subset, target)
    print(subset)
    print(target)
    print(algorithm)
elif args.algorithm_type == 'h_c':
    algorithm = solution_converter(hill_climbing(subset, target, args.iterations), subset)
    print(subset)
    print(target)
    print(algorithm)
elif args.algorithm_type == 'h_c_r':
    algorithm = solution_converter(hill_climbing_rng(subset, target, args.iterations), subset)
    print(subset)
    print(target)
    print(algorithm)
elif args.algorithm_type == 'g1':
    crossover = single_point_crossover
    mutation = simple_mutation
    algorithm = solution_converter(
        genetic_algorithm(subset, target, args.population_size, crossover, mutation, args.max_gen,
                          args.mutation_probability, args.max_no_imp), subset)
    print(subset)
    print(target)
    print(algorithm)
elif args.algorithm_type == 'g2':
    crossover = single_point_crossover
    mutation = multi_mutation
    algorithm = solution_converter(
        genetic_algorithm(subset, target, args.population_size, crossover, mutation, args.max_gen,
                          args.mutation_probability, args.max_no_imp), subset)
    print(subset)
    print(target)
    print(algorithm)
elif args.algorithm_type == 'g3':
    crossover = two_point_crossover
    mutation = simple_mutation
    algorithm = solution_converter(
        genetic_algorithm(subset, target, args.population_size, crossover, mutation, args.max_gen,
                          args.mutation_probability, args.max_no_imp), subset)
    print(subset)
    print(target)
    print(algorithm)
elif args.algorithm_type == 'g4':
    crossover = two_point_crossover
    mutation = multi_mutation
    algorithm = solution_converter(
        genetic_algorithm(subset, target, args.population_size, crossover, mutation, args.max_gen,
                          args.mutation_probability, args.max_no_imp), subset)
    print(subset)
    print(target)
    print(algorithm)

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
