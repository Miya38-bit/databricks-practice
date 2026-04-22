from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("databricks-dev").getOrCreate()
print(spark.version) 