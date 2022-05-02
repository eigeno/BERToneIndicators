import pandas as pd

df = pd.read_json('data.json')
df1 = df[df['text'].str.contains('/srs|/pos|/lh')]
print("number of filtered tweets:", df1.shape[0])
print(df1)
