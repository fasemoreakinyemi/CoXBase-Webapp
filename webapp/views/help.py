from pyramid.view import view_config
from sqlalchemy.sql import insert
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
)
from pyramid.httpexceptions import HTTPBadRequest
from pathlib2 import Path
import pandas as pd
import subprocess
import os
import uuid
import shutil
import json


@view_config(route_name="help", renderer="../templates/help.jinja2")
def help_page(request):
    return {}
