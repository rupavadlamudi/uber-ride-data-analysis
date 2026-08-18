"step-1 load and understanding"

import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\HP\Downloads\Uber_project\uber_analysis.csv")
df.info()
df.describe()
df.head()
df.shape
print("rows:",df.shape[0])
print("colums:",df.shape[1])

'step-2:-missing values'
m=df.isnull().sum()
m
'step-3 misssing percentage' 

m_p=(m/len(df))*100
m_p

'step-4 duplicate check'
d=df.duplicated.sum()
' can also check column wise'
d_p=df["Booking ID"].duplicated().sum()
d_p
"step -5  repeted duplicated frequency count of each"
r_d=df["Booking ID"].value_counts()
r_d
r=r_d[r_d>1]
r
'step-6  unique checking'
u=df.nunique()
u
'step-7 data type'
dt=df.dtypes
dt
'step-8 analysis '
c=df["Vehicle Type"].value_counts()
c
c_p=df["Payment Method"].value_counts()
c_p

c_b=df["Booking Status"].value_counts()
c_b

c_d=df["Cancelled Rides by Driver"].value_counts()
c_d

c_pl=df["Pickup Location"].nunique()
c_pl
c_dp=df["Drop Location"].nunique()
c_dp
' top 10 with count'
c_v=df["Pickup Location"].value_counts().head(10)
c_v

c_dv=df["Drop Location"].value_counts().head(10)
c_dv

' step-9 numeric calculation'
n_t=df[["Avg VTAT","Avg CTAT","Ride Distance","Driver Ratings","Customer Rating"]].describe()
n_t


'step-10-missing investigation'
missing_summary=pd.DataFrame({"missing count": df.isnull().sum()})
missing_summary

'add another column to missing summary'
missing_summary['missing percenatge']=(m/len(df))*100
missing_summary

"extract only the important columns whose ocunt>0 and removing remaing columns in table"
missing_summary=missing_summary[missing_summary["missing count"]>0]
missing_summary

'arranging in ascending order'
missing_summary=missing_summary.sort_values("missing percenatge",ascending=False)
missing_summary

'checking linkage or pattern analysis'
ct=pd.crosstab(df["Booking Status"], df["Booking Value"].isnull())
ct

cr=pd.crosstab(df["Booking Status"], df["Ride Distance"].isnull())
cr

cp=pd.crosstab(df["Booking Status"], df["Driver Ratings"].isnull())
cp

cc=pd.crosstab(df["Booking Status"], df["Customer Rating"].isnull())
cc


d_t=pd.crosstab(df["Booking Status"], df["Avg VTAT"].isnull())
d_t

d_c=pd.crosstab(df["Booking Status"], df["Avg CTAT"].isnull())
d_c


c_r=pd.crosstab(
    df["Booking Status"],
    df["Reason for cancelling by Customer"].isnull()
)

c_r


dd=pd.crosstab(
    df["Booking Status"],
    df["Driver Cancellation Reason"].isnull()
)

dd


ci=pd.crosstab(
    df["Booking Status"],
    df["Incomplete Rides"].isnull()
)


ci



cir=pd.crosstab(
    df["Booking Status"],
    df["Incomplete Rides Reason"].isnull()
)

cir

cp=pd.crosstab(
    df["Booking Status"],
    df["Payment Method"].isnull()
)   
cp

pn=df["Payment Method"].value_counts(dropna=False)
pn

df["Booking Status"].value_counts()

"coverting booking staus in percentag eform"
df["Booking Status"].value_counts(normalize=True) * 100


"time and date analysis"
df["Date"].head()
'it is object-text format need to convert'

df["Date"] = pd.to_datetime(df["Date"])

df["Date"].describe()


df["Date"].dtype

"year counts"
df["Date"].dt.month.value_counts().sort_index()


"week day"
df["Date"].dt.day_name().value_counts()

"time asnalysis"
df["Time"].head()

"coverting object time into time"
df["Time"]=pd.to_datetime(df["Time"],format="%H:%M:%S")

df["Time"].head()
"analysis based on time"
df["Time"].dt.hour.value_counts().sort_index()

df["Time"].min(), df["Time"].max()



"missing dat and time"
df[["Date", "Time"]].isnull().sum()


" vechile typ ethrpugh satus "

pd.crosstab(
    df["Vehicle Type"],
    df["Booking Status"]
)

"which pickup point have more cancliation"

pd.crosstab(
    df["Pickup Location"],
    df["Booking Status"]
)


df["Pickup Location"].value_counts().head(10)

