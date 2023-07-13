import pandas as pd
import matplotlib.pyplot as plt
import chardet
import csv


count = 0 
Yes_Cnt = 0
No_Cnt = 0

with open('MyDATA.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        count += 1
        if count > 4:
            break
      
        if ( row['status'] == 'Complete'):
            Yes_Cnt += 1
        else:
            No_Cnt += 1
    print('Number of Yes:',Yes_Cnt, 'Number of No:', No_Cnt )


'''
with open('./DATA.csv', 'rb') as f:
    rclsesult = chardet.detect(f.read())


covid19_data = pd.read_csv('./DATA.csv', encoding = result['encoding'])

  print(covid19_data.columns)  # Display the column names
print(covid19_data.head())  # Display the first few rows of the DataFrame


# Select the columns of interest
selected_columns = ['fainting_now', 'tremors_now', 'Heart_attack']

# Create a subset of the DataFrame with the selected columns
subset = covid19_data[selected_columns]

# Check for null values in the subset
subset_nulls = subset.isnull().sum()

# Fill missing values with 'No' to indicate absence of symptom
subset.fillna('No', inplace=True)

# Create data points based on the presence of symptoms and long COVID
points = []
for _, row in subset.iterrows():
    symptoms = row.values
    if 'Yes' in symptoms and 'Long COVID' in symptoms:
        points.append('Symptoms & Long COVID')
    elif 'Yes' in symptoms:
        points.append('Symptoms')
    elif 'Long COVID' in symptoms:
        points.append('Long COVID')
    else:
        points.append('No Symptoms or Long COVID')

# Count the occurrences of each data point
point_counts = pd.Series(points).value_counts()

# Create a bar plot of data point counts
plt.figure(figsize=(8, 6))
point_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Data Points')
plt.ylabel('Count')
plt.title('Symptoms vs. Long COVID - Data Points')
plt.xticks(rotation=0)
plt.show()
'''    
