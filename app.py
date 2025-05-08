
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

model = load_model(os.path.join(os.path.dirname('Model.hdf5')))
labels = ['label1', 'label2', 'label3']  # Replace with your actual class names

def predict_image(request):
    if request.method == 'POST' and request.FILES.get('img'):
        img = request.FILES['img']
        img_path = f'media/{img.name}'
        with open(img_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)

        img_obj = image.load_img(img_path, target_size=(128, 128))  
        img_arr = image.img_to_array(img_obj)
        img_arr = np.expand_dims(img_arr, axis=0) / 255.0

        pred = model.predict(img_arr)
        predicted_class = labels[np.argmax(pred)]

        return JsonResponse({'prediction': predicted_class})

    return render(request, 'index.html')

