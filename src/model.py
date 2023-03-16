from rating import Rating
from tensorflow import keras
from keras.datasets import cifar10
from PIL import Image
import numpy as np


class Model:\

    def __init__(self):
        self.classes_names = {
            0: "airplane",
            1: "automobile",
            2: "bird",
            3: "cat",
            4: "deer",
            5: "dog",
            6: "frog",
            7: "horse",
            8: "ship",
            9: "truck"
        }

    def load_data(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = cifar10.load_data()

    def define_classes(self, classes):
        self.classes = classes

    def normalize_images(self):
        self.x_train = self.x_train.astype("float32") / 255.0
        self.x_test = self.x_test.astype("float32") / 255.0

    def build_and_compile_model(self):
        self.model = keras.models.Sequential([
            keras.layers.Conv2D(32, (3, 3),
                                activation='relu',
                                input_shape=(32, 32, 3)),

            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(128, (3, 3), activation='relu'),
            keras.layers.Flatten(),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(100, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def train_model(self, epochs):
        self.model.fit(self.x_train, self.y_train,
                       epochs=epochs,
                       validation_data=(self.x_test, self.y_test))

    def evaluate(self):
        self.lost, self.accuracy = self.model.evaluate(self.x_test, self.y_test)

        if Rating.EXCELENT.value.__getitem__(0) <= self.accuracy <= Rating.EXCELENT.value.__getitem__(1):
            print("Seu modelo de aprendizagem é excelente.")
        elif Rating.VERY_GOOD.value.__getitem__(0) <= self.accuracy <= Rating.VERY_GOOD.value.__getitem__(1):
            print("Seu modelo de aprendizagem é muito bom.")
        elif Rating.GOOD.value.__getitem__(0) <= self.accuracy <= Rating.GOOD.value.__getitem__(1):
            print("Seu modelo de aprendizagem é bom.")
        elif Rating.NORMAL.value.__getitem__(0) <= self.accuracy <= Rating.NORMAL.value.__getitem__(1):
            print("Seu modelo de aprendizagem é normal.")
        elif Rating.BAD.value.__getitem__(0) <= self.accuracy <= Rating.BAD.value.__getitem__(1):
            print("Seu modelo de aprendizagem é mau.")
        elif Rating.TERRIBLE.value.__getitem__(0) <= self.accuracy <= Rating.TERRIBLE.value.__getitem__(1):
            print("Seu modelo de aprendizagem é terrível.")

    def save_model_in_file(self, location):
        self.model.save(location)

    def recognize_image(self, location):
        image = Image.open(location)
        image = image.resize((32, 32))

        img_array = np.array(image)
        img_array = img_array.astype("float32") / 255.0

        img_array = np.expand_dims(img_array, axis=0)

        prediction = self.model.predict(img_array)

        predicted_class = np.argmax(prediction)

        predicted_class_name = self.classes_names[predicted_class]

        print(predicted_class_name)
