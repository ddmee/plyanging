## Study a foreign language with whatever content you want

Bored of traditional tools that have you study a pre-determined content?

Just want to read the news or a new book in a foreign language?

Plyanging is a python tool that automatically translates foreign-language content into your native language. It will read you the content in both your native language and in the foreign language. Learn by assimilation. (Comprehensible input and interesting content to keep you learning.)

## Install

- Clone this repository
- Install python 3.9 on your system
- Install pipenv on the system python 3.9 installation `pip install pipenv`
- Cd into the directory containing this repository
- The run `pipenv install`  (this will setup the virtualenv and install dependencies for this project)

Now you should be ready to run the program. There are two modes at the minute:
- study mode (supply a list of foreign words to study)
- read mode  (supply a foreign text file to read)


Examples:

```
> pipenv run python -m plyanging study .\word.list
> pipenv run python -m plyanging read .\de_prologue.txt
```

Please note, the `word.list` and `de_prologue.txt` are not currently provided in repo.
