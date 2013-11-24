
==========
Quickstart
==========

Installation
------------

The easiest way to install **AFRO** is to use `pip <https://pypi.python.org/pypi/pip>`_.
All dependencies will be installed automatically.
You just have to ensure that you have the external softwares (cdparanoia and at least one audio encoders).

.. code-block:: bash

    $ pip install afro


Basic Usage
-----------

#. Show entries found in MusicBrainz's database for the inserted CD:
 
.. code-block:: bash

    $ afro list
 
#. Get more informations for an entry:
 
.. code-block:: bash

    $ afro info 1
 
#. Rip a CD using the informations from an entry:

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

