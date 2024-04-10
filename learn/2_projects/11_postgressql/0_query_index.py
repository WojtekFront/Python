from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""
    DO $$
    BEGIN
        IF NOT EXISTS(SELECT 1 FROM information_schema.columns
            WHERE TABLE_NAME = 'cars' AND COLUMN_NAME = 'id') THEN
            ALTER TABLE cars ADD COLUMN id SERIAL PRIMARY KEY;
        END IF;
    END $$               
    """)
    
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

