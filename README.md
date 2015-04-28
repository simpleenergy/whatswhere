# Whats Where

Attempting to solve the problem of figuring out if a specific pull request has
been deployed to a specific environment.


```bash
$ ww --pull-request 123 --pull-request 456 marketplace se preprod
#123 - product:partner:environment - Yes
#456 - product:partner:environment - No
```

## Installation

You can install `whatswhere` with `pip`.

```bash
$ pip install whatswhere
```

## Configuration

You have to tell whatswhere about your projects with an `rc` file.

```bash
# ~/.whatswhere.rc
[global]
github_api_token=<github-api-token>

[project_slug]
git_repo_location=/local/path/to/git/repo/
github_repo_name=<github_username>/<github_project_name>

[project_slug:partner_a]
dev=https://example.com/status/
prod=https://example.com/status/

[project_slug:partner_b]
dev=https://other-example.com/status/
prod=https://other-example.com/status/
```

Given this config file, you could then run the following command.

```bash
$ ww -p 123 project_slug partner_b prod
#123 - project_slug:partner_b:prod - Yes
```

What happens behind the scenes is.

1. Your config file is parsed looking for a **section** with the name
   `project_slug:partner`, with an **option** of `prod`, in order to find the
   url that can be hit to find out what version is deployed to that host.
2. You config file is parsed looking for a **section** with the name
   `project_slug` with an **option** `github_repo_name`.  The github repo is
   queried for pull request number `123` to find out what commits are contained
   in that pull request.
3. The `git_repo_location` is then used to lookup a tag relating to the version
   found in step 1, and then the history of that version is parsed to see if it
   contains all of the pull request commits.
