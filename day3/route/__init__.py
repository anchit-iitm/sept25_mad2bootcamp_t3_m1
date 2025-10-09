from flask import Blueprint

app_api = Blueprint('test_api', __name__)


from .test1 import *
from .test2 import *
from .test3 import *
