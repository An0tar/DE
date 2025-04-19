from clickhouse_driver import Client

client = Client(host='10.0.2.2')

create_table_query = """
CREATE TABLE IF NOT EXISTS employees123
(
    name String,
    position String,
    salary Float64,
    hire_date Date
)
ENGINE = MergeTree()
ORDER BY name;
"""

client.execute(create_table_query)
print("Таблица employees123 успешно создана.")

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark ClickHouse Connection") \
    .config("spark.jars", "clickhouse-jdbc-0.4.6.jar") \
    .getOrCreate()



url = "jdbc:clickhouse://10.0.2.2:8123/default"
properties = {
    "user": "default",
    "password": "",
    "driver": "com.clickhouse.jdbc.ClickHouseDriver"
}
data = [
    ("Alice", "Engineer", 75000, "2021-06-15"),
    ("Bob", "Manager", 90000, "2020-05-01"),
    ("Charlie", "HR", 60000, "2019-04-12"),
    ("Diana", "Sales", 50000, "2018-01-25")
]
columns = ["name", "position", "salary", "hire_date"]

df = spark.createDataFrame(data, columns)

df.write.jdbc(url=url, table="default.employees123", mode="overwrite", properties=properties)

print("Данные успешно записаны в таблицу employees")



spark.stop()