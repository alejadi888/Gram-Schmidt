import numpy as np

np.set_printoptions(precision=4, suppress=True)

# INGRESAR VECTORES

cantidad = int(input("¿Cuántos vectores desea ingresar?: "))
dimension = int(input("¿Cuál es la dimensión de los vectores?: "))

vectores = []

for i in range(cantidad):

    print(f"\nIngrese el vector {i + 1}")

    componentes = []

    for j in range(dimension):
        valor = float(input(f"Componente {j + 1}: "))
        componentes.append(valor)

    vectores.append(np.array(componentes))

# GRAM-SCHMIDT

ortonormales = []
ortogonales = []

dependientes = []

for i, v in enumerate(vectores):

    u = v.copy()

    # Restar las proyecciones sobre los vectores anteriores
    for anterior in ortogonales:

        proyeccion = (
            np.dot(v, anterior) / np.dot(anterior, anterior)
        ) * anterior

        u = u - proyeccion

    # Comprobar si el vector resultante es cero
    magnitud = np.linalg.norm(u)

    if np.isclose(magnitud, 0):

        dependientes.append(i + 1)

    else:

        ortogonales.append(u)

        e = u / magnitud

        ortonormales.append(e)

# MOSTRAR RESULTADOS

print("\n")
print("           RESULTADOS")

for i in range(cantidad):

    print(f"\nVECTOR {i + 1}")
    print("Vector inicial:", vectores[i])

    if i + 1 in dependientes:

        print("Vector linealmente dependiente")
        print("No se puede normalizar.")

    else:

        # Buscar posición del vector en los ortonormales
        posicion = sum(1 for x in dependientes if x < i + 1)

        u = ortogonales[i - posicion]
        e = ortonormales[i - posicion]

        
        print("Magnitud:", f"{np.linalg.norm(u):.4f}")
        print("Vector ortonormalizado:", e)

# DETECCIÓN DE DEPENDENCIA

print("\n")
print("       DEPENDENCIA LINEAL")

if dependientes:

    print("Se encontraron vectores dependientes:")

    for numero in dependientes:
        print(f"   Vector {numero}")

else:

    print(" 3No se encontraron vectores dependientes.")

# VERIFICACIÓN

print("\n")
print("       VERIFICACIÓN ORTONORMAL")

todo_correcto = True

# Verificar magnitudes
for i, e in enumerate(ortonormales):

    norma = np.linalg.norm(e)

    if np.isclose(norma, 1):

        print(f"✓ ||e{i + 1}|| = 1")

    else:

        print(f"✗ ||e{i + 1}|| ≠ 1")
        todo_correcto = False


# Verificar productos punto
for i in range(len(ortonormales)):

    for j in range(i + 1, len(ortonormales)):

        producto = np.dot(ortonormales[i], ortonormales[j])

        if np.isclose(producto, 0):

            print(f"✓ e{i + 1} · e{j + 1} = 0")

        else:

            print(f"✗ e{i + 1} · e{j + 1} ≠ 0")
            todo_correcto = False


# Resultado final
print("\n------------------------------------------")

if todo_correcto:

    print("✓ Los vectores obtenidos son ortonormales.")

else:

    print("⚠️ Hay un problema con la ortonormalización.")