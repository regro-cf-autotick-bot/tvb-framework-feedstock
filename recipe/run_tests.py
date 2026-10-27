import os
import sys

import pytest
import tvb.tests.framework.adapters.creators as creators_tests

# --ignore-glob is resolved against the CWD, which differs from the install prefix in conda-build,
# so compute the real installed paths of the tests that need siibra (not available on conda-forge).
tests_dir = os.path.dirname(creators_tests.__file__)
ignored = [os.path.join(tests_dir, name) for name in ("siibra_base_test.py", "siibra_creator_test.py")]

args = ["--pyargs", "tvb.tests.framework",
        "-k", "not (TestNetworkxImporter and test_import)"]
args += ["--ignore=" + path for path in ignored]

sys.exit(pytest.main(args))
