from mutagen.flac import FLAC
import xml.etree.ElementTree as ET
import os

tree = ET.parse('muzika.xml')
root = tree.getroot()

for filename in os.listdir():
    if filename.endswith('.flac'):
        audio = FLAC(filename)
        artist_ime = str(audio.tags['artist'])
        artist_ime = artist_ime.replace("['", "")
        artist_ime = artist_ime.replace("']", "")
        print(artist_ime)
        artist_found = False
        album_found = False
        album_ime = str(audio.tags['album'])
        album_ime = album_ime.replace("']", "")
        album_ime = album_ime.replace("['", "")
        for artist in root.findall('artist'):
            current = artist.get('name')
            if(current in artist_ime):
                artist_found = True
                for album in artist.findall('album'):
                    current2 = album.get('title')
                    if(current2 in album_ime):
                        album_found = True
                if (album_found == False):
                    novi = ET.SubElement(artist, 'album', title=str(album_ime))
                    ET.SubElement(novi, 'genre', genrecat='')
                    tree.write('muzika.xml')
        if(artist_found == False):
             artist = ET.SubElement(root, 'artist', name=str(artist_ime))
             novi = ET.SubElement(artist, 'album', title=str(album_ime))
             ET.SubElement(novi, 'genre', genrecat='')
             tree.write('muzika.xml')
