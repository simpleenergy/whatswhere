import logging

from whatswhere import config

from whatswhere.local_git import (
    retrieve_git_ref,
)


logger = logging.getLogger(__file__)


def filter_commit_hashes_not_found_in_ref(product, ref, commits,
                                          max_depth=config.MAX_COMMIT_SEARCH_DEPTH):
    """
    Given a string representing a git reference, and an iterable of commits,
    return the commits not found in the history of the reference.
    """
    commit_set = set(commits)
    ref = retrieve_git_ref(product, ref)

    for depth, parent_commit in enumerate(ref.iter_parents()):
        if depth > max_depth:
            break
        elif parent_commit.hexsha in commit_set:
            logger.info("Found %s in the history of %s", parent_commit.hexsha, ref)
            commit_set.remove(parent_commit.hexsha)

        if not commit_set:
            logger.info(
                "Found all of %s in the history of %s",
                repr((c[:7] for c in commits)),
                ref,
            )
            break

    if commit_set:
        logger.info(
            "Did not find %s in the history of %s",
            repr((c[:7] for c in commit_set)),
            ref,
        )

    return commit_set
