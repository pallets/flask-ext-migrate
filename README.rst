flask_ext_migrate: import migration tool
=========================

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
    usage: flask_ext_migrate [OPTIONS] INPUT_FILE

    A source code migration tool for converting extension imports.
    --------------------------------------------------------------------------
    https://github.com/pocoo/flask-ext-migrate

    required arguments:
      <INPUT_FILE>   The file to be modified

    optional arguments:
      --help         Show this help message and exit

For example to convert the imports in a file `app.py` use the command line:

.. code-block:: bash

    $ flask_ext_migrate app.py

