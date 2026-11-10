import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics as s

sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

df = pd.read_csv("/home/avcoe/heart.csv")
df.head()

#information of the dataset
df.info()

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

#Data type of each column
print("Data Type for Each Columns are\n",df.dtypes.value_counts())

print(df.describe())

print(df.head())

#Missing values
df.dtypes == 'object'

n = df.columns[df.dtypes != 'object']

#Display all values
df[n]

# dataframe.size
size = df.size
print("Size of dataset is :",size)
  
# dataframe.shape
shape = df.shape
print("shape of datset is \n\n:",shape)

#All zeros
df[n].isnull().sum().sort_values(ascending=False)

#Missing values
df.dtypes == 'object'
n = df.columns[df.dtypes != 'object']
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age values with median
df['age'] = df['age'].fillna(df['age'].median())
print("\nMissing Values After Handling:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

# --------------------------------------------------
# Statistical Analysis
# --------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nStandard Deviation:")
print(df.std(numeric_only=True))

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))


# Data Visualization
# --------------------------------------------------

# Histogram of Age
plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=20, edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Histogram - Cholesterol
plt.figure(figsize=(8, 5))
plt.hist(df['chol'], bins=15, edgecolor='black')
plt.title('Histogram of Cholesterol')
plt.xlabel('Cholesterol')
plt.ylabel('Frequency')
plt.show()

# Boxplot - Age
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['age'])
plt.title('Boxplot of Age')
plt.show()

# Boxplot - Cholesterol
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['chol'])
plt.title('Boxplot of Cholesterol')
plt.show()

#Finding mean age of Patients
df['age']
#Average Age of the Patients
average = s.mean(df['age'])
print("Average age : ",average)


#Extracting Particular Columns
print(df['age'])
print(df['sex'])
print(df['trestbps'])
print(df['chol'])

#Spliting the data into training and testing data
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
X.shape
y = df.target
y.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=56)

print(X_train)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

print("\nTraining Target Shape:")
print(y_train.shape)

print("\nTesting Target Shape:")
print(y_test.shape)
