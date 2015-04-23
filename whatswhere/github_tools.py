import ConfigParser

import config

import github


def get_api_token():
    try:
        return config.cp.get('global', 'github_api_token')
    except ConfigParser.NoSectionError:
        raise ValueError('Config file is missing the required `global` section')
    except ConfigParser.NoOptionError:
        raise ValueError(
            'Config file is missing the required `github_api_token` in the '
            '`global` section'
        )


def get_github_repo_name(product):
    try:
        return config.cp.get(product, 'github_repo_name')
    except ConfigParser.NoSectionError:
        raise ValueError('No section found for product: `{0}`'.format(product))
    except ConfigParser.NoOptionError:
        raise ValueError(
            'Configuration section for product: `{0}` is missing the '
            '`git_hub_repo_name` option'
        )


def get_recent_closed_pull_request_numbers(product):
    client = github.Github(get_api_token())
    repository = client.get_repo(get_github_repo_name(product))
    return tuple((pr.number for pr in repository.get_pulls(state='closed')[:10]))


def get_pull_request(product, number):
    client = github.Github(get_api_token())
    repository = client.get_repo(get_github_repo_name(product))
    return repository.get_pull(number)
