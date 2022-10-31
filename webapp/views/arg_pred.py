from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPNotAcceptable
from pyramid.httpexceptions import HTTPBadRequest
import uuid
from webapp import views_processor
from webapp import tasks
import time


@view_config(route_name="arg_pred_api")
def argpred_view(request):
    start = time.time()
    print("start: {}".format(start))
    process_ID = uuid.uuid4().hex
    VP = views_processor.ViewProcessor()
    if "fastafile" in request.POST:
        inputfile = request.POST["fastafile"].file
        file_path = VP.create_file_from_fastafile(inputfile, process_ID, "sole")
    else:
        if "fastaentry" in request.POST:
            sequence = memoryview(request.POST["fastaentry"].encode("utf-8"))
            file_path = VP.create_file_from_fastaentry(sequence, process_ID)
        else:
            raise HTTPNotFound()

    end_file_write = time.time()
    end_1 = end_file_write - start
    print("file_write_duration: {}".format(end_1))
    task = tasks.arg_pred_task.apply_async([process_ID,
                                            file_path],
                                     task_id=process_ID)
    url = request.route_url("res_arg_pred_page", ID=task.id)
    end = time.time()
    end_2 = end - start
    print("duration: {}".format(end_2))
    return HTTPFound(location=url)


@view_config(route_name="res_arg_pred_page",
            renderer="../templates/arg_pred_res_page.jinja2")
def res_argpred_page_view(request):
    task_id = request.matchdict["ID"]
    return {"task_id":task_id}

@view_config(route_name="res_arg_pred",
            renderer="json")
def res_argpred_status_view(request):
    task_id = request.matchdict["ID"]
    task = tasks.arg_pred_task.AsyncResult(task_id)
    response = {
            'state': task.state
        }
    return response
