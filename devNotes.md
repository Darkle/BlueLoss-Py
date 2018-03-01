https://github.com/klen/pylama#configuration-file



[pylint]
# https://code.visualstudio.com/docs/python/linting#_commandline-arguments-and-configuration-files
# http://pylint-messages.wikidot.com/all-messages
# https://github.com/janjur/readable-pylint-messages/blob/master/README.md
# C0103 - when a name doesn't doesn't fit the naming convention - http://pylint-messages.wikidot.com/messages:c0103
# C0111 - no docstrings in module - http://pylint-messages.wikidot.com/messages:c0111
disable = C0103,C0111

[pycodestyle]
# pycodestyle is pep8 renamed
# https://code.visualstudio.com/docs/python/linting#_commandline-arguments-and-configuration-files
# http://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
# https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes
# E226 - missing whitespace around arithmetic operator
# E302	- expected 2 blank lines, found 0
ignore = E226,E302
