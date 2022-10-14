from preprocess_data import preprocess_data
from api_request import api_request

def run():
    path_training = '../data/training'
    path_testing = '../data/testing'
    saved_folder = 'api_call'
    url = 'http://localhost:4446/run'
    csv_training_name = '../data/training_data.csv'
    csv_testing_name = '../data/testing_data.csv'

    preprocess_data(path_training, saved_folder)
    preprocess_data(path_testing, saved_folder)
    api_request(path_training, saved_folder, url, csv_training_name)
    api_request(path_testing, saved_folder, url, csv_testing_name)
    return


if __name__ == "__main__":
    run()
