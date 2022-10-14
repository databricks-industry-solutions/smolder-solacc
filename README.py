# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC <img src=" https://hls-eng-data-public.s3.amazonaws.com/img/Databricks_HLS.png" width=700> 
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Smolder: A package for ingesting HL7 messages to Delta Lake
# MAGIC In this notebook, we demonstrate how [Smolder](https://github.com/databrickslabs/smolder) can be used to parse HL7v2 message into your lakehouse. Smolder defines a very simple Spark file format that loads one HL7 message per file, and parses it into a dataframe. Here, we'll demonstrate this using a stream of HL7 ADT messages generated from a simulated dataset with [Synthea](https://github.com/synthetichealth/synthea)
# MAGIC 
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC <img src="https://databricks.com/wp-content/uploads/2021/01/blog-image-ehr-in-rt-1.jpg" width=900>
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC Copyright / License info of the notebook. Copyright Databricks, Inc. [2021].  The source in this notebook is provided subject to the [Databricks License](https://databricks.com/db-license-source).  All included or referenced third party libraries are subject to the licenses set forth below.
# MAGIC 
# MAGIC |Library Name|Library License|Library License URL|Library Source URL| 
# MAGIC | :-: | :-:| :-: | :-:|
# MAGIC | Spark|Apache-2.0 License | https://github.com/apache/spark/blob/master/LICENSE | https://github.com/apache/spark  |
# MAGIC |Smolder |Apache-2.0 License| https://github.com/databrickslabs/smolder | https://github.com/databrickslabs/smolder/blob/master/LICENSE|

# COMMAND ----------

# MAGIC %md
# MAGIC ## Disclaimers
# MAGIC Databricks Inc. (“Databricks”) does not dispense medical, diagnosis, or treatment advice. This Solution Accelerator (“tool”) is for informational purposes only and may not be used as a substitute for professional medical advice, treatment, or diagnosis. This tool may not be used within Databricks to process Protected Health Information (“PHI”) as defined in the Health Insurance Portability and Accountability Act of 1996, unless you have executed with Databricks a contract that allows for processing PHI, an accompanying Business Associate Agreement (BAA), and are running this notebook within a HIPAA Account. Please note that if you run this notebook within Azure Databricks, your contract with Microsoft applies.
# MAGIC 
# MAGIC All names have been synthetically generated, and do not map back to any actual persons or locations
