import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Neha"],
    "Sales": [12000, 15000, 18000, 10000]
}

df = pd.DataFrame(data)

total_sales = df["Sales"].sum()

df.loc[len(df)] = ["TOTAL", total_sales]

df.to_excel("sales_report.xlsx", index=False)

print("Excel report generated successfully!")