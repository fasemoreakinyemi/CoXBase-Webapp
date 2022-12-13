from pyramid_celery import celery_app as app
from webapp import deeparg

@app.task(bind=True)
def arg_pred_task(self, process_id, file_path):
    dp = deeparg.Predict("nucl",
                 process_id,
                 file_path)
    try:
        dp.PSSM_prediction()
    except:
        raise HTTPNotAcceptable()

