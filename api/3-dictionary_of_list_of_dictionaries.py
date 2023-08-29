#!/usr/bin/python3
"""using REST API to identify a given employee"""
import json
import requests
import sys


if __name__ == "__main__":
    """using REST API Placeholder through parameter"""

    url_todos = f"https://jsonplaceholder.typicode.com/todos"
    url_usuario = f"https://jsonplaceholder.typicode.com/users"

    respuesta_todos = requests.get(url_todos)
    respuesta_usuario = requests.get(url_usuario)

    total_todos = respuesta_todos.json()
    total_usuarios = respuesta_usuario.json()
    formato_archivo = "todo_all_employees" + ".json"

    with open(formato_archivo, mode='w') as file:
        formato = {}
        for tarea in total_todos:
            id_usuario = tarea["userId"]
            nombre = next((u.get("username") for u in total_usuarios
                           if u["id"] == id_usuario), None)
            titulo = tarea["title"]
            estado = tarea["completed"]

            if id_usuario not in formato:
                formato[id_usuario] = []
            formato[id_usuario].append(
                    {
                        "username": nombre,
                        "task": titulo,
                        "completed": estado
                    }
            )
        json.dump(formato, file)
