def langrage_point(x_nodes, y_nodes, x):
    def L(k, x):
        Lk = 1
        for i in range(len(x_nodes)):
            if i != k:
                Lk *= (x - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
        return Lk

    y_interpolated = 0
    for k in range(len(x_nodes)):
        y_interpolated += y_nodes[k] * L(k, x)
    
    return y_interpolated

def interpolate_lagrange(x_nodes, y_nodes, x_values):
    return [langrage_point(x_nodes, y_nodes, x) for x in x_values]