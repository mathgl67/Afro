README
======

Introduction
------------

**AFRO** is **A**nother **F**ree **R**ipping **O**rchestra

Requirements
------------

Afro is designed to run on Python version 2 and depends on the following python modules:

 - Mutagen: http://code.google.com/p/mutagen/
 - PyYaml: http://pyyaml.org/
 - Musicbrainz2: http://musicbrainz.org/doc/python-musicbrainz2

Theses dependencies can be installed with pip using the requirements.txt file. 

`# pip install -r requirements.txt`

It also need some external softwares:

 - cdparanoia: http://xiph.org/paranoia/
 - flac: http://flac.sourceforge.net/
 - vorbis-tools: http://www.vorbis.com/
 - lame: http://lame.sourceforge.net/

It's tested to be working on OSx and Linux.

Basic Usage
-----------

 1. Show entries found in MusicBrainz's database for the inserted CD:
 
 `# afro list`
 
 1. Get more informations for an entry:
 
 `# afro info 1`
 
 1. Rip a CD using the informations from an entry:
 
 `# afro rip 1`

Usefull options
---------------

 - Edit retrieved by MusicBrainz informations
 
  `# afro rip 1 --edit`
 
 - Select a profile
 
  `# afro rip 1 --profile mp3`
