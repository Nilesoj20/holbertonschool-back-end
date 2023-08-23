#!/usr/bin/python3
"""using REST API to identify a given employee"""

import requests
from sys import argv, exit


def inf_empleados():
    """using REST API Placeholder through parameter"""
    if len(argv) < 2:
        print("You must pass an ID parameter")
        exit()
    parametro_id = int(argv[1])

    url = f"https://jsonplaceholder.typicode.com/todos?userId={parametro_id}"
    url_nombre = f"https://jsonplaceholder.typicode.com/users/{parametro_id}"

    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        "deserializacion del archivo json optenido por el metodo get a la url"
        total_tarea = respuesta.json()
        if not total_tarea:
            print("error in deserialization")
            return
        tarea_completadas = []
        for tarea in total_tarea:
            if tarea["completed"]:
                tarea_completadas.append(tarea)
        cantidad_tarea_completada = len(tarea_completadas)
        cantidad_total_tarea = len(total_tarea)
    else:
        print("status error ")

    respuesta_nombre = requests.get(url_nombre)
    if respuesta_nombre.status_code == 200:
        informacion_empleado = respuesta_nombre.json()
        if "name" in informacion_empleado:
            nombre_empleado = informacion_empleado.get("name")
        print("Employee {} is done with tasks({}/{}):"
              .format(nombre_empleado,
                      cantidad_tarea_completada,
                      cantidad_total_tarea))

        for tarea in tarea_completadas:
            print("\t {}".format(tarea.get("title")))
    else:
        print("status error name")


if __name__ == '__main__':
    inf_empleados()
