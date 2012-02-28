README
======

Introduction
------------

**AFRO** is **A**nother **F**lac **R**ipping **O**rchestra

Requirements
------------

Afro is designed to run on Python version 2 and depends on the following python modules:

 - Mutagen: http://code.google.com/p/mutagen/
 - PyYaml: http://pyyaml.org/
 - Musicbrainz2: http://musicbrainz.org/doc/python-musicbrainz2

It also need some external softwares:

 - cdparanoia: http://xiph.org/paranoia/
 - flac: http://flac.sourceforge.net/

It's tested to be working on OSx and Linux.

Basic Usage
-----------

 1. Show entries found in MusicBrainz's database for the inserted CD: `# python afro.py list`
 1. Get more informations for an entry: `# python afro.py info 1`
 1. Rip a CD using the informations from an entry: `# python afro.py rip 1`

