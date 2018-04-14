import numpy as np
import matplotlib.pyplot as plt
 
def coefficient_estimation(x, y):
    # number of observations
    n = np.size(x)
 
    # mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    dev_xy = np.sum(y*x - n*mean_y*mean_x)
    dev_xx = np.sum(x*x - n*mean_x*mean_x)
 
    # calculating regression coefficients
    b_1 = dev_xy / dev_xx
    b_0 = mean_y - b_1*mean_x
 
    return(b_0, b_1)
 
def regression_line_plot(x, y, b):
    # plotting actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # labelling
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
 
def main():
    # observations input
    x = np.array([0, 3, 5,7, 9,11,13,15,17,19,21])
    y = np.array([2, 5, 7, 3, 8, 10, 14, 17, 21, 22, 25])
 
    # coefficient estimation output
    b = coefficient_estimation(x, y)
    print("b_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    # regression line plot output
    regression_line_plot(x, y, b)
 
if __name__ == "__main__":
    main()