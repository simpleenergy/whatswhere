import ConfigParser

from whatswhere import config

import git


def get_repo_location(product):
    try:
        return config.cp.get(product, 'git_repo_location')
    except ConfigParser.NoSectionError:
        raise ValueError('No section found for product: `{0}`'.format(product))
    except ConfigParser.NoOptionError:
        raise ValueError(
            'Configuration section for product: `{0}` is missing the '
            '`git_hub_repo_name` option'
        )


def retrieve_git_ref(product, ref):
    repo = git.Repo(get_repo_location(product))
    commit = repo.rev_parse(ref)
    return commit
