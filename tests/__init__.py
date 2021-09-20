import sys
import os

tests_dir = os.path.dirname(os.path.abspath(__file__))
top_level = os.path.dirname(tests_dir)

# append the top level so plyanging module can be imported.
# also append the tests dir so test_lib can be found.
# There may be some unusual side-affects doing this if a dev
# installs the plyanging source with pip and is trying to test it.
# I'm not sure. But for the minute, this is probably ok.
sys.path.append(tests_dir)
sys.path.append(top_level)
