import pyspark
from pyspark.sql.types import *
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

spark = pyspark.sql.SparkSession.builder \
            .master("local") \
            .appName("Don't Fret") \
            .getOrCreate()
sc = spark.sparkContext

class ALSImplicitModel(object):

  def __init__(self,):
      self.model = model

  def fit(self.model):
    user_item_spark_df = spark.createDataFrame(user_item_df)
    user_item_rdd = user_item_spark_df.rdd
    train, test = user_item_rdd.randomSplit([0.8, 0.2], seed=2711)
    testdata = test.map(lambda p: (p[0], p[1]))

if __name__ == "__main__":
    pass
