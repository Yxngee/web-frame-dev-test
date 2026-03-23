import random
class Artist:
    def __init__(self, name, dob, country, albums=None, songs=None):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = albums if albums is not None else []
        self.songs = songs if songs is not None else []

    def display_info(self):
        print("Artist Information")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Country: {self.country}")
        print(f"Albums: {[album.album_title for album in self.albums]}")
        print(f"Songs: {[song.song_title for song in self.songs]}")
        print()

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)
class Song:
    def __init__(self, song_title, artist_name, year_of_release):
        self.song_title = song_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release

    def display_info(self):
        print("Song Information")
        print(f"Song Title: {self.song_title}")
        print(f"Artist Name: {self.artist_name}")
        print(f"Year of Release: {self.year_of_release}")
        print()
class Album:
    def __init__(self, album_title, artist_name, year_of_release, songs=None):
        self.album_title = album_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        self.songs = songs if songs is not None else []

    def display_info(self):
        print("Album Information")
        print(f"Album Title: {self.album_title}")
        print(f"Artist Name: {self.artist_name}")
        print(f"Year of Release: {self.year_of_release}")
        print(f"Songs: {[song.song_title for song in self.songs]}")
        print()

    def add_song(self, title, release_year):
        new_song = Song(title, self.artist_name, release_year)
        self.songs.append(new_song)
        return new_song
class Playlist:
    def __init__(self, playlist_title, songs=None):
        self.playlist_title = playlist_title
        self.songs = songs if songs is not None else []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print(f"Playlist: {self.playlist_title}")
        for song in self.songs:
            print(f"{song.song_title} - {song.artist_name} ({song.year_of_release})")
        print()

    def sort_playlist(self, order='ASC'):
        reverse_order = True if order == 'DES' else False
        self.songs.sort(key=lambda song: song.song_title.lower(), reverse=reverse_order)

    def shuffle_playlist(self):
        random.shuffle(self.songs)
if __name__ == "__main__":
    artist = Artist("Taylor Swift", "13-12-1989", "USA")

    album = Album("1989", "Taylor Swift", 2014)

    song1 = Song("Blank Space", "Taylor Swift", 2014)
    song2 = Song("Style", "Taylor Swift", 2014)
    song3 = Song("Shake It Off", "Taylor Swift", 2014)

    album_song1 = album.add_song("Wildest Dreams", 2014)
    album_song2 = album.add_song("Bad Blood", 2014)

    album.songs.append(song1)
    album.songs.append(song2)
    album.songs.append(song3)

    artist.add_album(album)
    artist.add_song(song1)
    artist.add_song(song2)
    artist.add_song(song3)
    artist.add_song(album_song1)
    artist.add_song(album_song2)

    artist.display_info()
    album.display_info()
    song1.display_info()

    playlist = Playlist("My Favourite Playlist")

    for song in album.songs:
        playlist.add_song(song)

    playlist.print_all_song()

    playlist.sort_playlist("ASC")
    print("Sorted ASC:")
    playlist.print_all_song()

    playlist.sort_playlist("DES")
    print("Sorted DES:")
    playlist.print_all_song()

    playlist.shuffle_playlist()
    print("Shuffled Playlist:")
    playlist.print_all_song()
    
        