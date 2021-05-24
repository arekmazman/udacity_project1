# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS ;"
user_table_drop = "DROP TABLE IF EXISTS USERS ;"
song_table_drop = "DROP TABLE IF EXISTS SONGS ;"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS ;"
time_table_drop = "DROP TABLE IF EXISTS TIME ;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE SONGPLAYS
(
    songplay_id SERIAL PRIMARY KEY,
    start_time TEXT NOT NULL,
    user_id TEXT NOT NULL,
    level TEXT,
    song_id TEXT,
    artist_id TEXT,
    session_id TEXT,
    location TEXT,
    user_agent TEXT,
    FOREIGN KEY (user_id) REFERENCES USERS(user_id),
    FOREIGN KEY (artist_id) REFERENCES ARTISTS(artist_id),
    FOREIGN KEY (song_id) REFERENCES SONGS(song_id),
    FOREIGN KEY (start_time) REFERENCES time(start_time)
);
""")

user_table_create = ("""
CREATE TABLE USERS
(
    user_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    level TEXT
);
""")

song_table_create = ("""
CREATE TABLE SONGS
(
    song_id TEXT PRIMARY KEY,
    title TEXT,
    artist_id TEXT,
    year int,
    duration float
);
""")

artist_table_create = (""" 
CREATE TABLE ARTISTS
(
    artist_id TEXT PRIMARY KEY,
    name TEXT, 
    location TEXT, 
    latitude TEXT, 
    longitude TEXT
);
""")

time_table_create = (
    """
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY, 
        hour INT NOT NULL, 
        day INT NOT NULL, 
        week INT NOT NULL, 
        month INT NOT NULL, 
        year INT NOT NULL, 
        weekday INT NOT NULL
    );
    """)

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO SONGPLAYS
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO USERS
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE
SET level = EXCLUDED.level;
""")

song_table_insert = ("""  
INSERT INTO SONGS
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO ARTISTS
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = (
    """
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;    
    """)

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id
FROM  songs INNER JOIN artists ON songs.artist_id = artists.artist_id
WHERE songs.title = %s AND artists.name = %s AND songs.duration = '%s'
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]