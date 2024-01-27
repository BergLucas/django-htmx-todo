#!/usr/bin/env python
"""django_htmx_todo command-line utility for administrative tasks."""

try:
    from django_htmx_todo import main
except ImportError as exc:
    raise ImportError(
        "Couldn't import django_htmx_todo. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc

if __name__ == "__main__":
    main()
