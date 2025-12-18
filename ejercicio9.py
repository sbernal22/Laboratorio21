import multiprocessing
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
if __name__ == "__main__":
    inicio = time.time()
    procesos = []
    for nombre, id_c in consultas:
        p = multiprocessing.Process(target=consulta_db, args=(nombre, id_c))
        p.start()
        procesos.append(p)
    for p in procesos:
        p.join()
    print(f"\nTiempo total: {time.time() - inicio:.2f} segundos")