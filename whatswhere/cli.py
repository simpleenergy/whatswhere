import click

from whatswhere.env_tools import (
    get_deploy_environment_version,
)
from whatswhere.grid import (
    get_grid_cell,
)


@click.command()
@click.option(
    '--pull-requests', '-p', multiple=True, type=click.INT,
)
@click.argument(
    'host', type=(click.STRING, click.STRING, click.STRING)
)
def main(pull_requests, host):
    product, partner, deploy_environment = host
    if pull_requests:
        prefix = ':'.join((product, partner, deploy_environment))
        for pull_request_number in pull_requests:
            version = get_deploy_environment_version(product, partner, deploy_environment)
            is_present = get_grid_cell(product, pull_request_number, version)
            click.echo("#{pr_number} - {prefix} - {is_present}".format(
                pr_number=pull_request_number,
                prefix=prefix,
                is_present=is_present,
            ))
    else:
        assert False
