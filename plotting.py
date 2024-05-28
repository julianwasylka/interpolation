import pandas as pd
import matplotlib.pyplot as plt
import math
import random
from lagrange import interpolate_lagrange
from spline import interpolate_spline

def interpolate(filename, method, nodes_num, savename=None, chybyshev=False, deviation=False): #methods -> lagrange or spline
    x, y = read_data(filename)

    x_nodes, y_nodes = get_interpolation_nodes(x, y, nodes_num, chybyshev, deviation)
    
    if method == 'lagrange':
        method_for_title = 'wielomian interpolacyjny Lagrange\'a'
        y_interpolated = interpolate_lagrange(x_nodes, y_nodes, x)
    elif method == 'spline':
        method_for_title = 'funkcje sklejane'
        y_interpolated = interpolate_spline(x_nodes, y_nodes, x)

    plot_interpolation(x, y, x_nodes, y_nodes, y_interpolated, filename, method_for_title, nodes_num, savename)

def plot_interpolation(x, y, x_nodes, y_nodes, y_interpolated, filename, method_for_title, nodes_num, savename):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='b', label='Oryginalne dane')
    plt.scatter(x_nodes, y_nodes, color='purple', zorder=5, label='Węzły')
    plt.plot(x, y_interpolated, color='r', label='Interpolacja')

    plt.title(f'{filename}: metoda - {method_for_title}, liczba węzłów - {nodes_num}')
    plt.xlabel('dystans')
    plt.ylabel('wysokość')

    plt.legend()
    plt.grid(True)

    if savename != None: plt.savefig(f'{savename}.png')
    plt.show()

def read_data(filename):
    data = pd.read_csv(f'2018_paths/{filename}.csv')

    return data['x'], data['y']

def get_interpolation_nodes(x, y, nodes_num, Chybyshev=False, deviation=False):
    length = len(x)

    if Chybyshev:
        cheb_nodes = [(math.cos((2*k - 1) * math.pi / (2 * nodes_num))) for k in range(1, nodes_num + 1)]
        indices = [(int((n + 1) * (length - 1) / 2)) for n in cheb_nodes]
    else:
        step = length // (nodes_num - 1)
        indices = [i * step for i in range(nodes_num - 1)]
        indices.append(length - 1)

    x_nodes = [x[i] for i in indices]
    y_nodes = [y[i] for i in indices]
    
    if deviation:
        num_to_deviate = int(random.random() * nodes_num)
        nodes_indices = random.sample(range(nodes_num), num_to_deviate)
        for index in nodes_indices:
            y_nodes[index] += random.uniform(-0.4 * (max(y_nodes) - min(y_nodes)), 0.4 * (max(y_nodes) - min(y_nodes)))

    return x_nodes, y_nodes

if __name__ == '__main__':
    def ex2():
        #chybyshev = False
        interpolate('GlebiaChallengera', 'lagrange', 4, 'plots/ex2/4')
        interpolate('GlebiaChallengera', 'lagrange', 6, 'plots/ex2/6')
        interpolate('GlebiaChallengera', 'lagrange', 7, 'plots/ex2/7')
        interpolate('GlebiaChallengera', 'lagrange', 8, 'plots/ex2/8')
        interpolate('GlebiaChallengera', 'lagrange', 10, 'plots/ex2/10')
        interpolate('GlebiaChallengera', 'lagrange', 12, 'plots/ex2/12')

    def ex3():
        #chybyshev = False
        interpolate('Unsyncable_ride', 'lagrange', 4, 'plots/ex3/4')
        interpolate('Unsyncable_ride', 'lagrange', 6, 'plots/ex3/6')
        interpolate('Unsyncable_ride', 'lagrange', 8, 'plots/ex3/8')
        interpolate('Unsyncable_ride', 'lagrange', 9, 'plots/ex3/9')

    def ex4():
        #chybyshev = False
        interpolate('GlebiaChallengera', 'spline', 4, 'plots/ex4/4')
        interpolate('GlebiaChallengera', 'spline', 8, 'plots/ex4/8')
        interpolate('GlebiaChallengera', 'spline', 12, 'plots/ex4/12')
        interpolate('GlebiaChallengera', 'spline', 16, 'plots/ex4/16')

    def ex5():
        #chybyshev = False
        interpolate('Unsyncable_ride', 'spline', 4, 'plots/ex5/4')
        interpolate('Unsyncable_ride', 'spline', 8, 'plots/ex5/8')
        interpolate('Unsyncable_ride', 'spline', 12, 'plots/ex5/12')
        interpolate('Unsyncable_ride', 'spline', 16, 'plots/ex5/16')

    def bonus():
        #chybyshev = False
        interpolate('WielkiKanionKolorado', 'lagrange', 6, 'plots/bonus/6l')
        interpolate('WielkiKanionKolorado', 'spline', 6, 'plots/bonus/6s')
        interpolate('SpacerniakGdansk', 'lagrange', 8, 'plots/bonus/8l')
        interpolate('SpacerniakGdansk', 'spline', 8, 'plots/bonus/8s')

    def ex6():
        #chybyshev = True
        interpolate('WielkiKanionKolorado', 'lagrange', 6, 'plots/ex6/6a', True)
        interpolate('WielkiKanionKolorado', 'spline', 6, 'plots/ex6/s6a', False)
        interpolate('WielkiKanionKolorado', 'lagrange', 12, 'plots/ex6/12a', True)
        interpolate('WielkiKanionKolorado', 'spline', 12, 'plots/ex6/s12a', False)
        interpolate('SpacerniakGdansk', 'lagrange', 6, 'plots/ex6/6b', True)
        interpolate('SpacerniakGdansk', 'spline', 6, 'plots/ex6/s6b', False)
        interpolate('SpacerniakGdansk', 'lagrange', 12, 'plots/ex6/12b', True)
        interpolate('SpacerniakGdansk', 'spline', 12, 'plots/ex6/s12b', False)