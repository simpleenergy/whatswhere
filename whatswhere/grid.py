from git.exc import BadName

from whatswhere.github_tools import (
    get_recent_closed_pull_request_numbers,
    get_pull_request,
)
from whatswhere.env_tools import (
    get_environment_version_info,
)
from whatswhere.utils import (
    filter_commit_hashes_not_found_in_ref
)


def get_grid_cell(product, pull_request_number, version):
    if version == '?':
        return "Unable to connect to host"
    pull_request = get_pull_request(product, pull_request_number)

    pr_commit_hashes = {c.sha for c in pull_request.get_commits()}

    try:
        missing_hashes = filter_commit_hashes_not_found_in_ref(
            product,
            version,
            pr_commit_hashes,
        )
    except BadName:
        return "Unknown Version"

    if missing_hashes:
        return "No"
    else:
        return "Yes"


def get_grid(product):
    pull_request_numbers = get_recent_closed_pull_request_numbers(product)
    environment_version_info = get_environment_version_info(product)

    grid = {
        "column-headers": tuple(('-'.join(i) for i in environment_version_info)),
        "row-headers": tuple(('#{0}'.format(n) for n in pull_request_numbers)),
        "grid-data": tuple((
            tuple((
                get_grid_cell(product, pr_number, env_info[1])
                for env_info in environment_version_info
            )) for pr_number in pull_request_numbers
        ))
    }
    return grid
