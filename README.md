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

    onChanges <command> [-d DIR] [-p PATTERN]
 
Options:

    -d DIR           files directory path [default: .]
    -p PATTERN       filename pattern [default: *]

Examples
---------

```bash
onChanges make -d src -p '*.c'
```

```bash
onChanges 'make html' -d docs -p '*.rst'
```
