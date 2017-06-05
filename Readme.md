https://www.reddit.com/r/dailyprogrammer/comments/6coqwk/20170522_challenge_316_easy_knights_metric/

## How To Use It

Set up a virtual envirnment for Python. Things may have changed since 3 days ago when I started this project, but
here is what I did:

* `pyenv shell 3.6.1`
* `python -m venv env`
* `source env/bin/activate`

After you have the virtualenv working the Makefile has a few commands you may find useful:

* `make deps` will install any python dependencies (not many)
* `make test` will run unit tests against the code

For a demo of the code in action:

`python ./run_it.py`