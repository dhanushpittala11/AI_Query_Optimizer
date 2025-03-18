import joblib
import pandas as pd
from database import connect_to_db, execute_query, close_connection

# Load the trained model
model = joblib.load("query_optimizer_model.pkl")

# Example query features (replace with actual values)
query_features = {
    "query_complexity": 5,  # Example: Number of joins
    "table_size": 10000,    # Example: Number of rows in the table
    "index_usage": 1        # Example: 1 if index is used, 0 otherwise
}

# Convert features to DataFrame
features_df = pd.DataFrame([query_features])

# Predict execution time
predicted_time = model.predict(features_df)
print(f"Predicted Execution Time: {predicted_time[0]} ms")

# Example: Execute the query and compare actual vs predicted time
conn = connect_to_db()
query = "SELECT * FROM query_performance WHERE query_complexity = 5;"
results = execute_query(conn, query)
close_connection(conn)

# Compare actual vs predicted time (you can log this for future training)
actual_time = 0.094  # Replace with actual execution time
print(f"Actual Execution Time: {actual_time} ms")