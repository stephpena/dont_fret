import pandas as pd
import pyspark
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating


class ALSImplicitModel(object):

    def __init__(self):
        self.spark = pyspark.sql.SparkSession.builder.getOrCreate()
        self.sc = self.spark.sparkContext
        with open('data/user_item_df.csv') as f:
            user_item_df = pd.read_csv(f)
        self.user_item_df = user_item_df.astype(int)

    def fit_and_save_model(self,train_num=0.8,test_num=0.2,seed_num=2711,rank=5,iterations=5):
        user_item_spark_df = self.spark.createDataFrame(self.user_item_df)
        user_item_rdd = user_item_spark_df.rdd
        train, test = user_item_rdd.randomSplit([train_num, test_num], seed=seed_num)
        testdata = test.map(lambda p: (p[0], p[1]))
        model = ALS.trainImplicit(train, rank=rank, iterations=iterations, nonnegative=True)
        model.save(self.sc,'data/firstmodel')

if __name__ == "__main__":
    model = ALSImplicitModel()
    model = model.fit_and_save_model()
    print 'Successfully saved model!'
