import psycopg2

try:
    conn = psycopg2.connect(
        dbname="face_recognition",
        user="postgres",            # your PostgreSQL username
        password="123",   # replace with your actual password
        host="localhost",           # or IP address
        port="5432"                 # default PostgreSQL port
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL successfully!")

    # Sample query (check if tables exist)
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    for table in cursor.fetchall():
        print("Table:", table[0])

except Exception as e:
    print("❌ Connection failed:", e)

finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
