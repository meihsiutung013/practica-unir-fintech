# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas más.

---

## Ejecución

Este proyecto requiere **Docker** para ejecutarse en cualquier sistema operativo.

Puedes ejecutar el programa de la siguiente manera:

### En Linux y macOS

```bash
docker run --rm --volume "$(pwd)":/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes asc
```

### En Windows (PowerShell)

```powershell
docker run --rm --volume ${PWD}:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes asc
```

---

## Parámetros

```bash
python3 main.py <filename> <dup> <order>
```

- `filename`: **ruta** al fichero que contiene la lista de palabras, una por línea.
- `dup`: **yes** para eliminar palabras duplicadas, o **no** para mantener la lista tal cual.
- `order`: **asc** para ordenar las palabras de manera ascendente, o **desc** para ordenar las palabras de manera descendente.

> **Notas:**
> - El archivo `words.txt` debe estar en el mismo directorio desde donde ejecutes el comando.
> - El contenedor de Docker montará tu carpeta local y ejecutará `main.py` dentro de Python 3.6.

---
