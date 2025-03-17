import sqlite3

# Connect to the SQLite database
with sqlite3.connect("library.db") as conn:
    cursor = conn.cursor()
    
    # Create the Books table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    """)
    
    # Insert initial book data
    books = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", books)
    conn.commit()
    
    # Update the Year_Published of 1984 to 1950
    cursor.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984"))
    conn.commit()
    
    # Retrieve and display Dystopian books
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", ("Dystopian",))
    print("Dystopian Books:")
    for row in cursor.fetchall():
        print(row)
    
    # Delete books published before 1950
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    conn.commit()
    
    # Add a new column for Rating
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    conn.commit()
    
    # Update the Rating column with data
    ratings = {
        "To Kill a Mockingbird": 4.8,
        "1984": 4.7,
        "The Great Gatsby": 4.5
    }
    for title, rating in ratings.items():
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
    conn.commit()
    
    # Retrieve and display books sorted by Year_Published in ascending order
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print("\nBooks sorted by Year Published (Ascending):")
    for row in cursor.fetchall():
        print(row)
