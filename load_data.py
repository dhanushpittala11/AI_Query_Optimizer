import pandas as pd
from database import connect_to_db, insert_data, close_connection

# Load the CSV file
df = pd.read_csv("data.csv")

# Convert numpy types to native Python types
df = df.astype({
    "query_complexity": int,
    "table_size": int,
    "index_usage": int,
    "execution_time": int
})

# Connect to the database
conn = connect_to_db()

# Insert each row into the database
for index, row in df.iterrows():
    # Explicitly cast to native Python types before insertion
    insert_data(
        conn,
        int(row["query_complexity"]),
        int(row["table_size"]),
        int(row["index_usage"]),
        int(row["execution_time"])
    )

# Close the connection
close_connection(conn)

print("Data loaded into PostgreSQL successfully!")
