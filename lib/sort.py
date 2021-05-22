"""
Module for packages sorting
"""
from lib.getpackageslist import clean_packages_list

def sort_packages(packages):
    """
    Sort all packages by category
    """
    packages = clean_packages_list(packages)
    categories = {}
    for package in packages:
        parts = package.split('/')
        if not parts[0] in categories:
            categories[parts[0]] = [parts[1]]
        else:
            categories[parts[0]].append(parts[1])
    filecontent = ""
    for cat in categories:
        filecontent += f"# {cat}\n"
        categories[cat].sort()
        for package in categories[cat]:
            filecontent += f"{cat}/{package}\n"
        filecontent += "\n"

    return filecontent
