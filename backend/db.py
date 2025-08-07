import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def build_connection_string(prefix: str) -> str:
    server = os.getenv(f"{prefix}_SERVER")
    instance = os.getenv(f"{prefix}_INSTANCE")
    database = os.getenv(f"{prefix}_DATABASE")
    user = os.getenv(f"{prefix}_USER")
    password = os.getenv(f"{prefix}_PASSWORD")
    encrypt = os.getenv("DB_ENCRYPT", "false").lower() == "true"
    trust_cert = os.getenv("DB_TRUST_SERVER_CERT", "false").lower() == "true"

    full_server = f"{server}\\{instance}" if instance else server

    return (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={full_server};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        f"Encrypt={'yes' if encrypt else 'no'};"
        f"TrustServerCertificate={'yes' if trust_cert else 'no'};"
    )

# Connections
def get_db1_connection():
    return pyodbc.connect(build_connection_string("DB1"))

def get_db2_connection():
    return pyodbc.connect(build_connection_string("DB2"))

# Optional: Test at startup
def test_db_connections():
    try:
        conn1 = get_db1_connection()
        conn1.cursor().execute("SELECT 1")
        print("✅ DB1 Connected (SERVERSSRETAILTRAN)")
        conn1.close()

        conn2 = get_db2_connection()
        conn2.cursor().execute("SELECT 1")
        print("✅ DB2 Connected (SERVERSSRETAIL)")
        conn2.close()

    except Exception as e:
        print("❌ DB Connection Failed:", e)
