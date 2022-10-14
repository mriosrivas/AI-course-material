import requests
import json

url = 'http://localhost:4446/run'

data_dict = {"sampling_freq": 62.5, "draw_graphs": True, "axes": ["x", "y", "z"], "implementation_version": 2,
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
                         }, 'features': [-1, 0.4, 11.5]
             }

response = requests.post(url, json=data_dict)
result = response.json()

values = result['features']
print(values)