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
from pyramid.security import (
    remember,
    forget,
    )
from sqlalchemy.exc import DBAPIError
import uuid
from .. import models
from .. import security

SP = security.SecurityProcessor()
@view_config(route_name='login', renderer='../templates/login.jinja2')
def login_view(request):
    message = ""
    if 'submit' in request.params:
        username = request.params['username']
        password = request.params['password']
        query = request.db2_session.query(models.UserTable).filter(
                    models.UserTable.username == username).first()

        if query:
             hashed_pw = request.db2_session.query(models.UserTable.password).filter(
                models.UserTable.username == username).first()
             if SP.check_password(password, ''.join(hashed_pw)):
                headers = remember(request, username)
                return HTTPFound(location=request.route_url('home'),
                                 headers=headers)
             return {'message': "Failed login: Wrong password", 'username': username, 'status': 'Log in', 'route': 'login'}
        message = "login failed"
        return {'message': "Failed login: Unregistered user", 'username': username, 'status': "Log in", 'route': 'login'}
    return {'status': "Log in", 'route': 'login'}

@view_config(route_name='logout')
def logout(request):
        headers = forget(request)
        url = request.route_url('home')
        return HTTPFound(location=url,
                         headers=headers)
