__author__ = 'Bhagat'

import numpy as np
import matplotlib.pyplot as plt
import random
from library import mean, create_dataset, product, square, subtract

class line:
    predict_x=-120.01202
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.best_fit_slope_and_intercept()
        self.regression_line = [(self.m*x)+self.b for x in xs]
        self.coefficient_of_determination()

    def best_fit_slope_and_intercept(self):
        self.m=( mean(self.xs) * mean(self.ys) - mean(product(self.xs,self.ys))) / (mean(self.xs)**2 - mean(square(self.xs)))
        self.b=mean(self.ys)-self.m*mean(self.xs)

    def squared_error(self,ys_orig, ys_line):
        return sum(square(subtract(ys_line,ys_orig)))

    def coefficient_of_determination(self):
        y_mean_line = [mean(self.ys) for y in self.ys]
        squared_error_regr = self.squared_error(self.ys, self.regression_line)
        squared_error_y_mean = self.squared_error(self.ys, y_mean_line)
        self.r_squared= 1 - squared_error_regr/squared_error_y_mean

    def graph(self,color='black',size=10,predict_size=100,predict_color='green'):
        plt.scatter(self.xs,self.ys,s=size,color=color)
        plt.plot(self.xs,self.regression_line,color=color)
        if not self.predict_x==-120.01202:
            plt.scatter(self.predict_x,self.predict_y, s=predict_size, color=predict_color)
        plt.show()

    def predict(self, predict_x=-120.01202):
        self.predict_x=predict_x
        self.predict_x=predict_x
        self.predict_y = (self.m*self.predict_x)+self.b
        return self.predict_y

    def clear_predict(self):
        self.predict_x=-120.01202



