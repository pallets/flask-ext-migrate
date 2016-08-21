import os

import click

from . import fix


@click.command()
@click.argument('input_source', required=True)
def startup(input_source):
    if os.path.isdir(input_source):
        files_to_fix = get_source_files(input_source)
    elif os.path.isfile(input_source):
        files_to_fix = [input_source]
    else:
        raise click.UsageError(
            'You must provide a valid filename or directory.'
        )

    for filepath in files_to_fix:
        fix(filepath)


def get_source_files(directory):
    filepaths = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py'):
                filepaths.append(os.path.join(root, filename))

    return filepaths
