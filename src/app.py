from model import Model
from view import View

model = Model()

if __name__ == "__main__":

    view = View()
    view.run()

    '''
    model = Model()
    model.load_data()
    model.normalize_images()
    model.build_and_compile_model()
    model.train_model(3)
    model.evaluate()
    model.save_model_in_file("C:/Users/simao/PycharmProjects/image-classification/resources/models/model.h5")
    model.recognize_image("C:/Users/simao/PycharmProjects/image-classification/resources/images/frog.jpg")
    '''