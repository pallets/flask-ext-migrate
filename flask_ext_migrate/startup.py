import click

from . import fix


@click.command()
@click.argument('input_file', required=True)
def startup(input_file):
    fix(input_file)
