flask_ext_migrate: import migration tool
========================================

.. image:: https://img.shields.io/travis/pallets/flask-ext-migrate.svg
    :target: https://travis-ci.org/pallets/flask-ext-migrate
.. image:: https://img.shields.io/pypi/v/flask_ext_migrate.svg
    :target: https://pypi.python.org/pypi/flask_ext_migrate

This package allows for rapid fixing of old style Flask extension imports from 
the format `flask.ext.foo` to `flask_foo`. It also repairs any associated 
function calls. Although this tool has been tested extensively always check 
the output file to ensure correct functionality.

Installation
------------

To install, simply:

.. code-block:: bash

    $ pip install flask_ext_migrate

Usage
-----

::

    $ flask_ext_migrate --help
    usage: flask_ext_migrate <INPUT_SOURCE>

    A source code migration tool for converting extension imports.
    --------------------------------------------------------------------------
    https://github.com/pocoo/flask-ext-migrate

    required arguments:
      <INPUT_SOURCE>     Either a single file or directory to be recursively converted

    optional arguments:
      --help             Show this help message and exit

For example to convert the imports in a file `app.py` use:

.. code-block:: bash

    $ flask_ext_migrate app.py

To convert all imports in all files within the directory `app/` (relative path) use:

.. code-block:: bash

    $ flask_ext_migrate app

    # This also works.
    $ flask_ext_migrate app/
