class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1 # counting song attributes
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    # @classmethod
    def add_to_genres(cls):
        if cls.genres.count(cls.genre) == 0:
            cls.genres.append(cls.genre)

    # @classmethod
    def add_to_artists(cls):
        if cls.artists.count(cls.artist) == 0:
            cls.artists.append(cls.artist)

    # @classmethod
    def add_to_genre_count(cls):
        if cls.genre_count.get(cls.genre) == None:
            cls.genre_count[cls.genre] = 1
        else:
            cls.genre_count[cls.genre] += 1

    # @classmethod
    def add_to_artist_count(cls):
        if cls.artist_count.get(cls.artist) == None:
            cls.artist_count[cls.artist] = 1
        else:
            cls.artist_count[cls.artist] += 1