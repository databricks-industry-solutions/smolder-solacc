# Smolder: A package for ingesting HL7 messages to Delta Lake
<img src="https://drive.google.com/uc?export=view&id=1CEptCFInlQRfrgW2ZQyl09KlntdAmK34" width=100>

"Smolder" is evidently a synonym for "glow" and nicely alludes to FHIR ("Fire"), so what could be a better name for a Databricks-y library for loading HL7 (and eventually FHIR?) data! To start, smolder defines a very simple Spark file format that loads one HL7 message per file, and parses it into a dataframe. Here, we'll demonstrate this using HL7 ADT messages generated from our Synthea cohort. It might even work for _streaming data_...


<div style="text-align: center; line-height: 0; padding-top: 9px;">
<img src="https://databricks.com/wp-content/uploads/2021/01/blog-image-ehr-in-rt-1.jpg" width=900>
</div>

___

&copy; 2022 Databricks, Inc. All rights reserved. The source in this notebook is provided subject to the Databricks License [https://databricks.com/db-license-source].  All included or referenced third party libraries are subject to the licenses set forth below.

|Library Name|Library License|Library License URL|Library Source URL| 
| :-: | :-:| :-: | :-:|
| Spark|Apache-2.0 License | https://github.com/apache/spark/blob/master/LICENSE | https://github.com/apache/spark  |
|Smolder |Apache-2.0 License| https://github.com/databrickslabs/smolder | https://github.com/databrickslabs/smolder/blob/master/LICENSE|
