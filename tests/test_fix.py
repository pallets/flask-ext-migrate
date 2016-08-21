import pytest

import flask_ext_migrate as migrate


def test_simple_from_import():
    output = migrate.fix_tester("from flask.ext import foo")
    assert output == "import flask_foo as foo"


def test_non_flask_import_unchanged():
    output = migrate.fix_tester("import requests")
    assert output == "import requests"


def test_base_flask_import_unchanged():
    output = migrate.fix_tester("import flask")
    assert output == "import flask"


def test_base_flask_from_import_unchanged():
    output = migrate.fix_tester("from flask import Flask")
    assert output == "from flask import Flask"


def test_invalid_import_doesnt_raise():
    try:
        migrate.fix_tester("import adjfsjdn")
    except Exception as e:
        pytest.fail(e)


def test_invalid_import_unchanged():
    output = migrate.fix_tester("import adjfsjdn")
    assert output == "import adjfsjdn"


def test_from_to_from_import():
    output = migrate.fix_tester("from flask.ext.foo import bar")
    assert output == "from flask_foo import bar"


def test_from_to_from_named_import():
    output = migrate.fix_tester("from flask.ext.foo import bar as baz")
    assert output == "from flask_foo import bar as baz"


def test_from_to_from_samename_import():
    output = migrate.fix_tester("from flask.ext.foo import bar as bar")
    assert output == "from flask_foo import bar"


def test_from_to_from_samename_subpackages_import():
    output = migrate.fix_tester("from flask.ext.foo.bar import baz as baz")
    assert output == "from flask_foo.bar import baz"


def test_multiple_import():
    output = migrate.fix_tester(
        "from flask.ext.foo import bar, foobar, something"
    )
    assert output == "from flask_foo import bar, foobar, something"


def test_multiline_import():
    output = migrate.fix_tester("from flask.ext.foo import \
                                 bar,\
                                 foobar,\
                                 something")
    assert output == "from flask_foo import bar, foobar, something"


def test_module_import():
    output = migrate.fix_tester("import flask.ext.foo")
    assert output == "import flask_foo"


def test_named_module_import():
    output = migrate.fix_tester("import flask.ext.foo as foobar")
    assert output == "import flask_foo as foobar"


def test_named_from_import():
    output = migrate.fix_tester("from flask.ext.foo import bar as baz")
    assert output == "from flask_foo import bar as baz"


def test_parens_import():
    output = migrate.fix_tester("from flask.ext.foo import (bar, foo, foobar)")
    assert output == "from flask_foo import (bar, foo, foobar)"


def test_from_subpackages_import():
    output = migrate.fix_tester("from flask.ext.foo.bar import foobar")
    assert output == "from flask_foo.bar import foobar"


def test_from_subpackages_named_import():
    output = migrate.fix_tester(
        "from flask.ext.foo.bar import foobar as foobaz"
    )
    assert output == "from flask_foo.bar import foobar as foobaz"


def test_from_subpackages_parens_import():
    output = migrate.fix_tester(
        "from flask.ext.foo.bar import (foobar, foobarz, foobarred)"
    )
    assert output == "from flask_foo.bar import (foobar, foobarz, foobarred)"


def test_multiline_from_subpackages_import():
    output = migrate.fix_tester("from flask.ext.foo.bar import (foobar,\
                                 foobarz,\
                                 foobarred)")
    assert output == "from flask_foo.bar import (foobar, foobarz, foobarred)"


def test_function_call_migration():
    output = migrate.fix_tester("flask.ext.foo(var)")
    assert output == "flask_foo(var)"


def test_nested_function_call_migration():
    output = migrate.fix_tester("import flask.ext.foo\n\n"
                                "flask.ext.foo.bar(var)")
    assert output == ("import flask_foo\n\n"
                      "flask_foo.bar(var)")
