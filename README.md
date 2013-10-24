onChanges
---------

Watch given files and run certain command on changes.

Usage
-----

    onChanges (-r|--run) <command>

Examples
---------

```bash
$ ls . | onChanges --run make
```

and grep out the `c` files:

```bash
$ ls | grep -P ".*\.c$" | onChanges --run make
```

or:

```bash
find . -type f -name "*.c" | onChanges --run make
```

About
-----

The input should be a string, which each line is an available filepath.
