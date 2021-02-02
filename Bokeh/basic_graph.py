from bokeh.plotting import figure
from bokeh.io import output_file, show

# test data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]


# output file path
output_file("line.html")

# initialize an object of fundamental of graph
f = figure()

# f.line(x, y)  # line graph
f.triangle(x, y)  # triangle point graph
f.circle(y, y)   # circle point graph

show(f)
