#!/usr/bin/python3
"""using REST API to identify a given employee"""

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
    informacion_empleado = respuesta_nombre.json()
    nombre_empleado = informacion_empleado.get("name")

    tarea_completadas = []
    for tarea in total_tarea:
        if tarea["completed"]:
            tarea_completadas.append(tarea)
    cantidad_tarea_completada = len(tarea_completadas)
    cantidad_total_tarea = len(total_tarea)

    print("Employee {} is done with tasks({}/{}):"
          .format(nombre_empleado,
                  cantidad_tarea_completada,
                  cantidad_total_tarea))

    for tarea in tarea_completadas:
        print("\t {}".format(tarea.get("title")))
