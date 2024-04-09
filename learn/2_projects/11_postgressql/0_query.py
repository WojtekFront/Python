from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS(SELECT 1 FROM information_schema.columns WHERE table_name ='cars' AND COLUMN_NAME = 'color') THEN
                    ALTER TABLE cars ADD COLUMN color VARCHAR(10);
            end if;
        END $$
        """) 

    cursor.execute("""  
        ALTER TABLE cars ALTER column color TYPE VARCHAR(30);
        """)
    cursor.execute("""
        UPDATE cars set color = 'default_color' WHERE color IS NULL;
        """)
    cursor.execute("""
        ALTER TABLE cars ALTER COLUMN color SET NOT NULL;
        """)

except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

