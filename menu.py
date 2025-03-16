from dao.courier_service_impl import CourierServiceImpl
from entity.courier import Courier

def display_menu():
    service = CourierServiceImpl()

    while True:
        print("\nCourier Management System")
        print("1. Add Courier")
        print("2. Track Courier")
        print("3. Update Courier Status")
        print("4. Delete Courier")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nEnter Courier Details:")
            courier_id = int(input("Courier ID: "))
            sender_name = input("Sender Name: ")
            sender_address = input("Sender Address: ")
            receiver_name = input("Receiver Name: ")
            receiver_address = input("Receiver Address: ")
            weight = float(input("Weight (kg): "))
            status = input("Status (e.g., In Transit, Delivered): ")
            tracking_number = input("Tracking Number: ")
            delivery_date = input("Delivery Date (YYYY-MM-DD): ")

            courier = Courier(
                courier_id=courier_id,
                sender_name=sender_name,
                sender_address=sender_address,
                receiver_name=receiver_name,
                receiver_address=receiver_address,
                weight=weight,
                status=status,
                tracking_number=tracking_number,
                delivery_date=delivery_date
            )

            service.add_courier(courier)
            print("Courier added successfully.")
        
        elif choice == '2':
            tracking_number = input("Enter tracking number: ")
            courier = service.track_courier(tracking_number)
            if courier:
                print(f"Tracking Details - Sender: {courier.sender_name}, Status: {courier.status}")
            else:
                print("Courier not found.")

        elif choice == '3':
            courier_id = int(input("Enter Courier ID to update status: "))
            new_status = input("Enter new status: ")
            service.update_courier_status(courier_id, new_status)
            print("Courier status updated successfully.")

        elif choice == '4':
            courier_id = int(input("Enter Courier ID to delete: "))
            service.delete_courier(courier_id)
            print("Courier deleted successfully.")

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
