import numpy as np
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

x_arr = np.arange(-2.6,2.6,0.001)
my_func = lambda x, a: np.sqrt(np.sqrt(a**4+4*x**2)-x**2-1)
c_area = np.arange(0.3, 1.6, 0.1)
y_arr = [list(map(lambda x_i: my_func(x_i, c), x_arr)) for c in c_area]

with open('data.json', "w") as f:
    json.dump([x_arr, y_arr, c_area],f,cls=NumpyEncoder)