# 📊 Práctica Integral de Big Data: Batch y Streaming

**Estudiante:** Jeimmy Nuñez   
**Programa:** Ingeniería de Sistemas  
**Institución:** Unad  
**Asignatura:** Big Data  

---

## 📝 Descripción de la Solución
Este repositorio contiene la solución completa de la práctica académica, abarcando dos paradigmas de procesamiento de datos:
1. **Batch (Spark y HDFS):** Análisis retrospectivo de datos estructurados masivos mediante el script `análisis_batch_spark.py`.
2. **Streaming (Kafka y Spark Streaming):** Ingesta y procesamiento en tiempo real de eventos de sensores IoT (`kafka_producer.py` y `spark_streaming_consumer.py`) agrupados en ventanas temporales de un minuto.

---

## 🛠️ Contenido del Repositorio
* `análisis_batch_spark.py`: Script de procesamiento por lotes sobre HDFS.
* `kafka_producer.py`: Productor de eventos simulados de sensores hacia Kafka.
* `spark_streaming_consumer.py`: Consumidor de Spark Streaming con agregaciones en tiempo real.

---

## 🚀 Instrucciones de Ejecución
* **Batch:** `spark-submit análisis_batch_spark.py`
* **Streaming:** Iniciar los servicios de Zookeeper y Kafka, ejecutar el productor con `python3 kafka_producer.py`, y correr el consumidor con:
  ```bash
  spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py
