#!/usr/bin/env python.
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
          "Unable to import Django. Are you certain it's been installed and "
          "accessible on your PYTHONPATH environment variable? Did you "
          "forget to activate a virtual environment?"
        ) from exc
     execute_from_command_line(sys.args) 
         
if __name__ == '__main__':
      main()
