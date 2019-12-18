#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from .. import models
from pyramid.response import Response
import pandas as pd
import numpy as np
import os
import uuid
import shutil
import json
from pathlib2 import Path
import pyfastcopy
from Bio import pairwise2, SeqIO
import subprocess
import bcrypt

class SecurityProcessor():
 
    @staticmethod
    def checkstatus(request):
        if request.authenticated_userid:
            status = "Log out"
            route = 'logout'
            return {'status': status, 'route': route}


    @staticmethod
    def hash_password(passwrd):
        hashed = bcrypt.hashpw(passwrd.encode('utf8'), bcrypt.gensalt())
        return hashed.decode('utf8')

    @staticmethod
    def check_password(passwrd, hashed):
        expected_hash = hashed.encode('utf8')
        return bcrypt.checkpw(passwrd.encode('utf8'), expected_hash)
