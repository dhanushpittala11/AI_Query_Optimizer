import psycopg2

def connect_to_db():
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(
        dbname="query_optimizer",
        user="postgres",
        password="ChantHK@365",
        host="localhost",
        port="5432"
    )
    return conn

def execute_query(conn, query):
    """Execute a SQL query and return the results."""
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def insert_data(conn, query_complexity, table_size, index_usage, execution_time):
    """Insert data into the query_performance table."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO query_performance (query_complexity, table_size, index_usage, execution_time) VALUES (%s, %s, %s, %s)",
        (query_complexity, table_size, index_usage, execution_time)
    )
    conn.commit()
    cursor.close()

def close_connection(conn):
    """Close the database connection."""
    conn.close()