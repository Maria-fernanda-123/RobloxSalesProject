from db.connection import get_connection

def get_platform_by_id(platform_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM platforms WHERE platform_id=%s", (platform_id,))
    platform = cursor.fetchone()
    cursor.close()
    conn.close()
    return platform

def list_platforms():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM platforms")
    platforms = cursor.fetchall()
    cursor.close()
    conn.close()
    return platforms