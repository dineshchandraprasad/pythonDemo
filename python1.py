import pandas as pd
# df= pd.read_csv("nyc_weather.csv")
# print(df['Temperature'].min())
# print(df.Temperature.max())
# print(df.Temperature [df.Events == 'Rain'])
# print(df['WindSpeedMPH'])
# print(df.WindSpeedMPH.describe())
# weather = [('1/6/2017',31,2,'Sunny'),
# ('2/6/2017',29,1,'Winter'),
# ('4/6/2017',84,4,'summer'),
# ('8/6/2017',23,3,'Bunny'),
# ('9/6/2017',76,3,'rainy')]

# df = pd.DataFrame(weather, columns = ['date','temp','windspeed','season'])
# print(df)

# print(df['date''temp'])
# print(df.shape)
# print(df['date'][df.temp == df.temp.max()])
# print(df.columns)
# print(df[['date','temp']])
# print(df['date'][df.temp == df.temp.min()])
# print(df[df.temp == df.temp.max()])
# df.to_csv("new.csv", index=False)
# df.to_excel("new.xlsx",sheet_name = "weather_data")
# print(df)

# df =pd.read_csv("py.csv")
# print(df[['hello','name']])

# to load and read the excel files we should install a package called xlrd (xl read data)
# and to read the excel file the syntax should be like...
#  df = pd.read_excel("myexcelfile.xlsx")
# single excel file contains multiple tables those are nothing but the sheet names and it is like
# df.read_excel("myexcelfile.xlsx", sheet_name="weather_data")
# to store the excel file in another file we need to install a package called openpyxl (open is open source and py is python and xl is short notation of excel)
# syntax to store the excel files are...
# df.to_excel("new.xlsx") it will create a excel file with indexed rows, but we want to remove the index then we need to add argument as index=False
# df.to_excel("new.xlsx", index = False)

#dataframe operators:

# df = pd.read_csv("weather_data_cities.csv")
# print(df)

# for a, b in g:
#     print(a)
#     print(b)
# print(df.groupby('city').describe())


# concatinating tables

us_data = [
    ('1/5/2017',31,1,'Rain'),
    ('2/5/2017',32,2,'sunny'),
    ('3/5/2017',33,3,'fog'),
    ('4/5/2017',34,4,'rainy'),
    ('5/5/2017',35,5,'snow')
]

us_data = pd.DataFrame(us_data, columns = ['date','temp','humidity','season'])
# print(us_data)
india_data = pd.DataFrame({
    "date": ['19/5/2017','12/5/2017','13/5/2017','4/5/2017'],
    "temp": [39,43,38,54],
    "humidity": [1,2,3,4],
    "season": ["rainy","cloudy","sunny","sunny"]
})
print(india_data)
print(pd.concat([us_data,india_data],ignore_index=False)) # concatinating tables

print(pd.concat([us_data, india_data], ignore_index=True)) # it will print in order wise index
print(pd.concat([us_data,india_data], axis =1)) # row wise concatinating

#Merging  tables
india_data.to_csv("ekjv.csv")
india_data.to_csv("ekjvn.csv",index=False)


us_data = [
    ('hyd',34),
    ('viz',39),
    ('nellur',33)
]
us_data = pd.DataFrame(us_data, columns = ['city','temp'])
print(us_data)

india_data = pd.DataFrame({
    "city": ['hyd','tirupathi','nlg'],
    "humidity": [1,2,3]
})
print(india_data)

print(pd.concat([us_data,india_data],sort=False))
print(pd.merge(us_data,india_data, how="outer"))
 print(s.iloc[3])

# import pandas as pd
# import matplotlib.pyplot as plt
# # iris = pd.read_csv("irisdata.csv")
# # print(iris.tail())
# # plt.plot(iris['SepalLength'],"g--")
# # plt.show()
# # Import necessary libraries
# import seaborn as sns
# # import matplotlib.pyplot as plt

# # Load iris data
# iris = pd.read_csv("iris.csv")
# # iris = sns.load_dataset("iris.csv")

# # Construct iris plot
# sns.swarmplot(x="species", y="petal_length", data=iris)

# # Show plot
# plt.show()