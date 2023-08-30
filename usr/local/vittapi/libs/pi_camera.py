import io
import base64
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time
import os
import shutil
os.environ["LIBCAMERA_LOG_LEVELS"] = "3"


class Camera(object):
    def __init__(self, mode=1):
        self.camera = Picamera2()
        self.camera.set_logging(Picamera2.ERROR)
        self.camera_config = self.camera.create_preview_configuration({"size": (640, 480)}, raw=self.camera.sensor_modes[mode])
        self.camera.configure(self.camera_config)
        #self.video_config = self.camera.create_video_configuration()
        #self.encoder = H264Encoder(bitrate=10000000)
        # self.camera.start_preview(Preview.DRM)

    def get_frame(self):
        self.camera.start()
        time.sleep(2)
        
        # Enregistrez l'image dans le répertoire temporaire
        temp_filename = "temp_image.jpg"
        self.camera.capture_file(temp_filename)
        
        self.camera.stop()
        time.sleep(2)

        # Définir le chemin du répertoire et du fichier de destination
        filename = "image.jpg"
        #local
        #dirpath = '/home/pi/Desktop/vittapi/usr/local/vittapi/app/static/images/'
        #server
        dirpath = "/usr/local/vittapi/app/static/images/"
        # Créer le répertoire s'il n'existe pas
       

        destpath = os.path.join(dirpath, filename)

        # Copier l'image dans le répertoire de destination
        try:
            shutil.copy(temp_filename, destpath)
            print(f"Copié avec succès de {temp_filename} à {destpath}")
        except Exception as e:
            print(f"Impossible de copier le fichier. Erreur: {e}")

        # Supprimer l'image temporaire si nécessaire
        os.remove(temp_filename)

        print("IMAGE_CAPTURED_SUCCESSFULLY")
        return "IMAGE_CAPTURED_SUCCESSFULLY"

    def get_record(self, duration=5):
        self.camera.start_and_record_video('temp_video.mp4', duration=duration)
        

        time.sleep(2)

        # Enregistrez la vidéo dans le répertoire temporaire
        temp_filename = "temp_video.mp4"

        # Définir le chemin du répertoire et du fichier de destination
        filename = "video.mp4"
        #local
        #dirpath = '/home/pi/Desktop/vittapi/usr/local/vittapi/app/static/videos/'
        #server
        dirpath = "/usr/local/vittapi/app/static/videos/"

        

        destpath = os.path.join(dirpath, filename)

        # Copier la vidéo dans le répertoire de destination
        try:
            shutil.copy(temp_filename, destpath)
            print(f"Copié avec succès de {temp_filename} à {destpath}")
        except Exception as e:
            print(f"Impossible de copier le fichier. Erreur: {e}")

        # Supprimer la vidéo temporaire si nécessaire
        os.remove(temp_filename)


        print("VIDEO_CAPTURED_SUCCESSFULLY")
        return "VIDEO_CAPTURED_SUCCESSFULLY"