import os

os.environ["SPARK_HOME"] = "/usr/local/spark"

from pyspark import SparkContext

testFile = "sample.txt"
sc = SparkContext("local", "Simple App")
logData = sc.textFile(testFile)

numAs = logData.filter(lambda s: 'radvin' in s)

numBs = logData.filter(lambda s: 'atrina' in s)

filterNumA = numAs.flatMap(lambda line: line.split(",")).take(1)
filterNumB = numBs.flatMap(lambda line: line.split(",")).take(1)

print(filterNumA + filterNumB)
sc.stop()