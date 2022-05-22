!da program radi potrebno je instalirati mutagen (pip install mutagen)!

Program omogucuje brzo i prakticno mjenjanje "genre" metapodatka vece kolicine .flac file-ova

"xmlprojektCREATE" uzima sve .flac file-ove koji su u istom folderu kao i on, koristeci njihove
metapodatke u "muzika.xml" file dodaje nove elemente "<artist>" sa atributom "name" u kojem je
upisano ime umjetnika, zatim njegov child element "<album>" sa atributom "title" i tom elementu
na kraju dodaje child self-closing element "<genre>" sa atributom "genrecat" koji je prazan

korisnik zatim moze samostalno u "muzika.xml" file u prazan "genrecat" atribut upisat zeljeno 
ime zanra

"xmlprojektEDIT" zatim cita sve .flac file-ove koji su u istom folderu kao i on, usporeduje
njihove metapodatke sa ovima u "muzika.xml" i ako pronade da pjesma iz .flac file-a pripada
nekom od albuma sa "muzika.xml" liste, uzima ono napisano u "genrecat" atributu i promjeni
metapodatak "genre" tog .flac file-a

(za provjeru metapodatka .flac file-a -> desni klik -> properties -> details)