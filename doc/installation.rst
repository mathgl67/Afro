============
Installation
============

Requirements
------------

Afro is designed to run on Python version 2 and depends on the following python modules:

- `Mutagen <http://code.google.com/p/mutagen>`_
- `PyYaml <http://pyyaml.org/>`_
- `Musicbrainz2 <http://musicbrainz.org/doc/python-musicbrainz2>`_
- `python-discid <https://python-discid.readthedocs.org>`_

It also need some external softwares:

- `cdparanoia <http://xiph.org/paranoia>`_
- `flac <http://flac.sourceforge.net/>`_
- `vorbis-tools <http://www.vorbis.com/>`_
- `lame <http://lame.sourceforge.net/>`_

It's tested to be working on MacOSX and Linux.

Using PyPI
----------

The easiest way to install **AFRO** is to use `pip <https://pypi.python.org/pypi/pip>`_.
All dependencies will be installed automatically.
You just have to ensure that you have the external softwares (cdparanoia and at least one audio encoders).

.. code-block:: bash

    $ pip install afro

