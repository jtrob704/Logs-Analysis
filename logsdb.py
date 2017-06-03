"""Database code for the New logs."""
import psycopg2

DBNAME = "news"

def get_posts():
    """Return all entries from the 'database', most recent first."""
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("select content, time from posts order by time desc;")
    return cur.fetchall()
    conn.close()
