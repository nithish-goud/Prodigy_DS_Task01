# Task -01: Data Visualization
# Author: Nithish Goud Battupalli
# Internship: Prodigy Infotech - Data Science
# Objective: Create a bar chart and histogram to visualize data distribution

# 1. Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset (update path if dataset is in a different location)
df = pd.read_csv(r"C:\Users\Ruchi\Downloads\large_population.csv")

# Display first 5 rows
print("Dataset Preview:")
print(df.head())

# 3. Bar Chart - Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="Gender", data=df, palette="viridis")
plt.title("Gender Distribution", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("gender_distribution.png")   # Save chart as PNG
plt.show()

# 4. Histogram - Age Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df["Age"], bins=10, kde=True, color="blue")
plt.title("Age Distribution", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_distribution.png")   # Save chart as PNG
plt.show()

# 5. Summary
print("\nSummary:")
print("Bar Chart shows categorical distribution (Gender).")
print("Histogram shows continuous distribution (Age).")
