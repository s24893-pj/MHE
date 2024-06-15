import random
from optimization import *


def generate_all_subsets(subset: list) -> list:
    all_subsets = []
    for i in range(1 << len(subset)):
        current_subset = [subset[j] for j in range(len(subset)) if (i & (1 << j))]
        all_subsets.append(current_subset)
    return all_subsets


def full_search(subset: list, target: int) -> list:
    all_subsets = generate_all_subsets(subset)
    best_solution = []
    best_value = float('inf')

    for current_subset in all_subsets:
        current_value = goal_function(current_subset, target)
        if current_value < best_value:
            best_value = current_value
            best_solution = current_subset

    return best_solution


# random.random()


def single_point_crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2


def two_point_crossover(p1, p2):
    point = random.randint(1, len(p1) - 2)
    point2 = random.randint(point + 1, len(p1) - 1)
    c1 = p1[:point] + p2[point:point2] + p1[point2:]
    c2 = p2[:point] + p1[point:point2] + p2[point2:]
    return c1, c2


def simple_mutation(solution: list, mutation_probability=0.01) -> list:
    for i in range(len(solution)):
        if random.random() < mutation_probability:
            solution[i] = not solution[i]
    return solution


def multi_mutation(solution: list, mutation_probability=0.01) -> list:
    number = random.randint(1, len(solution))
    indexes = random.sample(range(len(solution)), number)
    if random.random() < mutation_probability:
        for i in indexes:
            solution[i] = not solution[i]
    return solution


def perfect_result_stop(fit) -> bool:
    return fit == 0


def no_improvement_stop(counter: int, max: int) -> bool:
    return counter >= max


def evaluate(population, subset, target) -> list:
    return [goal_function(solution_converter(individual, subset), target) for individual in population]


def select_parents(population: list, fit):
    parents = random.choices(population, weights=[1 / f for f in fit], k=2)
    return parents[0], parents[1]


def genetic_algorithm(subset, target, population_size, cross_method, mutation_method, max_gen, mutation_probability,
                      max_without_improvement):
    population = [random_solution(subset) for _ in range(population_size)]
    best_sol = None
    best_fit = float('inf')
    no_improvement = 0

    for gen in range(max_gen):
        fit = evaluate(population, subset, target)

        if min(fit) < best_fit:
            best_fit = min(fit)
            best_sol = population[fit.index(best_fit)]
            no_improvement = 0
        else:
            no_improvement += 1

        if perfect_result_stop(best_fit) or no_improvement_stop(no_improvement, max_without_improvement):
            break

        new_population = []
        while len(new_population) < population_size:
            p1, p2 = select_parents(population, fit)
            c1, c2 = cross_method(p1, p2)
            c1 = mutation_method(c1, mutation_probability)
            c2 = mutation_method(c2, mutation_probability)
            new_population.extend([c1, c2])

        population = new_population[:population_size]

    return best_sol


def hill_climbing(subset, target, iterations):
    current_sol = random_solution(subset)
    current_val = goal_function(solution_converter(current_sol, subset), target)

    for _ in range(iterations):
        neighbourhood = get_neighbourhood(current_sol)
        new_sol = best_neighbour(subset, neighbourhood, target)
        new_val = goal_function(solution_converter(new_sol, subset), target)
        if  new_val >= current_val:
            return current_sol
        else:
            current_sol = new_sol
            current_val = goal_function(solution_converter(current_sol, subset), target)

    return current_sol

def hill_climbing_rng(subset, target, iterations):
    current_sol = random_solution(subset)
    current_val = goal_function(solution_converter(current_sol, subset), target)

    for _ in range(iterations):
        neighbourhood = get_neighbourhood(current_sol)
        rng_neighbour = random.choice(neighbourhood)
        neigh_val = goal_function(solution_converter(rng_neighbour, subset), target)

        if neigh_val < current_val:
            current_sol = rng_neighbour
            current_val = neigh_val

    return current_sol



