from mrjob.job import MRJob
import numpy as np

class MRLinearRegression(MRJob):
    def mapper(self, _, line):
        if "user_id" in line:
            return
        fields = line.split(',')
        age = float(fields[2])
        completion = float(fields[4])
        yield None, (age, completion)

    def reducer(self, _, values):
        X, Y = [], []
        for x, y in values:
            X.append(x)
            Y.append(y)
        X = np.array(X)
        Y = np.array(Y)
        coeff = np.polyfit(X, Y, 1)
        yield "Regression Coefficients", coeff.tolist()

if __name__ == '__main__':
    MRLinearRegression.run()