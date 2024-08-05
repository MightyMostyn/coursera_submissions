import matplotlib.pyplot as PyPlot
import numpy as NumPy
from PseudoKit import chardefinitions

def plot_char(character):
    axes.imshow(character)

def main():

    eight = NumPy.array([
        [0., 0., 0.],
        [0., 1., 0.],
        [0., 0., 0.],
        [0., 1., 0.],
        [0., 0., 0.]
        ])
    
    eight = eight * 128
    
    eight[2, :] = 255.

    #print(eight)

    thefigure, theaxes = PyPlot.subplots()

    global figure
    figure = thefigure

    global axes
    axes = theaxes

    ## Plot F A C E using the characters defined above
    plot_char(chardefinitions.charMatrix('F'))
    plot_char(chardefinitions.charMatrix('A'))
    plot_char(chardefinitions.charMatrix('C'))
    plot_char(chardefinitions.charMatrix('E'))    

    #axes.imshow(char_A)#, cmap="gray")

    PyPlot.show()

if __name__ == "__main__":
    main()

