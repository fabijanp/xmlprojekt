from mutagen.flac import FLAC
import xml.etree.ElementTree as ET
import os

tree = ET.parse('muzika.xml')
root = tree.getroot()

def main(audio):
    artist_ime = audio['ARTIST']
    album_ime = audio['ALBUM']

    for artist in root.findall('artist'):
        current = artist.get('name')
        if(current in artist_ime):
            for album in artist.findall('album'):
                current = album.get('title')
                if(current in album_ime):
                    zanr = album.find('genre').get('genrecat')
                    audio.tags['genre'] = zanr
                    print('naso')
                    break
    audio.save()

for filename in os.listdir():
    if filename.endswith('.flac'):
        print(filename)
        audio = FLAC(filename)
        main(audio)
