import json
import plotly.graph_objs as go
from plotly import offline
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

with open('data.json') as f:
    aaarrrr = json.load(f)

x_arr = np.asarray(aaarrrr[0])
c_area = np.asarray(aaarrrr[2])
y_arr = np.asarray(aaarrrr[1])
data = [go.Scatter(x=np.append(x_arr,np.flip(x_arr)), y=np.append(y_i,np.flip(np.negative(y_i))), name='c = '+str(round(c_i,2))) for y_i, c_i in zip(y_arr, c_area)]

fig = go.Figure(
    data=data,
    layout_title_text="Овал Кассіні при a = 1, с змінюється від 0.3 до 1.6 з кроком 0.1"
)

offline.plot(fig, filename='plot.html', auto_open=False)