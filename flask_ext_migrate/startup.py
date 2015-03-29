import click

from . import run


@click.command()
@click.argument('input_file', required=True)
def startup(input_file):
    run(input_file)
