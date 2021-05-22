# Packages.use cleanup

[![Python package](https://github.com/Woomymy/PackagesDotUseCleanup/actions/workflows/pylint.yml/badge.svg)](https://github.com/Woomymy/PackagesDotUseCleanup/actions/workflows/pylint.yml)

Little python script to cleanup /etc/portage/package.use

- [Usage](#usage)
- [Demo](#demo)

## Usage

```bash
# Redirect new uses to "newuses" file
./cleanup.py /etc/portage/package.use > newuses
# This will remove uninstalled packages uses and print them to stderr
```

## Demo

[![asciicast](https://asciinema.org/a/415627.svg)](https://asciinema.org/a/415627)

