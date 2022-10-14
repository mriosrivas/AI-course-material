import numpy as np
import json
import os


def preprocess_data(path, saved_folder):
    try:
        os.makedirs(path+'/'+saved_folder)
    except Exception as e:
        print(e)
        print(f'Use another name for {saved_folder} folder in {path}')

    #file = 'circular.39ke6uvj.ingestion-5989f6cf-mws8t.json'
    files = os.listdir(path)

    for file in files:
        if file.endswith(".json"):
            with open(path + '/' + file) as json_file:
                data = json.load(json_file)

            data_dict = {"sampling_freq": 62.5, "draw_graphs": True, "axes": ["x", "y", "z"], "implementation_version": 1,
                         "params": {
                             "scale_axes": 1,
                             "filter_type": "low",
                             "filter_cutoff": 3,
                             "filter_order": 6,
                             "fft_length": 128,
                             "spectral_peaks_count": 3,
                             "spectral_peaks_threshold": 0.1,
                             "spectral_power_edges": [0.1, 0.5, 1.0, 2.0, 5.0],
                             "do_log": False,
                             "do_fft_overlap": True
                         }, 'features': list(np.array(data['payload']['values']).flatten()),
                         "label" : file.split('.')[0]}

            # print(f'data_dict size = {len(data_dict["features"])}')

            with open(path + '/' + saved_folder + '/' + file[:-5] + '_api_call.json', 'w') as dump_file:
                json.dump(data_dict, dump_file)


if __name__ == "__main__":
    path_training = '../data/training'
    path_testing = '../data/testing'
    saved_folder = 'api_call'

    preprocess_data(path_training, saved_folder)
    preprocess_data(path_testing, saved_folder)
