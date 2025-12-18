import threading
import time
import random
def consulta_db(nombre, id_consulta):
    tiempo = random.randint(1, 5)
    print(f"Iniciando {nombre} - Consulta {id_consulta}")
    time.sleep(tiempo)
    print(f"Finalizó {nombre} - Consulta {id_consulta}")
consultas = [
    ("Consulta 1", 1),
    ("Consulta 2", 2),
    ("Consulta 3", 3)
]
inicio = time.time()
hilos = []
for nombre, id_c in consultas:
    h = threading.Thread(target=consulta_db, args=(nombre, id_c))
    h.start()
    hilos.append(h)
for h in hilos:
    h.join()
print(f"Tiempo total: {time.time() - inicio:.2f} segundos")