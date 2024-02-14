# django_htmx_todo Documentation

- **Developer documentation:** https://github.com/BergLucas/django-htmx-todo/blob/main/docs

## Cloning the project

You can clone the repository using the following command:

```bash
git clone https://github.com/BergLucas/django-htmx-todo.git
```

## Setting up a development environment

### Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [Poetry](https://python-poetry.org/) ~= 1.7
- [Poe the Poet](https://pypi.org/project/poethepoet/) ~= 0.24
- [poetry-bumpversion](https://pypi.org/project/poetry-bumpversion/) ~= 0.3

### Python environment setup

You can setup the Python development environment by running the following command in the project root:

```bash
poetry install
```

### Database setup

You can setup a sqlite development database by running the following command in the project root:

```bash
poetry poe migrate
```

### Execution

You can execute the application in development mode by running the following command in the project root:

```bash
poetry poe dev
```

### Creation of a super user

You can create a super user by running the following command in the project root:

```bash
poetry poe createsuperuser
```

## Setting up a docker development environment

### Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [Poetry](https://python-poetry.org/) ~= 1.7
- [Poe the Poet](https://pypi.org/project/poethepoet/) ~= 0.24
- [poetry-bumpversion](https://pypi.org/project/poetry-bumpversion/) ~= 0.3
- [Docker](https://www.docker.com/) ~= 24.0
- [Docker Compose](https://docs.docker.com/compose/) ~= 2.20

### Python environment setup

You can setup the Python development environment by running the following command in the project root:

```bash
poetry install
```

### Execution

You can execute the application in development mode on docker by running the following command in the project root:

```bash
poetry poe dev-docker
```

### Execution of commands in the development container

You can open the development container terminal by running the following command in the project root:

```bash
poetry poe bash-docker
```

### Creation of a super user

You can create a super user by running the following commands in the project root:

```bash
poetry poe bash-docker
poetry poe createsuperuser
```
