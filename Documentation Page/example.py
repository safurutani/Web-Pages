import pandas as pd
dict = {
    'Name':["Abigail", "Sebastian", "Sam", "Alex", "Emily", "Penny"],
    'Age':[19, 25, 43, 18, 33, 59],
    'College Grad':[False, False, True, False, True, True],
    'Ethnicity':["Chinese", "Irish", "Italian", "Filipino", "Canadian", "African American"]
}
df = pd.DataFrame(dict)

print(df[(df['Age'] > 40) & (df['College Grad'] == True)])
