import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from matplotlib.pyplot import xlabel

from config import db_config

connection = mysql.connector.connect(**db_config)

query = """
select * from ae_data
order by ae_date, ae_time
"""
df = pd.read_sql(query, connection)
connection.close()

df['datetime'] = pd.to_datetime(df['ae_date']) + pd.to_timedelta(df['ae_time'])
df = df.sort_values('datetime')

# gets difference between total payouts
df['minute_gain'] = df['total_payout_amount'].diff()

# plot
plt.figure(figsize=(16, 9))
sns.lineplot(data=df, x="datetime", y='total_payout_amount', label='Payout', marker='o', color='green')
sns.lineplot(data=df, x='datetime', y='total_parcel_count', label='Parcels', marker='o', color='blue')
plt.title("Parcel Count and Total Payout Amount")
plt.xlabel("Date and Time")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('Total_Payout_Parcels.png')