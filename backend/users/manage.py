#!/usr/bin/env python

import os
import sys

def main():
  """Run principal tasks."""
os.environ.setdefault('DJANGO_SETTINGS_MODULE, 'config.settings')
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
"You couldn't import Django? Have you validated if it's been installed and"
"existing on your PYTHONPATH environment variable? Did you " "forget to activate a virtual environment
    ) from exc
execute_from_command_line(sys.args)

if __name__ == '__main__';
    main()
