import click

import flaskext_migrate


@click.command()
@click.argument('input_file',
                required=True)
def startup(input_file):
    flaskext_migrate.run(input_file)
