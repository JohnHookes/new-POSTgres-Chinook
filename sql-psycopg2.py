import psycopg2

# connect to chinook database

connection = psycopg2.connect(database="chinook")

#build a curser object of the database

cursor = connection.cursor()

#query1 select all records from the artist table
#cursor.execute('SELECT * FROM "Artist"')

#query2 select only name column from the artist table
#cursor.execute('SELECT "Name" FROM "Artist"')

# query3 selct only queen from the artist table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#query4 select only by ArtistId #51 from the artist table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#query5 Select only the albums with artistId #51 from artist table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#query6 select all tracks where the composer is queen from the track table
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

#query7 select all tracks where the composer is Santana from the track table
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Santana"])

#query8 Select all tracks from an unrecorded artist "test"
cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Test"])

# fetch the results (multiple)
results = cursor.fetchall()

#fetch the result(single)
#results = cursor.fetchone()

# close connection
connection.close()

for result in results:
    print(result)

