# CATEGORY FIELD.
CATEGORY_CHOICES = ((1, 'Básico'),
                    (2, 'Intermediário'),
                    (3, 'Avançado'))

# DEPRECATED FIELD.
DEPRECATED_CHOICES = ((0, 'Não'), (1, 'Sim'),)

# TITLE FIELD.
MAX_LENGTH_TITLE = 200

# TIP FIELD.
MAX_LENGTH_TIP = 500

# DEPRECATED FIELD.
IS_NOT_DEPRECATED = 0

# INPUT FIELD.
MAX_LENGTH_INPUT = 1000

# OUTPUT FIELD.
MAX_LENGTH_OUTPUT = 1000

# RESPONSE CODES.
REQUEST_SUCCEEDED = 200

# HACKERRANK API KEY.
HACKERRANK_API_KEY = "hackerrank|632360-1323|ed52e20086d8a64132b05ce42b0ae8b616d45472"

# TIME FIELD.
MAX_LENGTH_TIME = 10

# CODE FIELD.
CODE_NAME = 'code'
MIN_LENGTH_CODE = 10
CODE_SIZE = "You source code must have at least 10 characters."

# INITIAL SUM.
INITIAL_SUM = 0.0

# PROJECT NAME.
PROJECT_NAME = "CodaMais"

# DEFAULT CODE
DEFAULT_CODE = """
#include <stdio.h>
#include <stlib.h>

int main () {

    return 0;
}
                """
