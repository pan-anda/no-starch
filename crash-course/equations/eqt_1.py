import numpy as np
import matplotlib.pyplot as plt

def main():
    x=np.arange(-2,2,0.01)
    y=np.arange(-2,2,0.01)
    x,y=np.meshgrid(x,y)
    z=np.power(x,2)+np.power(y,2)-1
    plt.contour(x,y,z,0)
    plt.show()

main()
