# dummy file
# the actual metadata parser is at line 837 in lLyrics.py

import eyed3


class Parser(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.lyrics = ""

    def parse(self):
        resp = 1
        return "squonky sunky"

    def get_lyrics(self, resp):
        return "squinky squinky"

