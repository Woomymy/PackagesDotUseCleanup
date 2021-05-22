"""
File for package processing related functions
"""
from lib.remove_noninstalled_packages import remove_noninstalled_packages_uses
from lib.getpackageslist import clean_packages_list
from lib.sort import sort_packages
def process_packages(packages):
    """
    Process packages(sort,cleanup,remove non-installed,...)
    """
    packages = clean_packages_list(packages)
    (packages, removed) = remove_noninstalled_packages_uses(packages)
    packages = sort_packages(packages)
    return (packages, removed)
