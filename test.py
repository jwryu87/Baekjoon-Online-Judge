import pandas as pd

lst_names = ['철수','영희','민수', '민아', '영석', '석희', '희순', '영철']
lst_lang = [80,90,95,100,100,95,75,80]
lst_math = [70,85,90,95,75,80,90,85]
lst_eng = [80,85,80,100,95,90]

df = pd.DataFrame([ x for x in zip(lst_names,lst_lang,lst_math,lst_eng)],
                  columns=['이름','국어','수학','영어'])
print(df)