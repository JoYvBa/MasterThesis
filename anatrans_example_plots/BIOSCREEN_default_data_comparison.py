import matplotlib.pyplot as plt
import numpy as np
import anatrans.transport.analytical_equation as eq
import anatrans.visualize.plot_line as line
from anatrans.data.parameter_information import example_dictionary

example_dictionary["w_model"] = 200 / 3.281
example_dictionary["t_model"] = 10

bioscreen_nodeg_y1 = np.array([13.657, 8.062, 5.759, 3.907, 2.269, 1.063, 0.387, 0.107, 0.022, 0.003, 0.000])
bioscreen_nodeg_y3 = np.array([13.612, 8.624, 7.012, 6.182, 5.606, 5.127, 4.670, 4.186, 3.648, 3.052, 2.425])
bioscreen_nodeg_y5 = np.array([13.566, 8.600, 7.002, 6.192, 5.658, 5.258, 4.939, 4.672, 4.438, 4.223, 4.015])
bioscreen_nodeg_y10 = np.array([13.454, 8.529, 6.944, 6.141, 5.612, 5.217, 4.903, 4.645, 4.425, 4.236, 4.070])
bioscreen_lineardecay_y1 = np.array([13.657, 3.366, 1.061, 0.357, 0.119, 0.036, 0.010, 0.002, 0.000, 0.000, 0.000])
bioscreen_lineardecay_y3 = np.array([13.612, 3.358, 1.064, 0.366, 0.130, 0.047, 0.017, 0.006, 0.002, 0.001, 0.000])
bioscreen_lineardecay_y5 = np.array([13.566, 3.347, 1.060, 0.365, 0.130, 0.047, 0.017, 0.006, 0.002, 0.001, 0.000])
bioscreen_lineardecay_y10 = np.array([13.454, 3.319, 1.052, 0.362, 0.129, 0.047, 0.017, 0.006, 0.002, 0.001, 0.000])
bioscreen_instant_y1 = np.array([13.374, 6.845, 2.885, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000])
bioscreen_instant_y3 = np.array([12.771, 7.975, 6.446, 5.641, 5.009, 4.326, 3.428, 2.171, 0.466, 0.000, 0.000])
bioscreen_instant_y5 = np.array([12.181, 7.502, 6.032, 5.313, 4.848, 4.498, 4.200, 3.920, 3.627, 3.293, 2.880])
bioscreen_instant_y10 = np.array([10.760, 6.330, 4.938, 4.257, 3.820, 3.494, 3.225, 2.987, 2.768, 2.560, 2.360])
bioscreen_x = np.array([0,32, 64, 96, 128, 160, 192, 224, 256, 288, 320]) / 3.281

time_list = [1, 3, 10]
nodeg = [bioscreen_nodeg_y1, bioscreen_nodeg_y3, bioscreen_nodeg_y10]
lineardecay = [bioscreen_lineardecay_y1, bioscreen_lineardecay_y3, bioscreen_lineardecay_y10]
instant = [bioscreen_instant_y1, bioscreen_instant_y3, bioscreen_instant_y10]
subplot_list = ["a","b","c"]

obj = eq.Transport(example_dictionary, "no_decay", 1 / 3.281, 1 / 3.281, 1)
cxyt, x, y, t = obj.domenico()
for i in range(len(time_list)):
    plot = line.Lineplot(cxyt, x, y, t)
    plt.figure(dpi=200, figsize=(6, 4))
    plot.centerline(time = time_list[i], color = "red", label = "anatrans")
    plt.plot(bioscreen_x, nodeg[i], "--", color = "black", label = "bioscreen")
    plt.title(subplot_list[i], loc="left")
    plt.legend()
    plt.show()

obj = eq.Transport(example_dictionary, "linear_decay", 1 / 3.281, 1 / 3.281, 1)
cxyt, x, y, t = obj.domenico()
for i in range(len(time_list)):
    plot = line.Lineplot(cxyt, x, y, t)
    plt.figure(dpi=200, figsize=(6, 4))
    plot.centerline(time = time_list[i], color = "red", label = "anatrans")
    plt.plot(bioscreen_x, lineardecay[i], "--", color = "black", label = "bioscreen")
    plt.title(subplot_list[i], loc = "left")
    plt.legend()
    plt.show()

obj = eq.Transport(example_dictionary, "instant_reaction", 1 / 3.281, 1 / 3.281, 1)
cxyt, x, y, t = obj.domenico()
for i in range(len(time_list)):
    plot = line.Lineplot(cxyt, x, y, t)
    plt.figure(dpi=200, figsize=(6, 4))
    plot.centerline(time = time_list[i], color = "red", label = "anatrans")
    plt.plot(bioscreen_x, instant[i], "--", color = "black", label = "bioscreen")
    plt.title(subplot_list[i], loc="left")
    plt.legend()
    plt.show()
