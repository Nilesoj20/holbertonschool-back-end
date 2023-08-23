#!/usr/bin/python3
"""Export data in CSV format"""
import csv
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

    formato_archivo = f"{parametro_id}.csv"
    with open(formato_archivo, mode='w', newline="") as file:
        formato = ["USER_ID",
                   "USERNAME",
                   "TASK_COMPLETED_STATUS",
                   "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=formato)

        for task in total_tarea:
            writer.writerow({
                "USER_ID": f'{parametro_id}',
                "USERNAME": f'{informacion_empleado.get("username")}',
                "TASK_COMPLETED_STATUS": f'{task.get("completed")}',
                "TASK_TITLE": f'{task.get("title")}'
            })
