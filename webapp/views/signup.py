#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid_mailer.message import Message
from sqlalchemy.sql import insert
from pyramid.response import Response
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from sqlalchemy.exc import DBAPIError
import uuid
from .. import models
from .. import security
import bcrypt

SP = security.SecurityProcessor()

@view_config(route_name='signup', renderer='../templates/signup.jinja2')
def signup_view(request):
    return {}

@view_config(route_name='register', renderer='json')
def register_form(request):
    mailer = request.mailer
    submissionID = uuid.uuid4().hex
    user_dict = {"ID": submissionID}
    session = request.db2_session
    user_list = ["email", "username"]
    passhash = SP.hash_password(request.POST['password'])
    user_dict['password'] = passhash
    for item in user_list:
        user_dict[item] = request.POST.get(item)
    session.execute(insert(models.UserTable).values([user_dict]))
    session.commit()
    body = "Your registration was succesful you can sign in here http://coxiella.net/webapp/login"
    message = Message(subject="Registration on CoxBase",
              sender="admin@coxiella.net",
              recipients=[request.POST.get('email')],
              body=body)
    mailer.send(message)
    return {'done':'good'}
  #  return {}
 #   return HTTPNotFound()
   # url = request.route_url('succesful')
#    return HTTPFound(location=url)

