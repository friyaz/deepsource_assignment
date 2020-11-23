An AST based checker to raise issues if a function/method has been decorated with `@wraps` decorator from the `functools` standard library.

To test a file, pass the filename as command line argument to `analyzer.py`.

### Example Usage
```
>>> python analyzer.py test.py
test.py:7: @functools.wraps decorator used
test.py:19: @functools.wraps decorator used
test.py:33: @functools.wraps decorator used

>>> python analyzer.py more_tests.py
more_tests.py:4: @functools.wraps decorator used
```

### Useful Resources
* https://docs.python.org/3/library/ast.html
* https://greentreesnakes.readthedocs.io/en/latest/
* https://deepsource.io/blog/introduction-static-code-analysis/
* https://vpyast.appspot.com/
