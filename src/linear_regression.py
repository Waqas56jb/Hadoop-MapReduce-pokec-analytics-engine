from mrjob.job import MRJob
import numpy as np
import os

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
        yield "coefficients", coeff.tolist()

if __name__ == '__main__':
    input_path = os.path.join('..', 'data', 'processed', 'pokec_final.csv')
    output_path = os.path.join('..', 'data', 'output', 'regression_results.txt')
    
    with open(input_path, 'r') as f, open(output_path, 'w') as out:
        mr_job = MRLinearRegression(args=[f.name])
        with mr_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                out.write(line.decode('utf-8'))