def check_order_status(status):
    status = status.lower()
    if status == "processing":
        print("Your order is being processed.")
    elif status == "delivered":
        print("Your order has been delivered.")
    elif status == "cancelled":
        print("Your order was cancelled.")
    else:
        print("Invalid status entered.")

status = input("Enter order status (Processing, Delivered, Cancelled): ")
check_order_status(status)
