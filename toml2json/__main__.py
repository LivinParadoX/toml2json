"""DESCRIPTION

USAGE
"""

from importlib import resources

import click

with resources.path("toml2json", "banner.txt") as banner_path:
    with open(banner_path) as f:
        BANNER = f.read()


@click.command()
def main():
    """"""
    click.echo(BANNER)
