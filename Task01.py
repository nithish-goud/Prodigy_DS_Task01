#Task -01: Data Visualization
#Author:Nithish Goud Battupalli
#Internship:Prodigy Infotech - Data Science
# Objective: Create a bar chart and histogram to visualize data distribution
#
# 1. Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# For displaying plots in Jupyter Notebook
%matplotlib inline
#
#2. Load Data set
#
df = pd.read_csv("C:\Users\Ruchi\Downloads\large_population.csv")
df.head()
#
#3. Bar Chart
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=df, palette="viridis")
plt.title("Gender Distribution",fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
#
#4.Histogram
plt.figure(figsize=(6,4))
sns.histplot(df["Age"],bins=10,kde=True,color="blue")
plt.title("Age Distribution", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
#
#Summary
print("Bar Chart shows categorical distribution(Gender).")
print("Histogram shows continuous distribution(Age).")
