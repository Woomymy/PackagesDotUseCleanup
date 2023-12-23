# Packages.use cleanup

[![Python package](https://img.shields.io/github/actions/workflow/status/Woomymy/PackagesDotUseCleanup/pylint.yml?branch=main&style=for-the-badge)](https://github.com/Woomymy/PackagesDotUseCleanup/actions/workflows/pylint.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

Little python script to cleanup /etc/portage/package.use

- [Usage](#usage)

## Usage

```bash
# Redirect new uses to "newuses" file
./cleanup.py /etc/portage/package.use > newuses
# This will remove uninstalled packages uses and print them to stderr
```

