import sqlite3

# Connect to the SQLite database
with sqlite3.connect("roster.db") as conn:
    cursor = conn.cursor()
    
    # Create the Roster table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)
    
    # Insert initial character data
    characters = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)
    conn.commit()
    
    # Update the name of Jadzia Dax to Ezri Dax
    cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
    conn.commit()
    
    # Retrieve and display Bajoran characters
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    print("Bajoran Characters:")
    for row in cursor.fetchall():
        print(row)
    
    # Delete characters older than 100 years
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    conn.commit()
    
    # Add a new column for Rank
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    conn.commit()
    
    # Update the Rank column with data
    ranks = {
        "Benjamin Sisko": "Captain",
        "Ezri Dax": "Lieutenant",
        "Kira Nerys": "Major"
    }
    for name, rank in ranks.items():
        cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
    conn.commit()
    
    # Retrieve and display characters sorted by Age in descending order
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("\nCharacters sorted by Age (Descending):")
    for row in cursor.fetchall():
        print(row)
