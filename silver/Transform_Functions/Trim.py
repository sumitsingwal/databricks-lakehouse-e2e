import pyspark.sql.functions as F
from pyspark.sql.types import StringType
from pyspark.sql.functions import trim,col

def func_trim_col(df):
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
    return df