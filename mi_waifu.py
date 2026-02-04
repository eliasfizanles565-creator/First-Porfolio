import subprocess
import datetime

def actualizar_repositorio():
    # Obtenemos la hora actual para el mensaje del commit
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje_commit = f"Actualización automática: {fecha_hora}"

    try:
        print("--- Iniciando actualización de GitHub ---")
        
        # 1. Agrega todos los cambios (git add .)
        subprocess.run(["git", "add", "."], check=True)
        print("[1/3] Cambios agregados correctamente.")

        # 2. Crea el commit con la fecha actual
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)
        print(f"[2/3] Commit creado: '{mensaje_commit}'")

        # 3. Sube los cambios a la nube (git push)
        subprocess.run(["git", "push"], check=True)
        print("[3/3] ¡Subida exitosa! Vercel comenzará a actualizarse ahora.")

    except subprocess.CalledProcessError as e:
        print(f"Error detectado: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    actualizar_repositorio()