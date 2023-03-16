import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import cifar100


class Model:

    def __init__(self):
        pass

    def load_data(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = cifar100.load_data()

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
        self.test_loss, self.test_acc = self.model.evaluate(self.x_test,
                                                            self.y_test)
        print('Test accuracy:', self.test_acc)

    def save_model_in_file(self, location):
        self.model.save(location)