df["Booking Status"].isin(
    ["Cancelled by Customer", "Cancelled by Driver"]
)


df["Is Cancelled"].value_counts()



df.groupby("Pickup Location")["Is Cancelled"].mean().sort_values(ascending=False).head(10)



df.groupby("Vehicle Type")["Is Cancelled"].mean().sort_values(ascending=False)


df["Booking Status"].value_counts(normalize=True) * 100
df["Driver Cancellation Reason"].value_counts()

df["Reason for cancelling by Customer"].value_counts()

df["Reason for cancelling by Customer"].value_counts(normalize=True) * 100

df.groupby("Vehicle Type")["Reason for cancelling by Customer"].count().sort_values(ascending=False)


customer_cancel_rate = (
    df[df["Reason for cancelling by Customer"].notna()]
    .groupby("Vehicle Type")
    .size()
    / df.groupby("Vehicle Type").size()
) * 100

customer_cancel_rate.sort_values(ascending=False)


df[df["Reason for cancelling by Customer"].notna()]["Day of Week"].value_counts()




# Step 12: Deeper EDA / Relationship Analysis

print("Booking Status ↔ Vehicle Type")
print(pd.crosstab(df["Vehicle Type"], df["Booking Status"]))

print("\nBooking Status ↔ Pickup Location")
print(pd.crosstab(df["Pickup Location"], df["Booking Status"]))

print("\nBooking Status ↔ Drop Location")
print(pd.crosstab(df["Drop Location"], df["Booking Status"]))

print("\nRide Distance ↔ Booking Value")
print(df[["Ride Distance", "Booking Value"]].corr())

print("\nDriver Ratings ↔ Booking Status")
print(df.groupby("Booking Status")["Driver Ratings"].agg(["count", "mean", "median"]))

print("\nCustomer Rating ↔ Booking Status")
print(df.groupby("Booking Status")["Customer Rating"].agg(["count", "mean", "median"]))

print("\nAvg VTAT ↔ Booking Status")
print(df.groupby("Booking Status")["Avg VTAT"].agg(["count", "mean", "median"]))

print("\nAvg CTAT ↔ Booking Status")
print(df.groupby("Booking Status")["Avg CTAT"].agg(["count", "mean", "median"]))



# Step 13: Outlier Analysis using IQR

outlier_columns = [
    "Booking Value",
    "Ride Distance",
    "Avg VTAT",
    "Avg CTAT",
    "Driver Ratings",
    "Customer Rating"
]

outlier_summary = []

for col in outlier_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outlier_count = df[
        (df[col] < lower_bound) |
        (df[col] > upper_bound)
    ][col].count()
    
    outlier_percentage = (outlier_count / len(df)) * 100
    
    outlier_summary.append([
        col,
        Q1,
        Q3,
        lower_bound,
        upper_bound,
        outlier_count,
        outlier_percentage
    ])

outlier_summary = pd.DataFrame(
    outlier_summary,
    columns=[
        "Column",
        "Q1",
        "Q3",
        "Lower Bound",
        "Upper Bound",
        "Outlier Count",
        "Outlier Percentage"
    ]
)

outlier_summary



# Step 14: Final Python Cleaning

clean_df = df.copy()

# Remove duplicate Booking IDs
clean_df = clean_df.drop_duplicates(subset="Booking ID")

# Correct Date datatype
clean_df["Date"] = pd.to_datetime(
    clean_df["Date"],
    errors="coerce"
)

# Correct Time datatype
clean_df["Time"] = pd.to_datetime(
    clean_df["Time"].astype(str),
    errors="coerce"
)

# Correct numeric datatypes
numeric_columns = [
    "Booking Value",
    "Ride Distance",
    "Avg VTAT",
    "Avg CTAT",
    "Driver Ratings",
    "Customer Rating"
]

for col in numeric_columns:
    clean_df[col] = pd.to_numeric(
        clean_df[col],
        errors="coerce"
    )

print("Original shape:", df.shape)
print("Cleaned shape:", clean_df.shape)

print("\nRemaining missing values:")
print(
    clean_df.isnull().sum()
    .sort_values(ascending=False)
    .head(15)
)

print("\nData types:")
print(clean_df.dtypes)


# Step 15: Export Clean Dataset

output_path = r"C:\Users\HP\Downloads\Uber_project\uber_cleaned.csv"

clean_df.to_csv(
    output_path,
    index=False
)

print("Clean dataset exported successfully!")
print("Location:", output_path)
print("Rows:", clean_df.shape[0])
print("Columns:", clean_df.shape[1])






