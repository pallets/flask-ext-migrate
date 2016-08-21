import os

from flask_ext_migrate.startup import startup
import flask_ext_migrate as migrate


def test_single_file_input_runs_without_failures(runner, temp_dir):
    import_line = 'from flask.ext.foo import bar'
    temp_file = os.path.join(temp_dir, 'temp.py')

    with open(temp_file, 'w') as f:
        f.write(import_line)

    result = runner.invoke(startup, [temp_file])
    assert result.exit_code == 0


def test_no_file_arg_fails(runner, temp_dir):
    result = runner.invoke(startup, [])
    assert result.exit_code != 0


def test_single_file_run_modifies_file_properly(runner, temp_dir):
    import_line = 'from flask.ext.foo import bar'
    temp_file = os.path.join(temp_dir, 'temp.py')

    with open(temp_file, 'w') as f:
        f.write(import_line)
    runner.invoke(startup, [temp_file])

    assert open(temp_file, 'r').read() == migrate.fix_tester(import_line)
