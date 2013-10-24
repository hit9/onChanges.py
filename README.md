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

Input String Should Be
-----------------------

The input string's each line should be an available filepath.

Why make this tool
------------------

To auto build when I am saving my source files.
