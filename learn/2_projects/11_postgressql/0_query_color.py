from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS(SELECT 1 FROM information_schema.columns 
                WHERE table_name ='cars' AND COLUMN_NAME = 'color') THEN
                ALTER TABLE cars ADD COLUMN color VARCHAR(10);
            END IF;
        END $$
        """) 

    cursor.execute("""  
        ALTER TABLE cars ALTER column color TYPE VARCHAR(30);
        """)
    cursor.execute("""
        UPDATE cars SET color = 'default_color' WHERE color IS NULL;
        """)
    cursor.execute("""
        ALTER TABLE cars ALTER COLUMN color SET NOT NULL;
        """)

    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS( SELECT 1 FROM information_schema.columns 
                   WHERE table_name = 'cars' AND column_name = 'mileage') THEN
                   ALTER TABLE cars ADD COLUMN mileage INTEGER;
                END IF;
            END $$
            """)
    cursor.execute("""
            UPDATE cars SET mileage = 0 WHERE mileage is NULL ;
            """)
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS( SELECT 1 FROM information_schema.columns
                WHERE table_name = 'cars' AND column_name = 'price_gross') THEN
                ALTER TABLE cars ADD COLUMN price_gross MONEY;
            END IF;
        END $$
        """)
    cursor.execute("""
        UPDATE CARS SET price_gross = 0 WHERE price_gross IS NULL;        




        """)


except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

