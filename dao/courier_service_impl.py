from dao.courier_service import CourierService
from entity.courier import Courier
from util.db_conn_util import get_session
from sqlalchemy.exc import SQLAlchemyError

class CourierServiceImpl(CourierService):
    
    def add_courier(self, courier: Courier):
        session = get_session()
        try:
            session.add(courier)
            session.commit()
            print("Courier added successfully.")
        except SQLAlchemyError as e:
            print(f"Error adding courier: {e}")
            session.rollback()
        finally:
            session.close()

    def track_courier(self, tracking_number: str) -> Courier:
        session = get_session()
        try:
            courier = session.query(Courier).filter_by(tracking_number=tracking_number).first()
            if courier:
                return courier
            else:
                print("Courier not found.")
        except SQLAlchemyError as e:
            print(f"Error tracking courier: {e}")
        finally:
            session.close()

    def update_status(self, courier_id: int, status: str):
        session = get_session()
        try:
            courier = session.query(Courier).filter_by(courier_id=courier_id).first()
            if courier:
                courier.status = status
                session.commit()
                print("Courier status updated successfully.")
            else:
                print("Courier not found.")
        except SQLAlchemyError as e:
            print(f"Error updating status: {e}")
            session.rollback()
        finally:
            session.close()

    def delete_courier(self, courier_id: int):
        session = get_session()
        try:
            courier = session.query(Courier).filter_by(courier_id=courier_id).first()
            if courier:
                session.delete(courier)
                session.commit()
                print("Courier deleted successfully.")
            else:
                print("Courier not found.")
        except SQLAlchemyError as e:
            print(f"Error deleting courier: {e}")
            session.rollback()
        finally:
            session.close()
