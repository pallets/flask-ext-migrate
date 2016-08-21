import pytest
from redbaron import RedBaron

import flask_ext_migrate as migrate


def test_simple_from_import():
    red = RedBaron("from flask.ext import foo")
    output = migrate.fix_tester(red)
    assert output == "import flask_foo as foo"


def test_non_flask_import_unchanged():
    red = RedBaron("import requests")
    output = migrate.fix_tester(red)
    assert output == "import requests"


def test_base_flask_import_unchanged():
    red = RedBaron("import flask")
    output = migrate.fix_tester(red)
    assert output == "import flask"


def test_base_flask_from_import_unchanged():
    red = RedBaron("from flask import Flask")
    output = migrate.fix_tester(red)
    assert output == "from flask import Flask"


def test_invalid_import_doesnt_raise():
    red = RedBaron("import adjfsjdn")
    try:
        migrate.fix_tester(red)
    except Exception as e:
        pytest.fail(e)


def test_invalid_import_unchanged():
    red = RedBaron("import adjfsjdn")
    output = migrate.fix_tester(red)
    assert output == "import adjfsjdn"


def test_from_to_from_import():
    red = RedBaron("from flask.ext.foo import bar")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import bar"


def test_from_to_from_named_import():
    red = RedBaron("from flask.ext.foo import bar as baz")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import bar as baz"


def test_from_to_from_samename_import():
    red = RedBaron("from flask.ext.foo import bar as bar")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import bar"


def test_from_to_from_samename_subpackages_import():
    red = RedBaron("from flask.ext.foo.bar import baz as baz")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo.bar import baz"


def test_multiple_import():
    red = RedBaron("from flask.ext.foo import bar, foobar, something")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import bar, foobar, something"


def test_multiline_import():
    red = RedBaron("from flask.ext.foo import \
                    bar,\
                    foobar,\
                    something")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import bar, foobar, something"


def test_module_import():
    red = RedBaron("import flask.ext.foo")
    output = migrate.fix_tester(red)
    assert output == "import flask_foo"


def test_named_module_import():
    red = RedBaron("import flask.ext.foo as foobar")
    output = migrate.fix_tester(red)
    assert output == "import flask_foo as foobar"


def test_named_from_import():
    red = RedBaron("from flask.ext.foo import bar as baz")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import bar as baz"


def test_parens_import():
    red = RedBaron("from flask.ext.foo import (bar, foo, foobar)")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo import (bar, foo, foobar)"


def test_from_subpackages_import():
    red = RedBaron("from flask.ext.foo.bar import foobar")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo.bar import foobar"


def test_from_subpackages_named_import():
    red = RedBaron("from flask.ext.foo.bar import foobar as foobaz")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo.bar import foobar as foobaz"


def test_from_subpackages_parens_import():
    red = RedBaron(
        "from flask.ext.foo.bar import (foobar, foobarz, foobarred)"
    )
    output = migrate.fix_tester(red)
    assert output == "from flask_foo.bar import (foobar, foobarz, foobarred)"


def test_multiline_from_subpackages_import():
    red = RedBaron("from flask.ext.foo.bar import (foobar,\
                   foobarz,\
                   foobarred)")
    output = migrate.fix_tester(red)
    assert output == "from flask_foo.bar import (foobar, foobarz, foobarred)"


def test_function_call_migration():
    red = RedBaron("flask.ext.foo(var)")
    output = migrate.fix_tester(red)
    assert output == "flask_foo(var)"


def test_nested_function_call_migration():
    red = RedBaron("import flask.ext.foo\n\n"
                   "flask.ext.foo.bar(var)")
    output = migrate.fix_tester(red)
    assert output == ("import flask_foo\n\n"
                      "flask_foo.bar(var)")
