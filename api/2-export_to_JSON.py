#!/usr/bin/python3
"""using REST API to identify a given employee"""
import json
import requests
import sys


if __name__ == "__main__":
    """using REST API Placeholder through parameter"""
    parametro_id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/todos?userId={parametro_id}"
    url_nombre = f"https://jsonplaceholder.typicode.com/users/{parametro_id}"

    respuesta = requests.get(url)
    respuesta_nombre = requests.get(url_nombre)

    total_tarea = respuesta.json()
    inf_empleado = respuesta_nombre.json()
    formato_archivo = parametro_id + ".json"
    with open(formato_archivo, mode='w', newline="") as file:
        contenedor = []
        for tarea in total_tarea:
            formato = {
                    "task": "{}".format(tarea.get("title")),
                    "completed": "{}".format(tarea.get("completed")),
                    "username": "{}".format(inf_empleado.get("username"))
                    }
            contenedor.append(formato)
        dic_contenedor = {"{}".format(parametro_id): contenedor}
        json.dump(dic_contenedor, file)
