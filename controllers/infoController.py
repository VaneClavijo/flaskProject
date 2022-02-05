from App import app
from flask import render_template, session, request, redirect, url_for
from App import db
from models.models import*
from sqlalchemy import or_
from flask import flash
from datetime import datetime
from datetime import timedelta

@app.route('/', methods=['POST', 'GET'])
def info():
    formato1 = '%Y-%m-%dT%H:%M'
    formato2 = '%d-%m-%Y %H:%M'
    today=datetime.now()
    sumN=0
    sumD=0
    busqueda=[]
    busquedaA=[]
    equipos=dict()
    fEquipment=Equipment.query.filter().all()
    for e in fEquipment:
        equipos[e.equipment_id]=e.equipment_name
    filteredAnswer = Borrow.query.filter().all()
    for f in filteredAnswer:
        if f.borrow_state=='DEVUELTO':
            sumD=sumD+(f.borrow_delivery-f.borrow_end).days*5
            answer=dict(borrow_person=f.borrow_person,
                        borrow_start=f.borrow_start,
                        borrow_end=f.borrow_end,
                        borrow_delivery=f.borrow_delivery,
                        borrow_state=f.borrow_state,
                        borrow_equipment=f.borrow_equipment,
                        multa=((f.borrow_delivery-f.borrow_end).days*5))
            busqueda.append(answer)
        else:
            sumN=sumN+(datetime.today().date()-f.borrow_end).days*5
            answer=dict(borrow_person=f.borrow_person,
                        borrow_start=f.borrow_start,
                        borrow_end=f.borrow_end,
                        borrow_delivery=f.borrow_delivery,
                        borrow_state=f.borrow_state,
                        borrow_equipment=f.borrow_equipment,
                        multa=((datetime.today().date()-f.borrow_end).days*5))
            busquedaA.append(answer)
    if request.method == 'POST':
        startDate=request.form['startdate']
        endDate=request.form['enddate']
        filteredAnswer = Borrow.query.filter(Borrow.borrow_end>=startDate,Borrow.borrow_end<=endDate,Borrow.borrow_state=='DEVUELTO').all()
        busqueda=[]
        sumD=0
        for f in filteredAnswer:
            sumD=sumD+(f.borrow_delivery-f.borrow_end).days*5
            answer=dict(borrow_person=f.borrow_person,
                        borrow_start=f.borrow_start,
                        borrow_end=f.borrow_end,
                        borrow_delivery=f.borrow_delivery,
                        borrow_state=f.borrow_state,
                        borrow_equipment=f.borrow_equipment,
                        multa=((f.borrow_delivery-f.borrow_end).days*5))
            busqueda.append(answer)
    imgR='https://apod.nasa.gov/apod/image/2202/MwCenter_MeerKATMunoz_1080.jpg'

    return render_template('info.html',
                            busqueda=busqueda,
                            equipos=equipos,
                            busquedaA=busquedaA,
                            sumN=sumN,
                            sumD=sumD,
                            imgR=imgR)

