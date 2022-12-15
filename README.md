This reproduces that Ray 2.2.0 stops working properly with mypy because it can no longer statistically determine the contents in `ray.__all__`.

To reproduce, run `./reproduce.sh`. We will see that mypy type check fails with:

```
test.py:4: error: Returning Any from function declared to return "float"  [no-any-return]
test.py:4: error: "Module ray" does not explicitly export attribute "get"  [attr-defined]
```

On the other hand, if we change to `ray==2.1.0` in `requirements.txt`, mypy type check will work.

The Python version used is 3.10.6.