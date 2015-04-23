import os

from ConfigParser import SafeConfigParser

CONFIG_FILE_LOCATION = os.path.expanduser('~/.whatswhere.rc')


cp = SafeConfigParser()
cp.read([CONFIG_FILE_LOCATION])


MAX_COMMIT_SEARCH_DEPTH = 100
