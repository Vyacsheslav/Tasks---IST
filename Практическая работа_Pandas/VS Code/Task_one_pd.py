import pandas as pd

lst = [['tom','reacher',25], ['krish','pete',30], ['nick','wilson',26], ['juli','williams',22]]

df = pd.DataFrame(lst, columns=['FName', 'LName', 'Age'], dtype=float)

print(df)