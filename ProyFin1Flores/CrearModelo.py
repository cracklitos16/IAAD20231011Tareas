from google.colab import drive
import os
import re
import numpy as np
import h5py
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Montar la unidad de Google Drive
drive.mount('/content/drive')

# Directorio en Google Drive donde están tus datos
drive_dir = '/content/drive/MyDrive/dataSetFlores/Train'

images = []
labels = []

# Tamaño al que se redimensionarán las imágenes
target_size = (200, 200)

# Recorrer las carpetas de entrenamiento
for class_folder in os.listdir(drive_dir):
    class_path = os.path.join(drive_dir, class_folder)

    if os.path.isdir(class_path):
        print(f"Leyendo imágenes de la carpeta de entrenamiento {class_folder}")

        for filename in os.listdir(class_path):
            if re.search(r"\.(jpg|jpeg|png|bmp|tiff)$", filename):
                filepath = os.path.join(class_path, filename)

                try:
                    # Redimensionar y cargar la imagen
                    image = load_img(filepath, target_size=target_size)
                    image_array = img_to_array(image)

                    images.append(image_array)
                    labels.append(class_folder)
                except Exception as e:
                    print(f"Error al procesar la imagen {filepath}: {str(e)}")

# Convertir a numpy array
images = np.array(images)
labels = np.array(labels)

# Convertir etiquetas a valores numéricos
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

# Dividir datos de entrenamiento en conjuntos de entrenamiento y validación
train_X, val_X, train_Y, val_Y = train_test_split(images, labels_encoded, test_size=0.2, random_state=42)

# Normalizar datos de imagen
train_X = train_X.astype('float32') / 255.0
val_X = val_X.astype('float32') / 255.0

# Convertir etiquetas a one-hot encoding
train_Y_one_hot = to_categorical(train_Y)
val_Y_one_hot = to_categorical(val_Y)

# Crear un archivo HDF5 para almacenar los datos
hdf5_file = h5py.File('/content/drive/MyDrive/dataSetFlores/data.h5', 'w')
hdf5_file.create_dataset('train_X', data=train_X)
hdf5_file.create_dataset('train_Y', data=train_Y_one_hot)
hdf5_file.create_dataset('val_X', data=val_X)
hdf5_file.create_dataset('val_Y', data=val_Y_one_hot)
hdf5_file.close()

# Construir el modelo
model = Sequential()
model.add(Conv2D(16, kernel_size=(3, 3), activation='relu', input_shape=(200, 200, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(np.unique(labels)), activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Aumento de datos
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

datagen.fit(train_X)

# Parada anticipada
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Entrenar el modelo
history = model.fit(datagen.flow(train_X, train_Y_one_hot, batch_size=64),
                    epochs=18,
                    validation_data=(val_X, val_Y_one_hot),
                    callbacks=[early_stop])

# Obtener precisión, recuperación y puntuación F1
precision, recall, f1, _ = precision_recall_fscore_support(np.argmax(val_Y_one_hot, axis=1),
                                                           np.argmax(model.predict(val_X), axis=1),
                                                           average='weighted')

print(f'Validation Precision: {precision:.4f}')
print(f'Validation Recall: {recall:.4f}')
print(f'Validation F1 Score: {f1:.4f}')

# Guardar el modelo en el archivo HDF5
model.save("/content/drive/MyDrive/dataSetFlores/modelFlores.h5")

# Obtener métricas adicionales
accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(accuracy))

# Plot de la precisión
plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
plt.plot(epochs, val_accuracy, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

# Plot de la pérdida
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
