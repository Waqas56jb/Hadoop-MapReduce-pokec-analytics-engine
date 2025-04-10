from mrjob.job import MRJob
import os

class MRDemographicAnalysis(MRJob):
    def mapper(self, _, line):
        if "user_id" in line:
            return
        fields = line.split(',')
        gender = fields[1]
        region = fields[3]
        age = float(fields[2])
        yield (gender, region), (age, 1)

    def reducer(self, key, values):
        ages = []
        count = 0
        for age, cnt in values:
            ages.append(age)
            count += cnt
        avg_age = sum(ages) / len(ages)
        yield key, {"avg_age": avg_age, "count": count}

if __name__ == '__main__':
    input_path = os.path.join('..', 'data', 'processed', 'pokec_clean.csv')
    output_path = os.path.join('..', 'data', 'output', 'demographic_results.txt')
    
    # Simulate MapReduce execution
    with open(input_path, 'r') as f, open(output_path, 'w') as out:
        mr_job = MRDemographicAnalysis(args=[f.name])
        with mr_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                out.write(line.decode('utf-8'))