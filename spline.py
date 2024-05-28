def interpolate_spline(x_nodes, y_nodes, x_values):
    n = len(x_nodes) - 1
    h = [x_nodes[i+1] - x_nodes[i] for i in range(n)]
    alpha = [0] + [(3 / h[i] * (y_nodes[i+1] - y_nodes[i]) - 3 / h[i-1] * (y_nodes[i] - y_nodes[i-1])) for i in range(1, n)]
    
    l = [1] + [0] * n
    mu = [0] * (n + 1)
    z = [0] * (n + 1)
    
    for i in range(1, n):
        l[i] = 2 * (x_nodes[i+1] - x_nodes[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    l[n] = 1
    z[n] = 0

    b = [0] * n
    c = [0] * (n + 1)
    d = [0] * n
    c[n] = 0

    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y_nodes[j+1] - y_nodes[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    def S(x, j):
        return y_nodes[j] + b[j] * (x - x_nodes[j]) + c[j] * (x - x_nodes[j])**2 + d[j] * (x - x_nodes[j])**3

    y_values = []
    for x in x_values:
        for j in range(n):
            if x_nodes[j] <= x <= x_nodes[j+1]:
                y_values.append(S(x, j))
                break
    
    return y_values
