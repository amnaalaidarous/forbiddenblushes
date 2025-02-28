# Enum for ServiceType and Status
from enum import Enum

# Enum for different types of delivery services
class ServiceType(Enum):
    EXPRESS = "Express"
    STANDARD = "Standard"
    SAME_DAY = "Same Day"

# Enum for possible status of the order or service
class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

# Enum for different currencies used for payment
class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    AED = "AED"

# Enum for different payment methods
class Method(Enum):
    CREDIT_CARD = "Credit Card"
    PAYPAL = "PayPal"
    CASH = "Cash"


# Customer Class to store customer information
class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self.customer_id = customer_id  # Unique customer identifier
        self.name = name  # Name of the customer
        self.email = email  # Email address of the customer
        self.phone = phone  # Phone number of the customer
        self.address = address  # Address of the customer

    # Setters and Getters for customer attributes
    def setCustomerID(self, customer_id):
        self.customer_id = customer_id

    def getCustomerID(self):
        return self.customer_id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def placeOrder(self, order):
   # Returns a confirmation message for the placed order.
        return f"Placed Order for: {order.getOrderID()}"


    # Method to display customer information
    def displayCustomerInfo(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"


# DeliveryAdmin Class to store information about the delivery administrator
class DeliveryAdmin:
    def __init__(self, admin_id, provider, service_type, status, location):
        self.admin_id = admin_id  # Unique admin identifier
        self.provider = provider  # Delivery service provider
        self.service_type = service_type  # Type of service (Express, Standard, etc.)
        self.status = status  # Current status of the order
        self.location = location  # Location of the delivery admin

    # Setters and Getters for admin attributes
    def setAdminID(self, admin_id):
        self.admin_id = admin_id

    def getAdminID(self):
        return self.admin_id

    def setProvider(self, provider):
        self.provider = provider

    def getProvider(self):
        return self.provider

    def setServiceType(self, service_type):
        self.service_type = service_type

    def getServiceType(self):
        return self.service_type

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    # Method to display admin information
    def displayAdminInfo(self):
        return f"Admin ID: {self.admin_id}, Provider: {self.provider}, Service Type: {self.service_type}, Status: {self.status}, Location: {self.location}"


# Order Class to store information about orders
class Order:
    def __init__(self, order_id, items, quantity, package_weight, description):
        self.order_id = order_id  # Unique order identifier
        self.items = items  # Items included in the order
        self.quantity = quantity  # Quantity of items
        self.package_weight = package_weight  # Weight of the package
        self.description = description  # Description of the items

    # Setters and Getters for order attributes
    def setOrderID(self, order_id):
        self.order_id = order_id

    def getOrderID(self):
        return self.order_id

    def setItems(self, items):
        self.items = items

    def getItems(self):
        return self.items

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity

    def setPackageWeight(self, package_weight):
        self.package_weight = package_weight

    def getPackageWeight(self):
        return self.package_weight

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    # Method to display order information
    def displayOrderInfo(self):
        return f"Order ID: {self.order_id}, Items: {self.items}, Quantity: {self.quantity}, Package Weight: {self.package_weight}, Description: {self.description}"


# DeliveryStaff Class to store information about delivery staff
class DeliveryStaff:
    def __init__(self, staff_id, delivery_method, return_item, pick_up, drop_off):
        self.staff_id = staff_id  # Unique staff identifier
        self.delivery_method = delivery_method  # Method of delivery (e.g., Courier)
        self.return_item = return_item  # Whether item will be returned
        self.pick_up = pick_up  # Pickup location
        self.drop_off = drop_off  # Drop off location

    # Setters and Getters for staff attributes
    def setStaffID(self, staff_id):
        self.staff_id = staff_id

    def getStaffID(self):
        return self.staff_id

    def setDeliveryMethod(self, delivery_method):
        self.delivery_method = delivery_method

    def getDeliveryMethod(self):
        return self.delivery_method

    def setReturnItem(self, return_item):
        self.return_item = return_item

    def getReturnItem(self):
        return self.return_item

    def setPickUp(self, pick_up):
        self.pick_up = pick_up

    def getPickUp(self):
        return self.pick_up

    def setDropOff(self, drop_off):
        self.drop_off = drop_off

    def getDropOff(self):
        return self.drop_off

    # Method to display staff information
    def displayStaffInfo(self):
        return f"Staff ID: {self.staff_id}, Delivery Method: {self.delivery_method}, Return Item: {self.return_item}, Pick Up: {self.pick_up}, Drop Off: {self.drop_off}"


# Payment Class to handle payment information
class Payment:
    def __init__(self, payment_id, currency, method, total_price, payment_status):
        self.payment_id = payment_id  # Unique payment identifier
        self.currency = currency  # Currency used in payment
        self.method = method  # Payment method (Credit Card, PayPal, etc.)
        self.total_price = round(total_price, 2)  # Total price (rounded to 2 decimal places)
        self.payment_status = payment_status  # Payment status (Completed, Cancelled, etc.)

    # Setters and Getters for payment attributes
    def setPaymentID(self, payment_id):
        self.payment_id = payment_id

    def getPaymentID(self):
        return self.payment_id

    def setCurrency(self, currency):
        self.currency = currency

    def getCurrency(self):
        return self.currency

    def setMethod(self, method):
        self.method = method

    def getMethod(self):
        return self.method

    def setTotalPrice(self, total_price):
        self.total_price = round(total_price, 2)

    def getTotalPrice(self):
        return self.total_price

    def setPaymentStatus(self, payment_status):
        self.payment_status = payment_status

    def getPaymentStatus(self):
        return self.payment_status

    # Method to cancel payment
    def cancelPayment(self):
        self.payment_status = "Cancelled"
        return "Payment has been cancelled."

    # Method to display payment information
    def displayPaymentInfo(self):
        return f"Payment ID: {self.payment_id}, Currency: {self.currency}, Method: {self.method}, Total Price: {self.total_price}, Payment Status: {self.payment_status}"


# Object 1 - Customer, Admin, Order, Delivery Staff, Payment Information
if __name__ == "__main__":
    # Create object for each class for first customer
    customer = Customer("C123", "Amna Ibrahim", "amna@gmail.com", 1234567890, "Al Kayr St")
    delivery_admin = DeliveryAdmin("A123", "Aramex", ServiceType.EXPRESS, Status.PENDING, "Warehouse A")
    order = Order("O123", "Laptop", 1, 2.5, "Gaming Laptop")
    delivery_staff = DeliveryStaff("S123", "Courier", "Laptop", "Al Kayr St", "Al Saada St")
    payment = Payment("P123", Currency.AED, Method.CREDIT_CARD, 100.506, "Completed")

    # Display all information for the first customer
    print('Delivery Management System')
    print('Thank you For Using Our Delivery Service')
    print('  ')
    print('  ')
    print('Object 1 / Customer 1')
    print('  ')
    print(customer.displayCustomerInfo())
    print(delivery_admin.displayAdminInfo())
    print(order.displayOrderInfo())
    print(delivery_staff.displayStaffInfo())
    print(payment.displayPaymentInfo())

 # Object 2 - Customer, Admin, Order, Delivery Staff
if __name__ == "__main__":
    # Create object for each class for a new customer and their details
    customer2 = Customer("C124", "Mariam Ibrahim", "mariam@gmail.com", 9876543210, "Al bait St")
    delivery_admin2 = DeliveryAdmin("A124", "DHL", ServiceType.STANDARD, Status.IN_PROGRESS, "Warehouse B")
    order2 = Order("O124", "Smartphone", 2, 1.2, "Latest Model Smartphone")
    delivery_staff2 = DeliveryStaff("S124", "Standard Shipping", "Smartphone", "Al bait St", "Al salon St")
    payment2 = Payment("P124", Currency.USD, Method.PAYPAL, 250.75, "Completed")

    # Display all information for the second set of objects
    print('  ')
    print('  ')
    print('Object 2 / Customer 2')
    print('  ')
    print(customer2.displayCustomerInfo())
    print(delivery_admin2.displayAdminInfo())
    print(order2.displayOrderInfo())
    print(delivery_staff2.displayStaffInfo())
    print(payment2.displayPaymentInfo())
