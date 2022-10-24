from json.encoder import INFINITY
import random


def start():
    pop = generate_population()
    for i in range(1):
        fit = []
        for j in range(len(pop)):
            fit.append(fitness(pop[j]))
        mp = selection(pop, fit)
        crossover(mp)


def crossover(mp):
    p_cross = 0.6
    children = []
    for i in range(len(mp)):
        if random.random() < p_cross:
            print("cross")
        else:
            print("no cross")


def selection(pop, fit):
    tournament_size = 3
    tournament_count = len(pop)
    matinpool = []
    for i in range(tournament_count):
        tournament = []
        for j in range(tournament_size):
            tournament.append(random.randint(0, len(pop) - 1))
        best_fit = INFINITY
        best_index = -1
        for k in range(tournament_size):
            if fit[tournament[k]] < best_fit:
                best_index = tournament[k]
        matinpool.append(pop[best_index])
    return matinpool


def generate_population(n=10):
    population = []
    for i in range(n):
        individual = []
        for i in range(3 * 8):
            individual.append(random.randint(0, 1))
        population.append(individual)
    return population


def fitness(pop):
    decoded = bit_decoder(pop)
    intersections = 0
    for y in range(8):
        queen_count = 0
        for x in range(8):
            if decoded[x] == y:
                queen_count += 1
        if queen_count > 1:
            intersections += queen_count - 1
    # for x in range(8, 1, -1):
    #     queen_count = 0
    #     for y in range(1, 8 - x):
    #         for d in range(0, y):
    #             if decoded[x + d] == y:
    #                 queen_count += 1
    #         if queen_count > 1:
    #             intersections += queen_count - 1

    return intersections


def bit_decoder(bits):
    result = []
    for i in range(0, len(bits), 3):
        result.append(bits[i] * 2**2 + bits[i + 1] * 2**1 + bits[i + 2] * 1)
    return result


start()
