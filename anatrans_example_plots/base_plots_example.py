import matplotlib.pyplot as plt
import anatrans.transport.analytical_equation as eq
import anatrans.visualize.plot_line as line
import anatrans.visualize.plot_surface as surf
from anatrans.data.parameter_information import example_dictionary

mode_list = ["no_decay", "linear_decay", "instant_reaction"]
name_list = ["no decay", "linear decay", "instant reaction"]
color_list = ["black", "red", "green"]


plt.figure(dpi=200, figsize=(8, 6))
for i in range(len(mode_list)):
    obj = eq.Transport(example_dictionary, mode_list[i], 1 / 3.281, 1 / 3.281, 1)
    cxyt, x, y, t= obj.domenico()
    plot = line.Lineplot(cxyt, x, y, t)
    plot.centerline(time = 3, color = color_list[i], label = name_list[i])
plt.ylim((0,14))
#plt.title("Comparison of Domenico model modes, t = 3 years")
plt.legend()
plt.show()

obj = eq.Transport(example_dictionary, "no_decay", 1 / 3.281, 1 / 3.281, 1)
cxyt, x, y, t = obj.domenico()
plot = surf.Plume(cxyt, x, y, t)
ax = plot.surface(time = 5, cmap = "viridis")
ax.view_init(elev=30, azim=340)
#plt.title("Contaminant plume with Domenico model, linear decay, t = 5 years")
plt.show()

plot.flat(time = 5)
#plt.title("Contaminant plume with Domenico model, linear decay, t = 5 years")
plt.show()
