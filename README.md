# Smolder: A package for ingesting HL7 messages to Delta Lake

In this notebook, we demonstrate how [Smolder](https://github.com/databrickslabs/smolder) can be used to parse HL7v2 message into your lakehouse. Smolder defines a very simple Spark file format that loads one HL7 message per file, and parses it into a dataframe. Here, we'll demonstrate this using a stream of HL7 ADT messages generated from a simulated dataset with [Synthea](https://github.com/synthetichealth/synthea)


<div style="text-align: center; line-height: 0; padding-top: 9px;">
<img src="https://databricks.com/wp-content/uploads/2021/01/blog-image-ehr-in-rt-1.jpg" width=900>
</div>

___

&copy; 2022 Databricks, Inc. All rights reserved. The source in this notebook is provided subject to the Databricks License [https://databricks.com/db-license-source].  All included or referenced third party libraries are subject to the licenses set forth below.

|Library Name|Library License|Library License URL|Library Source URL| 
| :-: | :-:| :-: | :-:|
| Spark|Apache-2.0 License | https://github.com/apache/spark/blob/master/LICENSE | https://github.com/apache/spark  |
|Smolder |Apache-2.0 License| https://github.com/databrickslabs/smolder | https://github.com/databrickslabs/smolder/blob/master/LICENSE|

To run this accelerator, clone this repo into a Databricks workspace. Attach the RUNME notebook to any cluster running a DBR 11.0 or later runtime, and execute the notebook via Run-All. A multi-step-job describing the accelerator pipeline will be created, and the link will be provided. Execute the multi-step-job to see how the pipeline runs.

The job configuration is written in the RUNME notebook in json format. The cost associated with running the accelerator is the user's responsibility.

## Disclaimers
Databricks Inc. (“Databricks”) does not dispense medical, diagnosis, or treatment advice. This Solution Accelerator (“tool”) is for informational purposes only and may not be used as a substitute for professional medical advice, treatment, or diagnosis. This tool may not be used within Databricks to process Protected Health Information (“PHI”) as defined in the Health Insurance Portability and Accountability Act of 1996, unless you have executed with Databricks a contract that allows for processing PHI, an accompanying Business Associate Agreement (BAA), and are running this notebook within a HIPAA Account. Please note that if you run this notebook within Azure Databricks, your contract with Microsoft applies.

All names,  last names and places in this notebook have been randomly generated. No identification with actual persons (living or deceased), places, buildings, and products is intended or should be inferred.