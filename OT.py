import streamlit as st
import numpy as np
import random

# Streamlit page setup
st.set_page_config(page_title="Assignment Problem Solver", layout="centered")
st.title("🚚 Assignment Problem using Genetic Algorithm")

# Step 1: Input matrix size
rows = st.number_input("🔢 Number of Agents (Rows)", min_value=2, max_value=10, value=4, step=1)
cols = st.number_input("🎯 Number of Tasks (Columns)", min_value=2, max_value=10, value=4, step=1)

# Step 2: Input cost matrix
st.subheader("📋 Enter Cost Matrix")
st.markdown("🔹 Enter space-separated values for each row (e.g. 9 2 7 8)")

matrix_input = []
valid_matrix = True

for i in range(rows):
    row_input = st.text_input(f"Row {i+1}", key=f"row_{i}")
    if row_input.strip():
        try:
            row_values = list(map(int, row_input.strip().split()))
            if len(row_values) != cols:
                valid_matrix = False
                st.warning(f"⚠ Row {i+1} must contain exactly {cols} values.")
            matrix_input.append(row_values)
        except:
            valid_matrix = False
            st.warning(f"❌ Invalid input in Row {i+1}. Please enter integers only.")
    else:
        valid_matrix = False

# Step 3: GA parameters
st.subheader("⚙ Genetic Algorithm Settings")
pop_size = st.slider("👥 Population Size", 10, 200, 50)
generations = st.slider("🔁 Number of Generations", 100, 1000, 300)
mutation_rate = st.slider("🧪 Mutation Rate", 0.0, 1.0, 0.1)

# Step 4: GA Functions
def create_population(size, n):
    return [random.sample(range(n), n) for _ in range(size)]

def calculate_cost(assignment, cost_matrix):
    return sum(cost_matrix[i][assignment[i]] for i in range(len(assignment)))

def selection(population, cost_matrix):
    return min(random.choices(population, k=5), key=lambda x: calculate_cost(x, cost_matrix))

def crossover(p1, p2):
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end+1] = p1[start:end+1]
    pointer = 0
    for gene in p2:
        if gene not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = gene
    return child

def mutate(path, rate):
    if random.random() < rate:
        i, j = random.sample(range(len(path)), 2)
        path[i], path[j] = path[j], path[i]
    return path

def evolve(population, cost_matrix, rate):
    new_pop = [min(population, key=lambda x: calculate_cost(x, cost_matrix))]  # Elitism
    while len(new_pop) < len(population):
        p1 = selection(population, cost_matrix)
        p2 = selection(population, cost_matrix)
        child = mutate(crossover(p1, p2), rate)
        new_pop.append(child)
    return new_pop

# Step 5: Run GA
if st.button("🚀 Optimize Assignment"):
    if rows != cols:
        st.error("⚠ This version only supports square matrices (same number of agents and tasks).")
    elif not valid_matrix or len(matrix_input) != rows:
        st.error("❌ Please complete the matrix with valid numeric input.")
    else:
        population = create_population(pop_size, rows)
        for _ in range(generations):
            population = evolve(population, matrix_input, mutation_rate)

        best_solution = min(population, key=lambda x: calculate_cost(x, matrix_input))
        best_cost = calculate_cost(best_solution, matrix_input)

        st.success("✅ Optimal Assignment Found!")
        for i, task in enumerate(best_solution):
            st.write(f"Agent {i+1} ➡️ Task {task+1} (Cost: {matrix_input[i][task]})")
        st.markdown(f"### 💰 Total Minimum Cost: `{best_cost}`")
