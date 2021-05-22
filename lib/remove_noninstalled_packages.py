"""
Utils for non-installed packages uses removing
"""
# pylint: disable=E0611
# Pylint doesn't detect members of portage correctly
from portage import db, root as portageroot

def remove_noninstalled_packages_uses(packages):
    """
    Remove uninstalled packages from list
    """
    sortedpackages = []
    removed = []
    dbapi = db[portageroot]["vartree"].dbapi
    for package in packages:
        pkgname = package.split(' ')[0]
        if dbapi.cp_list(pkgname):
            sortedpackages.append(package)
        else:
            removed.append(package)

    return (sortedpackages, removed)
