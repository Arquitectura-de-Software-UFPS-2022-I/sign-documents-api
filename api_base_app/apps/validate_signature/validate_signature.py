import numpy as np
import tensorflow as tf
import os
from PIL import Image
from django.conf import settings
from tensorflow import keras
from keras.models import Sequential

class ClassifierSignature():
    model = keras.models.load_model(os.path.join(settings.BASE_DIR, 'model_saved.h5'))
    img_height = 300
    img_width = 300
    class_names = ['non-signature', 'signature']

    #Metodo para validación de firma, se tiene que copiar primero la imagen en la carpeta
    #'media/' y luego pasarle el nombre del archivo a este metodo (FUNCIONAL)
    def validate_image(self, file_name):
        img_dir = os.path.join(settings.MEDIA_ROOT, file_name)
        img = keras.utils.load_img(
            img_dir, target_size=(self.img_width, self.img_height)
        )
        print(type(img))
        img_array = keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        prediction = self.model.predict(img_array)
        score = tf.nn.softmax(prediction[0])

        os.remove(img_dir)


        return {"class_label": np.argmax(score), "confidence": 100 * np.max(score)}

