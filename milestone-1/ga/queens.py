from json.encoder import INFINITY
import random


def start():
    pop = generate_population()
    for i in range(1_000):
        fit = []
        for j in range(len(pop)):
            fit.append(fitness(pop[j]))
        if min(fit) == 0:
            individual = pop[fit.index(min(fit))]
            return {
                "success": True,
                "iterations": i + 1,
                "individual": individual,
                "readable_indi": bit_decoder(individual),
                "fitness": min(fit),
            }
        mp = selection(pop, fit)
        new_pop = crossover(mp)
        pop = mutation(new_pop)
    individual = pop[fit.index(min(fit))]
    return {
        "success": False,
        "iterations": i + 1,
        "individual": individual,
        "readable_indi": bit_decoder(individual),
        "fitness": min(fit),
    }


def mutation(pop):
    p_mut = 0.01
    mutated_pop = pop.copy()
    for i in mutated_pop:
        for g in i:
            if random.random() <= p_mut:
                if g == 0:
                    g = 1
                if g == 1:
                    g = 0
    return mutated_pop


def crossover(mp):
    p_cross = 0.6
    new_pop = []
    while len(new_pop) < len(mp):
        g_a = random.randint(0, len(mp) - 1)
        while True:
            g_b = random.randint(0, len(mp) - 1)
            if g_b != g_a:
                break
        if random.random() < p_cross:
            crossover_point = random.randint(1, (len(mp[0]) - 2))
            old_g_a = mp[g_a].copy()
            old_g_b = mp[g_b].copy()
            new_g_a = old_g_a[0:crossover_point] + old_g_b[crossover_point : (len(mp[0]))]
            new_g_b = old_g_b[0:crossover_point] + old_g_a[crossover_point : (len(mp[0]))]
            new_pop.extend([new_g_a, new_g_b])
        else:
            new_pop.extend([mp[g_a], mp[g_b]])
    return new_pop


def selection(pop, fit):
    tournament_size = 3
    tournament_count = len(pop)
    matingpool = []
    for i in range(tournament_count):
        tournament = []
        for j in range(tournament_size):
            tournament.append(random.randint(0, len(pop) - 1))
        best_fit = INFINITY
        best_index = -1
        for k in range(tournament_size):
            if fit[tournament[k]] < best_fit:
                best_index = tournament[k]
        matingpool.append(pop[best_index])
    return matingpool


def generate_population(n=100):
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
    for q in range(len(decoded)):
        for x in range(len(decoded)):
            if x == q:
                continue
            if decoded[q] == decoded[x]:
                intersections += 1
    count = 0
    for i in range(len(decoded) - 1, -1, -1):
        for j in range(0, len(decoded) - i):
            if decoded[i + j] == j:
                count += 1
        for j in range(1, i):
            if decoded[i - j] == j:
                count += 1
        if count > 1:
            intersections += count
        count = 0

    return intersections


def bit_decoder(bits):
    result = []
    for i in range(0, len(bits), 3):
        result.append(bits[i] * 2**2 + bits[i + 1] * 2**1 + bits[i + 2] * 1)
    return result


print(start())
