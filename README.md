# Practical Python Programming (David Beazley)

This is a fork of https://github.com/dabeaz-course/practical-python and is my work through the [Practical Python Programming](https://dabeaz-course.github.io/practical-python/) course by David Beazley. I'm trying to take a TDD approach as I also use this opportunity to learn [pytest](https://docs.pytest.org/en/latest/). Thankfully David provides verbatim output for most of the examples in the course, so I can copy and paste that into my test assertions.

## Progress

You can see my progress here: [https://github.com/dabeaz-course/practical-python/compare/master...kavun:dabeaz-practical-python:master](https://github.com/dabeaz-course/practical-python/compare/master...kavun:dabeaz-practical-python:master)

## Setup

I've also created a small Powershell script to create a venv and run tests. It's usage looks like this:

```powershell
cd Work
.\work.ps1 venv
```

This will create a venv in the current directory and install pytest using `requirements.txt` and `pip`.

Then you can run the tests like this:

```powershell
.\work.ps1 test:watch
```
