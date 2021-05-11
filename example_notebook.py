# Databricks notebook source
print(func_from_another_notebook()) 

# COMMAND ----------

# DBTITLE 1,%run works (from the sidebar we can see another_notebook exists)
# MAGIC %run ./another_notebook

# COMMAND ----------

print(func_from_another_notebook()) 

# COMMAND ----------

# DBTITLE 1,another_notebook does not show up in the list when files is enabled
# MAGIC %sh
# MAGIC ls .

# COMMAND ----------

# MAGIC %sh cat foof

# COMMAND ----------

# MAGIC %sh cat foof

# COMMAND ----------

# MAGIC %sh cat foof
