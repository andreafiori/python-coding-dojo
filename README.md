# 🐍 Python Coding Dojo

![CI](https://img.shields.io/badge/tests-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.x-blue)
![TDD](https://img.shields.io/badge/methodology-TDD-purple)

A **Test‑Driven Development (TDD) playground** for Python.

This repository contains a growing collection of **small, focused programming problems (katas)** implemented with **clean, readable code** and backed by **comprehensive automated tests**. The goal is not just to solve problems, but to practice **thinking in tests**, refactoring safely, and applying Python best practices.

## 🎯 Goals

* Practice **TDD** in Python (red → green → refactor)
* Improve **problem‑solving and algorithmic thinking**
* Write **clean, maintainable, well‑tested code**
* Serve as a **reference repository** for Python idioms, testing, and tooling

## 📦 What You’ll Find Here

* Generic programming problems (algorithms, strings, collections, data structures, etc.)
* Each kata includes:

  * a clear and minimal implementation
  * one or more unit tests
* Strong focus on:

  * correctness
  * readability
  * refactoring
  * test coverage
  * static analysis

This is intentionally **not** a competitive‑programming repository: clarity beats cleverness.

## 🗂 Project Structure

```text
src/
  python_algorithms
    algorithms/
    strings/
    ...

tests/
  algorithms/
  strings/
  ...
```

* `src/` contains production code
* `tests/` mirrors the same structure and contains all unit tests

## 🛠 Requirements

* **Python** ≥ 3.x
* **pip**

### Recommended Tools

* [pytest](https://docs.pytest.org/) – test runner
* [coverage](https://coverage.readthedocs.io/) – code coverage
* [pytest-cov](https://pytest-cov.readthedocs.io/) – coverage integration for pytest
* [pylint](https://pylint.org/) – static code analysis

---

## 🚀 Getting Started

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Update dependencies

```bash
python  -m pip install -r requirements.txt --upgrade
```

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Stop after the first failure:

```bash
pytest -x
```

Run a single test file:

```bash
pytest tests/algorithms/strings/test_stringutil.py
```

Run test from a venv:

```bash
.\.venv\Scripts\python.exe -m pytest
```

## 📊 Code Coverage

Run code coverage:

```bash
coverage run --source=src -m pytest
coverage report
```

Generate an HTML report:

```bash
coverage html
```

### Using pytest-cov (recommended)

`pytest-cov` also reports files without tests:

```bash
pytest --cov=src tests/
pytest --cov=src tests/ --cov-report=html
```

### Run tests and update coverage

```bash
pytest --cov=your_package --cov-report=term-missing --cov-report=html
```

## 🔍 Static Analysis (pylint)

Run pylint on source and tests (ignoring missing docstrings):

```bash
pylint src --disable=missing-docstring
pylint tests --disable=missing-docstring
```

## 📦 Managing Dependencies

Update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## 🧠 Philosophy

> Make it work. Make it right. Make it simple.

Every exercise starts with a failing test and evolves through refactoring. If you’re learning Python, improving your design skills, or sharpening your TDD mindset, this dojo is for you.

## Algorithms

* [Backtracking](./src/python_algorithms/algorithms/backtracking/README.md)

## Resources & Inspiration

* [Python Algorithms](https://github.com/TheAlgorithms/Python)
* [Python data structures and algorithms](https://github.com/shushrutsharma/Data-Structures-and-Algorithms-Python)
* [Project Euler github](https://www.freecodecamp.org/learn/project-euler/#project-euler-problems-1-to-100)
* [Python best practices on Real Python](https://realpython.com/tutorials/best-practices/)
* [Leetcode problems](https://leetcode.com/problemset/)
* [Algo Monster](https://algo.monster/)
* [Algo Expert](https://www.algoexpert.io/)
