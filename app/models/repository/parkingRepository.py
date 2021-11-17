from app import db
from app.models.tables import Establishment, EstablishmentDetails, ParkingRating, ParkingService, Service
from sqlalchemy.orm import aliased

class ParkingRepository:

    def getAllParkings(self):
        return db.session.query(Establishment,EstablishmentDetails,ParkingRating
        ).join(EstablishmentDetails, EstablishmentDetails.fk_establishments == Establishment.id_establishment
        ).join(ParkingRating,ParkingRating.fk_establishments == Establishment.id_establishment
        ).all()
    
    def getAllParkingsByIdParking(self,id):
        return db.session.query(Establishment,EstablishmentDetails,ParkingRating
    ).filter_by(id_establishment = id).join(EstablishmentDetails, EstablishmentDetails.fk_establishments == Establishment.id_establishment
    ).join(ParkingRating,ParkingRating.fk_establishments == Establishment.id_establishment
    ).all()

    def returnToJson(self, result):
            parkings = []
            for x in result:
                y = {
                        'id': x.Establishment.id_establishment,
                        'name': x.Establishment.name,
                        'hour_price': x.EstablishmentDetails.hour_value,
                        'monthly_price': x.EstablishmentDetails.monthly_lease_value,
                        'user_avaliation': x.ParkingRating.rating,
                        'address': x.Establishment.address,
                        'reference_point': x.Establishment.reference_point,
                        'image_url': '../../assets/images/teste.png',
                        'monthly': x.EstablishmentDetails.ic_monthly_lease,
                        'available_vacancies': x.EstablishmentDetails.num_vacancies,
                        'services_available': ""
                    }
               
                parkings.append(y)
            return parkings