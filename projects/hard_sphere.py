# """ Problem 8.58, molecular dynamics simulation of liquid argon. This is a simplified simulation of
# around 20 particles in one dimension. This can be extended to 2 or 3 dimensions if there is enough
# time. This doesn’t appear to use the more advanced later material in chapter 8, but rather the
# velocity verlet algorithm which, in fact, use the first year physics kinematics equations combined
# with larger scale calculations for the force due to many particles."""

# import numpy as np
# import matplotlib.pyplot as plt

# N = 20
# sigma = 1.0
# epsilon = 1.0
# mass = 1.0
# dt = 0.001
# steps = 5000

# a = 2**(1/6) * sigma
# L = a * N
# x = np.linspace(0, L, N, endpoint=False)

# np.random.seed(0)
# v = np.random.randn(N)
# v -= np.mean(v)

# def apply_pbc(x):
#     return x % L

# def minimum_image(dx):
#     dx -= L * np.round(dx / L)
#     return dx

# def compute_forces(x):
#     forces = np.zeros(N)
#     potential_energy = 0.0
#     for i in range(N):
#         for j in range(i + 1, N):
#             dx = x[i] - x[j]
#             dx = minimum_image(dx)
#             r = np.abs(dx)
#             if r < 1e-6:
#                 continue
#             if r < 3.0 * sigma:
#                 inv_r = sigma / r
#                 inv_r6 = inv_r**6
#                 inv_r12 = inv_r6**2
#                 force_mag = 24 * epsilon * (2 * inv_r12 - inv_r6) / r
#                 force = force_mag * (dx / r)
#                 forces[i] += force
#                 forces[j] -= force
#                 potential_energy += 4 * epsilon * (inv_r12 - inv_r6)
#     return forces, potential_energy

# positions_history = []
# kinetic_energy_history = []
# potential_energy_history = []

# forces, potential_energy = compute_forces(x)

# for step in range(steps):
#     x += v * dt + 0.5 * forces / mass * dt**2
#     x = apply_pbc(x)
#     new_forces, potential_energy = compute_forces(x)
#     v += 0.5 * (forces + new_forces) / mass * dt
#     forces = new_forces
#     kinetic_energy = 0.5 * mass * np.sum(v**2)
#     positions_history.append(x.copy())
#     kinetic_energy_history.append(kinetic_energy)
#     potential_energy_history.append(potential_energy)

# total_energy = np.array(kinetic_energy_history) + np.array(potential_energy_history)

# plt.figure()
# plt.plot(total_energy)
# plt.title("Total Energy vs Time")
# plt.xlabel("Time step")
# plt.ylabel("Energy")
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

N = 20
sigma = 1.0
epsilon = 1.0
mass = 1.0
dt = 0.001
steps = 5000

a = 2**(1/6) * sigma
L = a * N
x = np.linspace(0, L, N, endpoint=False)

np.random.seed(0)
v = np.random.randn(N)
v -= np.mean(v)

def apply_pbc(x):
    return x % L

def minimum_image(dx):
    dx -= L * np.round(dx / L)
    return dx

def compute_forces(x):
    forces = np.zeros(N)
    potential_energy = 0.0
    for i in range(N):
        for j in range(N):
            if i != j:
                dx = minimum_image(x[i] - x[j])
                r = np.abs(dx)
                if r < 1e-6:
                    continue
                term = 48 * epsilon * ((sigma / r)**12 - 0.5 * (sigma / r)**6) / (r**2)
                forces[i] -= term * dx
                potential_energy += 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6) * 0.5
    return forces, potential_energy

forces, potential_energy = compute_forces(x)

kinetic_energy_history = []
potential_energy_history = []

for step in range(steps):
    x = x + dt * v + (dt**2) * forces / (2 * mass)
    x = apply_pbc(x)
    new_forces, potential_energy = compute_forces(x)
    v = v + dt * (forces + new_forces) / (2 * mass)
    forces = new_forces
    kinetic_energy = 0.5 * mass * np.sum(v**2)
    kinetic_energy_history.append(kinetic_energy)
    potential_energy_history.append(potential_energy)

total_energy = np.array(kinetic_energy_history) + np.array(potential_energy_history)

plt.figure()
plt.plot(total_energy)
plt.xlabel("Time step")
plt.ylabel("Total Energy")
plt.title("Total Energy vs Time")
plt.show()

# fjsdfsdafjdds
# f



import numpy as np
import matplotlib.pyplot as plt

N = 20
sigma = 1.0
epsilon = 1.0
mass = 1.0
dt = 0.001
burn_in_steps = 1500
production_steps = 3500
total_steps = burn_in_steps + production_steps

target_temperature = 1.0

a = 2**(1/6) * sigma
L = a * N
x = np.linspace(0, L, N, endpoint=False)

np.random.seed(0)
v = np.random.randn(N)
v -= np.mean(v)

def apply_pbc(x):
    return x % L

def minimum_image(dx):
    dx -= L * np.round(dx / L)
    return dx

def compute_forces(x):
    forces = np.zeros(N)
    potential_energy = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            dx = minimum_image(x[i] - x[j])
            r = np.abs(dx)
            if r < 1e-12:
                continue
            inv_r = sigma / r
            inv_r6 = inv_r**6
            inv_r12 = inv_r6**2
            force_scalar = 48 * epsilon * (inv_r12 - 0.5 * inv_r6) / (r**2)
            f = force_scalar * dx
            forces[i] += f
            forces[j] -= f
            potential_energy += 4 * epsilon * (inv_r12 - inv_r6)
    return forces, potential_energy

def rescale_velocities(v):
    kinetic = 0.5 * mass * np.sum(v**2)
    current_temp = (2.0 * kinetic) / N
    scale = np.sqrt(target_temperature / current_temp)
    return v * scale

forces, potential_energy = compute_forces(x)

kinetic_energy_history = []
potential_energy_history = []
total_energy_history = []

for step in range(total_steps):
    x = x + dt * v + (dt**2) * forces / (2 * mass)
    x = apply_pbc(x)
    new_forces, potential_energy = compute_forces(x)
    v = v + dt * (forces + new_forces) / (2 * mass)
    forces = new_forces

    if step < burn_in_steps and step % 10 == 0:
        v = rescale_velocities(v)

    kinetic_energy = 0.5 * mass * np.sum(v**2)
    total_energy = kinetic_energy + potential_energy

    kinetic_energy_history.append(kinetic_energy)
    potential_energy_history.append(potential_energy)
    total_energy_history.append(total_energy)

plt.figure()
plt.plot(kinetic_energy_history, label="Kinetic Energy")
plt.plot(potential_energy_history, label="Potential Energy")
plt.plot(total_energy_history, label="Total Energy")
plt.xlabel("Time step")
plt.ylabel("Energy")
plt.legend()
plt.show()