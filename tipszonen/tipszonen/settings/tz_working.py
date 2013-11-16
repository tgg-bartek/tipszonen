

from os.path import abspath, basename, dirname, join, normpath
from sys import path


DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)

red = normpath(join(SITE_ROOT, 'media/uploads'))
print red