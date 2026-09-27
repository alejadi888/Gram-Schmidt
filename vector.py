import numpy as np

np.set_printoptions(precision=4, suppress=True)

print("Ingrese los componentes del vector 1:")
ve1 = np.array([
    float(input("x = ")),
    float(input("y = ")),
    float(input("z = "))
])

print("\nIngrese los componentes del vector 2:")
ve2 = np.array([
    float(input("x = ")),
    float(input("y = ")),
    float(input("z = "))
])

print("\nIngrese los componentes del vector 3:")
ve3 = np.array([
    float(input("x = ")),
    float(input("y = ")),
    float(input("z = "))
])

u1 = ve1
magnitud_u1 = np.linalg.norm(u1)
v1 = u1 / magnitud_u1 

proy_21 = (np.dot(ve2, u1) / np.dot(u1, u1)) * u1
v2 = ve2 - proy_21
magnitud_u2 = np.linalg.norm(v2)
e2 = v2 / magnitud_u2

proy_31 = (np.dot(ve3, u1) / np.dot(u1, u1)) * u1
proy_32 = (np.dot(ve3, v2) / np.dot(v2, v2)) * v2
v3 = ve3 - proy_31 - proy_32
magnitud_u3 = np.linalg.norm(v3)
e3 = v3 / magnitud_u3

print("\n========== RESULTADOS ==========")

print("\nVECTOR 1")
print("Vector inicial:", ve1)
print("Magnitud:", f"{magnitud_u1:.4f}")
print("Vector ortonormalizado:", v1)

print("\nVECTOR 2")
print("Vector inicial:", ve2)
print("Magnitud:", f"{magnitud_u2:.4f}")
print("Vector ortonormalizado:", v2)

print("\nVECTOR 3")
print("Vector inicial:", ve3)
print("Magnitud:", f"{magnitud_u3:.4f}")
print("Vector ortonormalizado:", v3)