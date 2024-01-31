import pandas as pd

customers = pd.DataFrame({'id': list(range(1, 5)), 'name': ['Joe', 'Henry', 'Sam', 'Max']})
orders = pd.DataFrame({'id': list(range(1, 3)), 'customerId': [3, 1]})

data = pd.DataFrame(
    customers[~customers['id'].isin(orders['customerId'])].rename(columns={'name': 'Customers'})['Customers'])
# print(type(data))


df = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId')
print(df)
