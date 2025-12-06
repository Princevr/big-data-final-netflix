#!/usr/bin/env python
# coding: utf-8

# ## Notebook_1
# 
# null

# In[1]:


# Load the raw table (change table name if needed)
df = spark.read.table("netflix_raw")

display(df)          # Shows the first rows
df.printSchema()     # Shows column names and types


# In[2]:


from pyspark.sql.functions import col, to_date, regexp_extract, year

df_clean = (
    df
    # Make sure release_year is integer
    .withColumn("release_year", col("release_year").cast("int"))
    
    # Convert date_added (e.g. 'September 9, 2019') to a proper date
    .withColumn("date_added", to_date(col("date_added"), "MMMM d, yyyy"))
    
    # Extract number from duration (e.g. '90 min' or '2 Seasons')
    .withColumn(
        "duration_int",
        regexp_extract(col("duration"), r"(\d+)", 1).cast("int")
    )
    
    # Remove rows missing important fields
    .na.drop(subset=["title", "type"])
)

display(df_clean)
df_clean.printSchema()


# In[3]:


df_clean.write.mode("overwrite").saveAsTable("netflix_clean")


# In[4]:


titles_per_type = (
    df_clean.groupBy("type")
    .count()
    .withColumnRenamed("count", "num_titles")
)

display(titles_per_type)


# In[5]:


top_countries = (
    df_clean
    .groupBy("country")
    .count()
    .withColumnRenamed("count", "num_titles")
    .orderBy(col("num_titles").desc())
)

display(top_countries.limit(10))


# In[6]:


titles_by_year = (
    df_clean
    .where(col("date_added").isNotNull())
    .withColumn("year_added", year(col("date_added")))
    .groupBy("year_added")
    .count()
    .withColumnRenamed("count", "num_titles")
    .orderBy("year_added")
)

display(titles_by_year)


# In[6]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# SELECT
#   type,
#   COUNT(*) AS num_titles
# FROM netflix_clean
# GROUP BY type;



# In[7]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# SELECT
#   country,
#   COUNT(*) AS num_titles
# FROM netflix_clean
# WHERE country IS NOT NULL
# GROUP BY country
# ORDER BY num_titles DESC
# LIMIT 10;


# In[8]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# SELECT
#   YEAR(date_added) AS year_added,
#   COUNT(*) AS num_titles
# FROM netflix_clean
# WHERE date_added IS NOT NULL
# GROUP BY YEAR(date_added)
# ORDER BY year_added;


# In[ ]:




