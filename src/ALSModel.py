import pyspark
from pyspark.sql.types import *
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating


class ALSImplicitModel(object):

    def __init__(self):
        self.spark = pyspark.sql.SparkSession.builder.getOrCreate()
        self.sc = spark.sparkContext
        with open('data/user_item_df.csv') as f:
            self.user_item_df = pd.read_csv(f)
            self.user_item_df = user_item_df.astype(int)

    def fit(user_item_df=self.user_item_df,seed_num=2711,train=0.8,test=0.2):
        user_item_spark_df = spark.createDataFrame(user_item_df)
        user_item_rdd = user_item_spark_df.rdd
        train, test = user_item_rdd.randomSplit([train, test], seed=seed_num)
        testdata = test.map(lambda p: (p[0], p[1]))

    def train():
        model = ALS.trainImplicit(train, rank=5, iterations=5, nonnegative=True)
        return model

    def save_model():
        model.save('data/firstmodel')

if __name__ == "__main__":
    model = ALSImplicitModel()
    model = model.fit()
    model = mode.train()
    model.save_model()
    return 'Successfully saved model!'
