""" This is doing the growth part.

Takes in: inital center, initial radius, max point on boundary, and growth constant.

Outputs: a graph showing the intial circle and the new circle.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111, aspect='equal')
# ax1.axis([-1, 1, -1, 1])
# ax1.add_patch(patches.Circle((0,0), 1, fill=False))
# fig1.savefig('circle1.png')

def add_circle(subplot, center, radius):
    """ Adds a circle of input center and radius to subplot.
    """
    subplot.add_patch(patches.Circle(center, radius, fill=False))

def add_point(subplot, coordinates):
    """ Adds a point (very small circle) at input coordinates to subplot.
    """
    subplot.add_patch(patches.Circle(coordinates, .01, facecolor='#000000'))

def find_new_center(rad_i, d, center_i, max_pt):
    """ Calculates center of new circle after a season of growth.

        Input: initial radius, d, initial center, maximum point

        Returns: new center, new radius
    """
    x_new = d * abs((center_i[0] - max_pt[0])) / rad_i
    y_new = d * abs((center_i[1] - max_pt[1])) / rad_i
    center_new = (x_new, y_new)
    return center_new

def find_distance(rad_i, k_growth):
    rad_new = rad_i * k_growth
    d = rad_new - rad_i
    return d, rad_new

def add_new_circle(subplot, center_i, rad_i, k, max_pt):
    d, rad_new = find_distance(rad_i, k)
    center_new = find_new_center(rad_i, d, center_i, max_pt)
    add_circle(subplot, center_new, rad_new)



# Define variables
center_i = (0, 0)       # center of initial circle
rad_i = .5              # radius of initial circle
k = 1.1                 # rate of increasing radius
max_pt = (.5, 0)        # point of maximum sunniness on boundary, Currently arbitrary
# Set up plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.axis([-1, 1, -1, 1])

add_circle(ax1, center_i, rad_i)
add_point(ax1, center_i)
add_new_circle(ax1, center_i, rad_i, k, max_pt)
#
# add_circle(ax1, (0,0), .5)
# add_point(ax1, (0,0))
# add_point(ax1, (.5,0))
# add_new_circle(ax1, .5, 1.1, (0,0), (.5,0))
fig1.savefig('circle1.png')
