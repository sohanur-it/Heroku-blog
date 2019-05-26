DEV = True # just change it to False when pushing to heroku

if DEV:
    from .local import *
else:
    from .heroku import *
