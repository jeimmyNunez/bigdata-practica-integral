from pyspark.sql import SparkSession, functions as F

# Inicializa la sesión de Spark
spark = SparkSession.builder.appName('Tarea3').getOrCreate()

# Define la ruta del archivo .csv en HDFS
file_path = 'hdfs://localhost:9000/Tarea3/rows.csv'

# Lee el archivo .csv
df = spark.read.format('csv').option('header','true').option('inferSchema', 'true').load(file_path)

# Imprimimos el esquema y mostramos filas
df.printSchema()
df.show()

# Estadísticas básicas
df.summary().show()

# Filtrar por valor mayor a 5000
print("Días con valor mayor a 5000\n")
dias = df.filter(F.col('VALOR') > 5000).select('VALOR', 'VIGENCIADESDE', 'VIGENCIAHASTA')
dias.show()

# Ordenar filas por la columna "VALOR" de forma descendente
print("Valores ordenados de mayor a menor\n")
sorted_df = df.sort(F.col("VALOR").desc())
sorted_df.show()