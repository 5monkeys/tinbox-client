import os
import warnings

VERSION = (0, 1, 0, 'beta', 3)


def get_version(version=None):
    """Derives a PEP386-compliant version number from VERSION."""
    if version is None:
        version = VERSION
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return main + sub

__version__ = get_version()


# Set by setup.py when fetching version before installation of dependencies.
TRAK_CLIENT_VERSION_ONLY = os.environ.get('TRAK_CLIENT_VERSION_ONLY')

if TRAK_CLIENT_VERSION_ONLY is None:
    from .client import Trak
else:
    warnings.warn('Environment variable TRAK_CLIENT_VERSION_ONLY is set. '
                  'trak_client.__init__ will not perfom any convenience '
                  'imports.')