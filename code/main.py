import cli
import config
import sys
sys.path.append("../tests/")

import tests
''' Start up'''
obj = cli.CLI()
the = obj.cli(obj.the)
config.settings = the

if the["eg"] != "nothing":
    tests.runs(the["eg"])
exit(tests.fails)
