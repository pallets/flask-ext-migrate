from flask_ext_migrate.startup import startup
import flask_ext_migrate as migrate


def test_single_file_input_runs_without_failures(runner, tmpdir):
    import_line = 'from flask.ext.foo import bar'
    temp_file = tmpdir.join('temp.py')
    temp_file.write(import_line)

    result = runner.invoke(startup, [str(temp_file)])
    assert result.exit_code == 0
    assert temp_file.read() == migrate.fix_tester(import_line)


def test_no_file_arg_fails(runner):
    result = runner.invoke(startup, [])
    assert result.exit_code != 0


def test_single_file_run_modifies_file_properly(runner, tmpdir):
    import_line = 'from flask.ext.foo import bar'
    temp_file = tmpdir.join('temp.py')
    temp_file.write(import_line)

    result = runner.invoke(startup, [str(temp_file)])
    assert result.exit_code == 0
    assert temp_file.read() == migrate.fix_tester(import_line)
