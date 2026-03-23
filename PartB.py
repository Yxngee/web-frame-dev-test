import unittest
from PartA import Artist, Song, Album, Playlist
class TestMusicPlaylist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Taylor Swift", "13-12-1989", "USA")
        self.song1 = Song("Blank Space", "Taylor Swift", 2014)
        self.song2 = Song("Style", "Taylor Swift", 2014)
        self.song3 = Song("Shake It Off", "Taylor Swift", 2014)
        self.album = Album("1989", "Taylor Swift", 2014)
        self.playlist = Playlist("My Playlist")
        
        
    def test_artist_instance(self):
        self.assertIsInstance(self.artist, Artist)

    def test_song_instance(self):
        self.assertIsInstance(self.song1, Song)

    def test_album_instance(self):
        self.assertIsInstance(self.album, Album)

    def test_playlist_instance(self):
        self.assertIsInstance(self.playlist, Playlist)
        
        
    def test_artist_not_song(self):
        self.assertNotIsInstance(self.artist, Song)

    def test_song_not_album(self):
        self.assertNotIsInstance(self.song1, Album)

    def test_album_not_playlist(self):
        self.assertNotIsInstance(self.album, Playlist)

    def test_playlist_not_artist(self):
        self.assertNotIsInstance(self.playlist, Artist)
        
        
    def test_identical_objects(self):
        another_reference = self.song1
        self.assertIs(self.song1, another_reference)

    def test_unidentical_but_similar_objects(self):
        another_song = Song("Blank Space", "Taylor Swift", 2014)
        self.assertIsNot(self.song1, another_song)
        self.assertEqual(self.song1.song_title, another_song.song_title)
        self.assertEqual(self.song1.artist_name, another_song.artist_name)
        self.assertEqual(self.song1.year_of_release, another_song.year_of_release)
        
        
    def test_album_add_song(self):
        self.album.add_song("Wildest Dreams", 2014)
        self.assertEqual(len(self.album.songs), 1)
        self.assertEqual(self.album.songs[0].song_title, "Wildest Dreams")

    def test_artist_add_album(self):
        self.artist.add_album(self.album)
        self.assertEqual(len(self.artist.albums), 1)

    def test_artist_add_song(self):
        self.artist.add_song(self.song1)
        self.assertEqual(len(self.artist.songs), 1)

    def test_playlist_add_song(self):
        self.playlist.add_song(self.song1)
        self.assertEqual(len(self.playlist.songs), 1)
        
        
    def test_sort_playlist_ascending(self):
        self.playlist.add_song(self.song3)
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.sort_playlist("ASC")
        titles = [song.song_title for song in self.playlist.songs]
        self.assertEqual(titles, ["Blank Space", "Shake It Off", "Style"])

    def test_sort_playlist_descending(self):
        self.playlist.add_song(self.song3)
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.sort_playlist("DES")
        titles = [song.song_title for song in self.playlist.songs]
        self.assertEqual(titles, ["Style", "Shake It Off", "Blank Space"])

    def test_shuffle_playlist(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song3)

        before_shuffle = sorted([song.song_title for song in self.playlist.songs])
        self.playlist.shuffle_playlist()
        after_shuffle = sorted([song.song_title for song in self.playlist.songs])

        self.assertEqual(before_shuffle, after_shuffle)
        
        
if __name__ == "__main__":
    unittest.main()
    