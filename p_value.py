import scipy.stats as st
import math, numpy as np
import statistics 
import matplotlib.pyplot as plt

plotFig = 1
def p_value(z_score):
    return round(st.norm.cdf(z_score), 5)
def z_score(p_value):
    return round(st.norm.ppf(p_value), 2)
def cal_z_score(sample_mean, sample_sdev, sample_size, population_mean):
    population_mean = float(population_mean)
    sample_sdev = float(sample_sdev)
    sample_size = float(sample_size)
    sample_mean = float(sample_mean)
    return round((sample_mean - population_mean)/(sample_sdev/math.sqrt(sample_size)), 3)

def calculate_std_dev(num_arr):
    return statistics.stdev(num_arr)

def margin_of_error(z_s, std_dev, sample_size):
    return abs(z_s*(std_dev/math.sqrt(sample_size)))

def confidence_interval(ci_percent, std_dev, sample_size, sample_mean, two_tailed):
    z_percent = ci_percent/100
    if two_tailed == 1:
        z_s = z_score(round(((1 - z_percent) / 2), 4))
    else:
        z_s = z_score(1 - z_percent)
    margin_E = margin_of_error( z_s, std_dev, sample_size)
    res = []
    res.append(sample_mean - margin_E)
    res.append(sample_mean + margin_E)
    list.sort(res)
    return res

def plotter(axis_x, axis_y=[], x_label = 'x_label', y_label = 'y_label'):
    global plotFig
    plt.figure(plotFig)
    if len(axis_y) == 0:
        plt.plot(axis_x)
        plt.xlabel(x_label)
    else:
        plt.plot(axis_x, axis_y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    plotFig = plotFig +1


def relation_CI_MI(std_dev, sample_size, two_tailed):
    i = 0.0
    x_ax = []
    y_ax = []    
    while i <= 99.99 :
        x_ax.append(i)
        z_percent = i/100
        if two_tailed == 1:
            z_s = z_score(round(((1 - z_percent) / 2), 4))
        else:
            z_s = z_score(1 - z_percent)
        y_ax.append(margin_of_error(z_s, std_dev, sample_size))
        i = i + 0.5
    plotter(x_ax, y_ax, 'CI', 'MI')

def relation_Sample_MI(CI, std_dev, two_tailed):
    i = 10
    x_ax = []
    y_ax = []    
    z_percent = i/100
    if two_tailed == 1:
        z_s = z_score(round(((1 - z_percent) / 2), 4))
    else:
        z_s = z_score(1 - z_percent)
    while i <= 1000:
        x_ax.append(i)
        y_ax.append(margin_of_error(z_s, std_dev, i))
        i = i + 10
    plotter(x_ax, y_ax, 'size of Sample', 'MI')

# res = cal_z_score(600,400,40,500)
# print(res)
# res = p_value(1.58)
# print(res)
# res = calculate_std_dev([136,102,84,150,115,98,125,176,120,74])
# print(res)

# # res = margin_of_error()
# # print(res)
# res = confidence_interval(95, 25.8, 10, 118, 1)
# # res = z_score(0.95)
# print(res)
# res = confidence_interval(0, 25.8, 10, 118, 1)
# # res = z_score(0.95)
# print(res)

# relation_CI_MI(25.8, 10, 1)
# relation_Sample_MI(95.0, 25.8, 1)


# plt.show()

