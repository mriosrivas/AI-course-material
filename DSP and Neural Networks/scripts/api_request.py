import requests
import json
import os
import pandas as pd


def api_request(path, saved_folder, url, csv_name):
    files = os.listdir(path + '/' + saved_folder)

    data_values = []

    for file in files:
        if file.endswith('.json'):
            with open(path + '/' + saved_folder + '/' + file) as json_file:
                data = json.load(json_file)

            response = requests.post(url, json=data)
            result = response.json()

            values = result['features']
            values.append(data['label'])
            data_values.append(values)

        df = pd.DataFrame(data_values)

    df.rename(columns=dict(zip(df.columns.values, list(3*result['labels'] + ['features']))), inplace=True)
    df.to_csv(csv_name)
    #df.columns(list(result['labels']))


if __name__ == "__main__":
    path_training = 'data/training'
    path_testing = 'data/testing'
    saved_folder = 'api_call'
    url = 'http://localhost:4446/run'
    csv_training_name = '../data/training_data.csv'
    csv_testing_name = '../data/testing_data.csv'

    api_request(path_training, saved_folder, url, csv_training_name)
    api_request(path_testing, saved_folder, url, csv_testing_name)
