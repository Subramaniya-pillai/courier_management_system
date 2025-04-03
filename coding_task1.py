def check_order_status(order_status):
    if order_status.lower() == "delivered":
        print("The order has been delivered.")
    elif order_status.lower() == "processing":
        print("The order is still being processed.")
    elif order_status.lower() == "cancelled":
        print("The order has been cancelled.")
    else:
        print("Invalid status entered.")

# Example usage
status = input("Enter the order status (Processing, Delivered, Cancelled): ")
check_order_status(status)
