from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#Executing the instructions from our localhost chinook database
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key =True),
    Column("Name", String)
)

#Creating variable for "album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"),)
)

#create variable for Track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),
)


#Making the connection
with db.connect() as connection:
    #query1 select all records from the artist table
    #select_query = artist_table.select()

    #query2 select only name column from the artist table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query3 selct only queen from the artist table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    #query4 select only by ArtistId #51 from the artist table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    #query5 Select only the albums with artistId #51 from artist table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    #query6 select all tracks where the composer is queen from the track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")


    results = connection.execute(select_query)
    for result in results:
        print(result)
