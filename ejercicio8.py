import json

equipos = [
    {
        "Nombre": "Equipo1",
        "pais": "Pais1",
        "nivelAtaque": 95,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Equipo2",
        "pais": "Pais2",
        "nivelAtaque": 93,
        "nivelDefensa": 90
    },
    {
        "Nombre": "Equipo3",
        "pais": "Pais3",
        "nivelAtaque": 91,
        "nivelDefensa": 87
    }
]

json_equipos = json.dumps(equipos, indent=4)
print(json_equipos)
