import matplotlib.pyplot as plt
import numpy as np
import anatrans.transport.analytical_equation as eq
import anatrans.visualize.plot_line as line
import anatrans.visualize.plot_surface as surf

comparison_dictionary = {
    "v": 1609.1 / 3.281, #m/yr
    "alpha_x": 28.5 / 3.281,
    "alpha_y": 2.9 / 3.281,
    "alpha_z": 0,
    "R": 1.2,
    "l_model": 1450 / 3.281,
    "w_model": 320 / 3.281,
    "t_model": 5,
    "d_source": 10 / 3.281,
    "c_source": np.array([[0,9], [50 / 3.281,2.8], [75 / 3.281,0.07], [125 / 3.281,0]]),
    "m_total": "inf",
    "n" : 0.25,
    "t_half" : 0.10,
    "dO": 5.78,
    "dNO3": 17,
    "Fe2": 11.3,
    "dSO4": 100,
    "CH4": 0.414,
}


bioscreen_nodeg_y05 = np.array([9.000, 8.435, 7.267, 5.900, 4.091, 2.151, 0.780, 0.183, 0.027, 0.002, 0.000])
bioscreen_nodeg_y1 = np.array([9.000, 8.467, 7.465, 6.680, 6.070, 5.548, 5.006, 4.327, 3.441, 2.410, 1.432])
bioscreen_nodeg_y2 = np.array([9.000, 8.467, 7.466, 6.684, 6.089, 5.624, 5.250, 4.940, 4.679, 4.454, 4.256])
bioscreen_lineardecay_y05 = np.array([9.000, 4.348, 1.965, 0.889, 0.386, 0.146, 0.043, 0.009, 0.001, 0.000, 0.000])
bioscreen_lineardecay_y1 = np.array([9.000, 4.348, 1.969, 0.905, 0.424, 0.201, 0.096, 0.046, 0.022, 0.010, 0.004])
bioscreen_lineardecay_y2 = np.array([9.000, 4.348, 1.969, 0.905, 0.424, 0.201, 0.096, 0.047, 0.023, 0.011, 0.005])
bioscreen_instant_y05 = np.array([9.000, 8.332, 6.473, 2.364, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000])
bioscreen_instant_y1 = np.array([9.000, 8.466, 7.405, 6.331, 5.165, 3.757, 1.724, 0.000, 0.000, 0.000, 0.000])
bioscreen_instant_y2 = np.array([9.000, 8.466, 7.407, 6.350, 5.268, 4.192, 3.152, 2.167, 1.244, 0.378, 0.000])
bioscreen_x = np.array([0, 145, 290, 435, 580, 725, 870, 1015, 1160, 1305, 1450]) / 3.281

time_list = [0.5, 1, 2]
nodeg = [bioscreen_nodeg_y05, bioscreen_nodeg_y1, bioscreen_nodeg_y2]
lineardecay = [bioscreen_lineardecay_y05, bioscreen_lineardecay_y1, bioscreen_lineardecay_y2]
instant = [bioscreen_instant_y05, bioscreen_instant_y1, bioscreen_instant_y2]
subplot_list = ["a","b","c"]

obj = eq.Transport(comparison_dictionary, "no_decay", 1 / 3.281, 1 / 3.281, 0.5)
cxyt, x, y, t = obj.domenico()
for i in range(len(time_list)):
    plot = line.Lineplot(cxyt, x, y, t)
    plt.figure(dpi=200, figsize=(6, 4))
    plot.centerline(time = time_list[i], color = "red", label = "anatrans")
    plt.plot(bioscreen_x, nodeg[i], "--", color = "black", label = "bioscreen")
    plt.title(subplot_list[i], loc="left")
    plt.legend()
    plt.show()

obj = eq.Transport(comparison_dictionary, "linear_decay", 1 / 3.281, 1 / 3.281, 0.5)
cxyt, x, y, t = obj.domenico()
for i in range(len(time_list)):
    plot = line.Lineplot(cxyt, x, y, t)
    plt.figure(dpi=200, figsize=(6, 4))
    plot.centerline(time = time_list[i], color = "red", label = "anatrans")
    plt.plot(bioscreen_x, lineardecay[i], "--", color = "black", label = "bioscreen")
    plt.title(subplot_list[i], loc="left")
    plt.legend()
    plt.show()

obj = eq.Transport(comparison_dictionary, "instant_reaction", 1 / 3.281, 1 / 3.281, 0.5)
cxyt, x, y, t = obj.domenico()
for i in range(len(time_list)):
    plot = line.Lineplot(cxyt, x, y, t)
    plt.figure(dpi=200, figsize=(6, 4))
    plot.centerline(time = time_list[i], color = "red", label = "anatrans")
    plt.plot(bioscreen_x, instant[i], "--", color = "black", label = "bioscreen")
    plt.title(subplot_list[i], loc="left")
    plt.legend()
    plt.show()

