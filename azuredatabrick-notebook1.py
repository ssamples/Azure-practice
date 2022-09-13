# Databricks notebook source
# MAGIC %md ###Exploration Notebook
# MAGIC TESTING PYTHON CODE

# COMMAND ----------

# DBTITLE 1,Simple Python Print
"Hello World"

# COMMAND ----------

# DBTITLE 1,Recursive Algorithm
# Databricks notebook source
# Recursive Algorithm - need items but this is an example
def backwardsby2(num):
    if num <= 0:
        print('Zero!')
        return
    else:
        emojismiles = []
        for i in range(0, num):
            emojismiles += '😃'
        print(num, ' '.join(emojismiles))
        backwardsby2(num - 2)


backwardsby2(9)


# COMMAND ----------

# DBTITLE 1,Simple Sum in Python
#sum in Python
x = int(10)
y = int(5)
print (x+y)

# COMMAND ----------

# DBTITLE 1,Arrays in Python simple
#Python:  How to Sum an Array of Items
array = [1,1,2,0,-1]
sum_array = sum (array)
print(sum_array)

# COMMAND ----------

# DBTITLE 1,Previously defined Variables
#Using Previously defined variables
array2 = sum_array + 2
print(array2)

# COMMAND ----------

# DBTITLE 1,Display Azure Databricks mountPoints
display(dbutils.fs.mounts())

# COMMAND ----------

# DBTITLE 1,Mount Blob Storage using Python
# #Create Variable for Mounting storage for use in Databrick account
# storage_account_name = "azuredatabricksstorage1"
# storage_account_key = "xzzE2xoVhIM48lgicta+whoyUs+OH3v9fTzTz39cYkqfmxa235oDw0CHR8UP+iBI9vcQBClcSAEA+AStLFZLvw=="
# container = "taxisource"

# # set a Spark config to point to your instance of Azure Blob Storage
# spark.conf.set("fs.azure.account.key.{0}.blob.core.windows.net".format(storage_account_name), storage_account_key)

# #To mount it to Azure Databricks, use the dbutils.fs.mount method. The source is the address to your instance of Azure Blob Storage and a specific container. The mount point is where it will be mounted in the Databricks File Storage on Azure Databricks. The extra configs is where you pass in the Spark config so it doesn't always need to be set.
# dbutils.fs.mount(
 # source = "wasbs://{0}@{1}.blob.core.windows.net".format(container, storage_account_name),
 # mount_point = "/mnt//databricks-datasets",
 # extra_configs = {"fs.azure.account.key.{0}.blob.core.windows.net".format(storage_account_name): storage_account_key}
# )

#Check it can see files in the storage account
dbutils.fs.ls("dbfs:/mnt//databricks-datasets")

# COMMAND ----------

# DBTITLE 1,Mount Data Lake Gen 2 Storage using Python
# #Create Variable for Mounting storage for use in Databrick account
# storage_account_name = "taxisourcedatalakegen2"
# storage_account_key = "i+WYiV8OUbLzxIbLlhcI2t1u0tzB/x4PNNR2+Lcbw1wiB2AdVaeK9Ta0UsuUsUDRqROGlwicZiAe+AStxRAlvg=="
# container = "taxisourcedatalakegen2"

# # set a Spark config to point to your instance of Azure Blob Storage
# spark.conf.set("fs.azure.account.key.{0}.blob.core.windows.net".format(storage_account_name), storage_account_key)

# #To mount it to Azure Databricks, use the dbutils.fs.mount method. The source is the address to your instance of Azure Blob Storage and a specific container. The mount point is where it will be mounted in the Databricks File Storage on Azure Databricks. The extra configs is where you pass in the Spark config so it doesn't always need to be set.
# dbutils.fs.mount(
 # source = "wasbs://{0}@{1}.blob.core.windows.net".format(container, storage_account_name),
 # mount_point = "/mnt//databricks-datasets2",
 # extra_configs = {"fs.azure.account.key.{0}.blob.core.windows.net".format(storage_account_name): storage_account_key}
# )

#Check it can see files in the storage account
dbutils.fs.ls("dbfs:/mnt//databricks-datasets2")
