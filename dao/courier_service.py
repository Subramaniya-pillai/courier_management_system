from entity.courier import Courier

class CourierService:
    def add_courier(self, courier: Courier):
        """Add a new courier to the database"""
        pass

    def track_courier(self, tracking_number: str) -> Courier:
        """Fetch courier details by tracking number"""
        pass

    def update_status(self, courier_id: int, status: str):
        """Update the status of a courier"""
        pass

    def delete_courier(self, courier_id: int):
        """Delete a courier from the database"""
        pass
