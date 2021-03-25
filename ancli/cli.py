import click


class Config(object):

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory


@cli.command()
@click.option('--string', default='Hello world',
              help='string to print.')
@click.option('--repeat', default=1, type=int,
              help='Number of times to print.')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
@pass_config
def say(config, string, repeat, out):
    """
    This script runs the command line interface.
    """
    if config.verbose:
        click.echo('we are in verbose')
    click.echo(out)
    click.echo(config.home_directory)
    for i in range(repeat):
        click.echo(string, file=out)
