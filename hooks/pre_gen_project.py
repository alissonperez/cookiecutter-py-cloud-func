import re
import sys


NAME_REGEXP = r'^[a-z0-9]+$'

function_name = '{{ cookiecutter.function_name }}'

if not re.match(NAME_REGEXP, function_name):
    print(('ERROR: "{function_name}" is not a valid function name! '
          'Should only contain lowercase letters and numbers.').format(
              function_name=function_name))

    # exits with status 1 to indicate failure
    sys.exit(1)
