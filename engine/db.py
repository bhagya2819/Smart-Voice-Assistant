import sqlite3

conn = sqlite3.connect("sophia.db")
cursor = conn.cursor()

# Create table if it doesn't exist
# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)


# query = "INSERT INTO sys_command VALUES (null,'onenote', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.lnk')"
# cursor.execute(query)


# conn.commit()
# conn.close()
# Don't forget to close the connection when done

# cursor.execute("""
#     UPDATE sys_command 
#     SET name = 'whatsapp' 
#     WHERE path = 'C:\\Users\\Joshika\\OneDrive\\Desktop\\WhatsApp.lnk'
# """)


# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# # to insert values
# query = "INSERT INTO web_command VALUES (null,'instagram', 'https://instagram.com')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done


# testing module
# query = "onenote"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
# results = cursor.fetchall()
# print(results[0][0])

# cursor.execute("DROP TABLE IF EXISTS web_command")