from mrjob.job import MRJob
import pandas as pd

class MRDemographicAnalysis(MRJob):
    def mapper(self, _, line):
        if "user_id" in line:  # Skip header
            return
        fields = line.split(',')
        gender = fields[1]
        region = fields[3]
        age = fields[2]
        yield (gender, region), (float(age), 1)

    def reducer(self, key, values):
        ages = []
        count = 0
        for age, cnt in values:
            ages.append(age)
            count += cnt
        avg_age = sum(ages) / len(ages)
        yield key, {"avg_age": avg_age, "count": count}

if __name__ == '__main__':
    MRDemographicAnalysis.run()