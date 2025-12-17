import pandas as pd
scores=pd.Series([85,90,78,92])
print(scores)

scores = pd.Series([85, 90, 78, 92], index=["Math", "Eng", "Bio", "Chem"])
print(scores)

#Pandas Dataframe from dictionary
print("DATAFRAME: ")

data={
    "Name":["Ola","Imisi","Ayomide","Timi","Eniola","Michael","Samuel","Wisdom","Seyi","Bolu"],
    "Age":[20,21,24,18,26,22,21,23,23,21],
    "Score":[92,86,90,78,88,90,76,85,84,77]
    }
df=pd.DataFrame(data)
print(df)

#Inspecting dataframes
print("HEADS: ",df.head())    #First 5 rows
print("TAILS: ",df.tail())    #Last 5 rows
print("SHAPES: ",df.shape)   #(Rows, Columns)
print("COLUMNS: ",df.columns)   # Column names
print("INFO: ",df.info())    #Data types + nulls

#Selecting Data
print("SELECTING:",df["Name"])
print("SELECTING:",df["Score"])
#By position
print("POSITIONING: ")
print(df.iloc[0])   #First row
print(df.iloc[1:3])   #Row 1 to 2

#Filtering rows
print("FILTERING ROWS:")
print(df[df["Score"]>85])   #Scores greater than 85

print(df[(df["Score"]>85)&(df["Age"]>20)])  #Scores greater than 85 and Age above 20

#Basic Operations
print("BASIC OPERATIONS:")
print(df["Score"].mean())
print(df["Age"].max())
print(df["Score"].sum())

#PRACTICE:
data1={
    "Name1":["Bob","Allen","Grace","April","Johnson","Gabriel","Sunny","Andrew","Caleb"],
    "Department":["CSC","BSA","MSC","PHY","BIO","MED","BAN","ENG","POL"],
    "CGPA":[3.14,2.33,4.22,4.56,4.67,2.34,1.78,3.99,4.10]
}
print("DATAFRAME: ")
df1=pd.DataFrame(data1)
print(df1)
print("CGPA COLUMN ONLY: ")
print(df1["CGPA"])
print("STUDENTS WITH CGPA ABOVE 3.5:")
print(df1[df1["CGPA"]>3.5])
print("SHAPE OF THE DATAFRAME: ")
print(df1.shape)