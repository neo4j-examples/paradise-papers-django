import ast
import os

from django.core.exceptions import ImproperlyConfigured


def env(key, default=None, required=True):
    """
    Retrieves environment variables and returns Python natives. The (optional)
    default will be returned if the environment variable does not exist.
    """
    try:
        value = os.environ[key]
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        value = value.replace("**newline**", "\n")
        return value
    except KeyError:
        if default or not required:
            return default
        raise ImproperlyConfigured("Missing required environment variable '%s'" % key)

