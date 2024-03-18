class Song:
    all = []
    count = 0

    def __init__(self, name, genre, artist):
        self.name = name
        self.genre = genre
        self.artist = artist
        Song.all.append(self)
        Song.count += 1
        
    
    def __repr__(self):
        return f"<{self.name}>"

    @classmethod
    def genre_count(cls):
        genres = {}
        # loop through songs in Song.all
        for song in Song.all:
            if song.genre in genres:
                genres[song.genre] += 1
            else:
                genres[song.genre] = 1
        # returns {"Rap": 5, "Rock": 1, "Country": 3} - genre as key and number of songs as value
        return genres

    @classmethod 
    def artist_count(cls):
        artists = {}
        # return the number of songs each artist is responsible for
        for song in Song.all:
            if song.artist in artists:
                artists[song.artist] += 1
            else:
                artists[song.artist] = 1
        return artists
