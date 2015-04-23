from ConfigParser import SafeConfigParser

from whatswhere.env_tools import (
    get_environment_info_from_config_parser,
)


def test_getting_environmen_info_from_config_parser():
    cp = SafeConfigParser()
    cp.read(['tests/config_files/test_environment_info_parsing.rc'])

    env_info = get_environment_info_from_config_parser(cp)

    assert set(env_info.keys()) == set(('test_a', 'test_b'))
    test_a_info = env_info['test_a']
    test_b_info = env_info['test_b']

    assert set(test_a_info.keys()) == set(('sub_test_a', 'sub_test_b'))
    assert set(test_b_info.keys()) == set(('sub_test_a',))

    assert set(test_a_info['sub_test_a'].keys()) == set(('dev', 'prod'))
    assert set(test_a_info['sub_test_b'].keys()) == set(('dev', 'prod'))
    assert set(test_b_info['sub_test_a'].keys()) == set(('dev', 'prod'))

    assert test_a_info['sub_test_a']['dev'] == "http://dev.example.com/test_a/sub_test_a/"
    assert test_a_info['sub_test_a']['prod'] == "http://example.com/test_a/sub_test_a/"

    assert test_a_info['sub_test_b']['dev'] == "http://dev.example.com/test_a/sub_test_b/"
    assert test_a_info['sub_test_b']['prod'] == "http://example.com/test_a/sub_test_b/"

    assert test_b_info['sub_test_a']['dev'] == "http://dev.example.com/test_b/sub_test_a/"
    assert test_b_info['sub_test_a']['prod'] == "http://example.com/test_b/sub_test_a/"
