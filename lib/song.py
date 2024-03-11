class Song:
    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}


    def __init__(self,name,artist,genre) -> None:

        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        

    @classmethod
    def add_to_genres(cls, genre):
        #check if genre is already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)


    @classmethod
    def add_to_artists(cls, artist):
        #check if artist is already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        #iterate over the genres list and populate a dictionary
        
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls,artist):
        #iterate over the artists list and populate a dictionary
    
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1    

# Create instances of the Song class
song1 = Song("Song 1", "Jay Z", "Rap")
song2 = Song("Song 2", "Eminem", "Rap")
song3 = Song("Song 3", "Jay Z", "Rap")
song4 = Song("Song 4", "Drake", "Hip Hop")
song5 = Song("Song 5", "Eminem", "Rap")

# Access class attributes to verify functionality
print("Total songs count:", Song.count)
print("Artists:", Song.artists)
print("Genres:", Song.genres)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)