======
README
======

Introduction
------------

**AFRO** is **A**\ nother **F**\ ree **R**\ ipping **O**\ rchestra

Requirements
------------

Afro is designed to run on Python version 2 and depends on the following python modules:

- `Mutagen <http://code.google.com/p/mutagen>`_
- `PyYaml <http://pyyaml.org/>`_
- `Musicbrainz2 <http://musicbrainz.org/doc/python-musicbrainz2>`_

Theses dependencies can be installed with pip using the requirements.txt file. 

.. code-block:: bash

    $ pip install -r requirements.txt

It also need some external softwares:

- `cdparanoia <http://xiph.org/paranoia>`_
- `flac <http://flac.sourceforge.net/>`_
- `vorbis-tools <http://www.vorbis.com/>`_
- `lame <http://lame.sourceforge.net/>`_

It's tested to be working on MacOSX and Linux.

Basic Usage
-----------

#. Show entries found in MusicBrainz's database for the inserted CD:
 
.. code-block:: bash

    $ afro list
 
#. Get more informations for an entry:
 
.. code-block:: bash

    $ afro info 1
 
#. Rip a CD using the informations from an entry:
 `
.. code-block:: bash

    $ afro rip 1

Usefull options
---------------

- Edit retrieved by MusicBrainz informations
 
.. code-block:: bash

    $ afro rip 1 --edit
 
- Select a profile

.. code-block:: bash

    $ afro rip 1 --profile mp3

