import operator

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import text
from .models import (
    DBSession,
    Thing,
    )

import transaction


def check_eq(letters):
    i = 0
    list_letters = list(letters)
    numbers = ['1','2','3',
                    '4','5','6',
                    '7','8','9']
    for i in range(len(list_letters)):
        if i % 2 == 0 and list_letters[i] not in numbers:
            return False
    return True




@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    try:
        if request.method == 'POST':
            result = str(DBSession.query(Thing).order_by('-id').first().result)
            mark = str(request.POST.getone('button'))
            #sequance = Sequance(pass)
            if mark == '=': 
            #     if check_eq(result) == True: # checking validity of equation. (1+1 no 1++1)
            #         result = eval(result)
            #     else:
            #         result = 'ERROR'
                if str(type(check_eq(result))) == "<class 'int'>":
                    result = eval(result)
                else:
                    result = 'ERROR'

            elif mark == 'C':
                result = ''
                # thing = Thing(result=result) #
                # DBSession.add(adding)
                # transaction.commit()
            else:
                result += mark

            thing = Thing(result=result)
           
     
            DBSession.add(thing)
            transaction.commit()
            
        else:
            result = 0
        dBList = []
        for instance in DBSession.query(Thing).order_by(Thing.id):
            dBList.append([instance.id, instance.result])

    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'result': result, 'dBList': dBList}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_MyProject_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

