import pandas as pd
import random

# Generate synthetic data
data = {
    "query_complexity": [random.randint(1, 10) for _ in range(100)],
    "table_size": [random.randint(100, 100000) for _ in range(100)],
    "index_usage": [random.randint(0, 1) for _ in range(100)],
    "execution_time": [random.randint(50, 500) for _ in range(100)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)