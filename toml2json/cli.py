#!/bin/env python3

"""Convert TOML files to JSON.


USAGE
"""

import json
import toml
import sys
from pathlib import Path

import click


@click.command()
@click.option("-p/-c", "--pretty/--compact")
@click.argument(
    "toml_files",
    nargs=-1,
    required=True,
    type=click.Path(
        exists=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
        allow_dash=True,
    ),
)
def main(toml_files, pretty):
    """Convert TOML_FILE(S) to JSON."""

    if pretty:
        separators = (', ', ': ')
        indent="\t"
    else:
        separators = (',', ':')
        indent=None

    for toml_file in toml_files:

        if toml_file == "-":
            toml_str = sys.stdin.read()

        else:
            with open(toml_file) as file:
                toml_str = file.read()

        json_str = json.dumps(toml.loads(toml_str), indent=indent, separators=separators)

        if toml_file == "-":
            click.echo(json_str)

        else:
            with open(Path(toml_file).with_suffix(".json"), "w") as file:
                file.write(json_str)
