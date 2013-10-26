onChanges
---------

Watch given files and run certain command on changes.

Installation
------------

```
pip install git+git://github.com/hit9/onChanges.py.git
```

Usage
-----

    onChanges (-r|--run) <command> [(-d|--directory) <directory>] [(-p|--pattern) <pattern>]

Examples
---------

```bash
onChanges -r make -d src -p '*.c'
```

```bash
onChanges -r 'make html' -d docs -p '*.rst'
```
