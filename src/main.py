from model import Model


if __name__ == "__main__":

    model = Model()
    model.load_data()
    model.normalize_images()
    model.build_and_compile_model()
    model.train_model(3)
    model.evaluate()
    model.save_model_in_file()
