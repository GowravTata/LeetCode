# Code to create a column based on the other column
# Ways of approaching the solution
data['Bonus'] = data['Salary'] * 2

data['Bonus'] = data['Salary'].apply(lambda x:x*2)


# 2. How to drop duplicates from the dataset
customer.drop_duplicates([subset='email'])


# 3.Replacing the column names in the dataframe
students.rename(columns={'id':'student_id','first':'first_name','last':'last_name',
    'age':'age_in_years'},inplace=True)

#4. Modify Columns by multiplying salary column by 2
employees['salary'] = employees['salary']*2
employees['salary'] = employees['salary'].apply(lambda x:x*2)

#5. Converting a data type from float to numeric by selecting a column in the dataframe
students.grade = students.grade.astype(int)

#6. Drop the data missing from the dataframe where the data is null for name column
students.dropna(subset=['name'], inplace=True)

#7. In the dataframe replace all the null values with 0 for a particular column
products.quantity.fillna(0,inplace=True)

#8. Concatenating two tables into a single dataframe
df = pd.concat([df1,df2])

#9. Write a function to pivot the table , to which
weather.pivot_table(index='month',columns='city',values='temperature',aggfunc='max')

#10. Write to melt a table so 
report.melt(id_vars=['product'],var_name='quarter',value_name='sales')

#11. Return the dataframe which based on like this
animals[animals['weight']>100].sort_values(by='weight',ascending=False)[['name']]
