import requests
from requests.exceptions import ConnectionError

from whatswhere import config


def get_environment_info_from_config_parser(cp):
    environments = {}
    for section in cp.sections():
        product, _, partner = section.partition(':')

        if not product or not partner:
            continue

        environments.setdefault(product, {})

        environments[product][partner] = {
            deploy_environment: url for deploy_environment, url in cp.items(section)
        }
    return environments


def parse_status_text(status_text):
    _, _, version = status_text.partition('.')
    return version


def get_deploy_environment_version(product, partner, deploy_environment):
    environment_info = get_environment_info_from_config_parser(config.cp)

    url = environment_info[product][partner][deploy_environment]

    try:
        status_text = requests.get(url, verify=False).content
    except ConnectionError:
        return '?'
    else:
        version = parse_status_text(status_text)
        return version


def get_environment_version_info(product):
    responses = []
    environment_info = get_environment_info_from_config_parser(config.cp)
    for partner, environments in environment_info[product].items():
        for environment in environments:
            key = "{partner}.{environment}".format(partner=partner, environment=environment)
            version = get_deploy_environment_version(product, partner, environment)
            responses.append((key, version))

    return tuple(responses)
