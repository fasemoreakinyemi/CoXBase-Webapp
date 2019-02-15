#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.request import Request
from pyramid.decorator import reify

class MyRequest(Request):
    "override the pyramid request object to add explicit db session handling"

    @reify
    def db1_session(self):
        "returns the db_session at start of request lifecycle"
        # register callback to close the session automatically after
        # everything else in request lifecycle is done
        self.add_finished_callback( self.close_dbs_1 )
        return self.registry.db1_factory.get_session()

    @reify
    def db2_session(self):
        self.add_finished_callback( self.close_dbs_2 )
        return self.registry.db2_factory.get_session()

    def close_dbs_1(self, request):
        request.db1_session.close()

    def close_dbs_2(self, request):
        request.db2_session.close()
