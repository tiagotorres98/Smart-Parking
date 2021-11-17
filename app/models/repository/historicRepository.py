from app import db
from app.models.tables import Establishment, Rent

class HistoricRepository:

        def getHistoricByIdUser(self,id):
            return db.session.query(Rent,Establishment
            ).filter_by(fk_user = id
            ).join(Establishment,Establishment.id_establishment == Rent.fk_establishments
            ).all()
        
        def returnToJson(self, result):
            historic = []
            for x in result:
                y = {
                    'parking_name': x.Establishment.name, 
                    'date': x.Rent.scheduling_date.strftime("%d/%m/%Y"), 
                    'price': x.Rent.hourly_value, 
                    'timeIn' : x.Rent.entry_time.strftime("%H:%M:%S"), 
                    'timeOut' : x.Rent.exit_time.strftime("%H:%M:%S")
                }
                historic.append(y)
            return historic