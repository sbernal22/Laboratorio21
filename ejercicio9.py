import asyncio
import time
import random
async def consulta_db(nombre, id_consulta):
    tiempo = random.randint(1, 5)
    print(f"Iniciando {nombre} - Consulta {id_consulta}")
    await asyncio.sleep(tiempo)
    print(f"Finalizó {nombre} - Consulta {id_consulta}")
consultas = [
    ("Consulta 1", 1),
    ("Consulta 2", 2),
    ("Consulta 3", 3)
]
async def main():
    inicio = time.time()
    await asyncio.gather(
        consulta_db("Consulta 1", 1),
        consulta_db("Consulta 2", 2),
        consulta_db("Consulta 3", 3)
    )
    print(f"Tiempo total: {time.time() - inicio:.2f} segundos")
asyncio.run(main())