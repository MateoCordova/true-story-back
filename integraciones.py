from models import Post

def report_to_google_maps(post: Post):
    # Aquí pondrías tu llamada a la API externa
    print(f"Enviando reporte a Google Maps: {post.title}, ubicación: {post.lat}, {post.lon}")
    # Simula latencia
    import time
    time.sleep(2)
    print("Reporte enviado")