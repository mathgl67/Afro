===========
Development
===========

Requirements
------------

- `Sphinx <http://sphinx-doc.org/>`_

.. code-block:: bash

    $ pip install -r requirements_dev.txt

Documentation
-------------

To generate this documentation :

.. code-block:: bash

    $ ./setup.py build_sphinx

Tests
-----

To run the (very limited) test suite :

.. code-block:: bash

    $ ./setup.py test

Release
-------

There is several steps to get a new release published :

- Review the changelog (doc/changelog.rst)
- Increase the version number in the __init__.py file inside the 'afro' module (used by the setup script and the documention).
- Commit with the message "Release x.x.x"
- Create a tag "x.x.x"
- Send everything on GitHub.
- Publish the new version on PyPI
- Generate and send to documentation to PyPi

.. code-block:: bash

    $ vi doc/changelog.rst
    $ vi afro/__init__.py
    $ git add afro/__init__.py
    $ git commit -m "Release x.x.x"
    $ git tag x.x.x
    $ git push
    $ git push --tags
    $ ./setup.py register sdist upload
    $ ./setup.py build_sphinx
    $ ./setup.py upload_doc

