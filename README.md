# Reproductor de música con FastAPI
Esta es una API de reproductor de música construida con FastAPI y Python.

# USO
Clona este repositorio:
git clone https://github.com/Lifimastar/Reproducir_1_cancion.git

## Instala las dependencias:
```
pip install fastapi
pip install uvicorn
pip install pygame
```
## Inicia la aplicación:
```
uvicorn main:app --reload
```
* Haz una petición POST a http://localhost:8000/upload/ para subir un archivo mp3, puedes usar POSTMAN para insertar la URL y en Body -> Form -> Files, agregar el archivo mp3 y escribes "files"
* Haz una petición POST a http://localhost:8000/play/ para reproducir la cancion.
* Haz una petición POST a http://localhost:8000/stop/ para detener la reproducion.

# Contribución
Siéntete libre de enviar solicitudes de extracción para agregar nuevas características, solucionar errores o mejorar la documentación.

# Licencia
Este proyecto está bajo la Licencia MIT.
