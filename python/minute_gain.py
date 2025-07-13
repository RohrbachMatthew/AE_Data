import pandas as pd

from config import db_config
import mysql.connector


connection = mysql.connector.connect(**db_config)

query = """
select ae_date, ae_time, total_payout_amount, total_parcel_count
from ae_data
order by ae_date DESC, ae_time DESC
"""

df = pd.read_sql(query, connection)
connection.close()

# Date time column
df['datetime'] = pd.to_datetime(df['ae_date']) + pd.to_timedelta(df['ae_time'])
df = df.sort_values('datetime')

df["minute_gain"] = df["total_payout_amount"].diff()
print(df[['total_parcel_count', 'datetime', 'total_payout_amount', 'minute_gain']])
