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

https://github.com/Subramaniya-pillai/courier_management_system/blob/2e321419144b55c4cca05937c1e0e73fdaccd3f8/program-TASK1/image.png
