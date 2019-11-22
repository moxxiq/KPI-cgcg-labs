import numpy as np
import plotly.graph_objs as go
from plotly import offline

x_arr = np.arange(-2.6,2.6,0.001)
my_func = lambda x, a: np.sqrt(np.sqrt(a**4+4*x**2)-x**2-1)
c_area = np.arange(0.3, 1.6, 0.1)
y_arr = [list(map(lambda x_i: my_func(x_i, c), x_arr)) for c in c_area]
data = [go.Scatter(x=np.append(x_arr,np.flip(x_arr)), y=np.append(y_i,np.flip(np.negative(y_i))), name='c = '+str(round(c_i,2))) for y_i, c_i in zip(y_arr, c_area)]

fig = go.Figure(
    data=data,
    layout_title_text="Овал Кассіні при a = 1, с змінюється від 0.3 до 1.6 з кроком 0.1"
)

offline.plot(fig, filename='plot.html', auto_open=False)