import pandas as pd
df  = pd.read_csv('final.csv')
df.sort_values('weighted_rating' , ascending = False , inplace = True)
output = df[['original_title' , 'poster_link' , 'runtime' , 'release_date' , 'weighted_rating']].head(20)