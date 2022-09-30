from flask import flash, render_template, redirect, request
from FlaskExercise import app
from datetime import datetime
@app.route('/')
def home():
    log = request.values.get('log_button')
    if log:
        if log.lower()== 'info':
         app.logger.info('%s button pressed at with value of %s', datetime.now(),log)
        elif log.lower() == 'warning':
            app.logger.warning('%s button pressed at with value of %s', datetime.now(),log)
        elif log.lower() == 'error':
         app.logger.error('%s button pressed at with value of %s', datetime.now(),log)
        elif log.lower() == 'critical':
         app.logger.critical('%s button pressed at with value of %s', datetime.now(),log)
    return render_template(
        'index.html',
        log=log
    )