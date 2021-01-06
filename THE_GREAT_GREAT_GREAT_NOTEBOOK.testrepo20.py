# Databricks notebook source
import sys
sys.path.append("/Workspace/Projects/sai.suram@databricks.com/testrepo20")

# COMMAND ----------

import codegen

# COMMAND ----------

# MAGIC %sh 
# MAGIC cd /Workspace/Projects/sai.suram@databricks.com/testrepo20
# MAGIC strace python -c 'import codegen' 2>&1 | grep 'testrepo20'

# COMMAND ----------

# MAGIC %sh 
# MAGIC cd /Workspace/Projects/sai.suram@databricks.com/testrepo20
# MAGIC strace python -c 'import codegen' 2>&1 | grep 'testrepo20' | sort | uniq

# COMMAND ----------

from pathlib import Path
def treeWalkInternal(start, stats):
  if start.is_dir():
    stats["ndirs"]+=1
    # print(f"{start} is dir")
    for x in start.iterdir():
      treeWalkInternal(x, stats)
  else:
    stats["nfiles"]+=1
    size = len(start.read_bytes())
    stats["nbytes"] += size
    # print(f"{start} is file. size = {size}")

def treeWalk(start):
  stats = {"nfiles":0 , "ndirs":0, "nbytes": 0}
  %time treeWalkInternal(start, stats)
  print(f"stats for {start} = {stats}")

treeWalk(Path("/Workspace/Projects/sai.suram@databricks.com/testrepo20"))
treeWalk(Path("/Workspace/Projects/sai.suram@databricks.com/mlflow")) 

# COMMAND ----------

# MAGIC %time Path("/Workspace/Projects/sai.suram@databricks.com/testrepo20/codegen.py").read_bytes()
# MAGIC %time Path("/Workspace/Projects/sai.suram@databricks.com/mlflow/mlflow/deployments/utils.py").read_bytes()

# COMMAND ----------

# MAGIC %time Path("/Workspace/Projects/sai.suram@databricks.com/mlflow/mlflow/deployments/utils.py").read_bytes()

# COMMAND ----------

# MAGIC %time Path("/Workspace/Projects/sai.suram@databricks.com/mlflow/mlflow/deployments/utils.py").read_bytes()

# COMMAND ----------

# MAGIC %time x=Path("/Workspace/Projects/sai.suram@databricks.com/mlflow/Dockerfile").read_bytes()