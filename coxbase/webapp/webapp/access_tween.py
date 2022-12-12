from pyramid.settings import asbool
import uuid
from sqlalchemy.sql import insert
from datetime import datetime
from webapp import models

def access_tween_factory(handler, registry):
    print("up here")
    if asbool(registry.settings.get('do_stats')):
        print("here")
        # if statistics support is enabled, return a wrapper
        def save_request_props_tween(request):
            date = datetime.now()
            formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
            submission_dict = {
                "ID": uuid.uuid4().hex,
                "view_name": request.path,
                "user_ip": request.remote_addr}
            try:
                response = handler(request)
            finally:
                session = request.db2_session
                session.execute(insert(models.accessTable).values([submission_dict]))
                session.commit()
            return response

        return save_request_props_tween

    # if statistics support is not enabled, return the original

    # handler

    return handler
