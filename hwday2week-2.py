# Problem #1


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
# Adding new category called "Beverages" with at least two items
restaurant_menu["Beverages"] = {}
beverages = restaurant_menu["Beverages"]
beverages["Cold drinks"] = {"Sodas": 2.99}
beverages["Hot drinks"] = {"Coffee": 2.25}

print(restaurant_menu)

# updating price of steak from 15.99 to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

# removing "Bruschetta" from "Starters"
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)




# Problem 2
# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. 
# You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# example service_tickets = {
#    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.


class Ticket:
    ticket_counter = 0

    def __init__(self, customer_name, issue_description):
        Ticket.ticket_counter += 1
        self.ticket_id = f"Ticket{Ticket.ticket_counter:03}"
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.status = "Open"

    def update_status(self, new_status):
        self.status = new_status

class TicketingSystem:

    def __init__(self):
        self.tickets = []
    
    # def generate_ticket_id(self):
    #     ticket_id = f"Ticket{self.ticket_id_counter:03}"
    #     self.ticket_id_counter += 1
    #     return ticket_id

    def open_new_ticket(self, customer_name, issue_description):
        ticket = Ticket(customer_name, issue_description)
        self.tickets.append(ticket)

    def update_ticket_status(self, ticket_id, new_status):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.update_status(new_status)
                return True
        return False

    def display_tickets(self, status=None):
        if status:
            filtered_tickets = [ticket for ticket in self.tickets if ticket.status == status]
            if filtered_tickets:
                for ticket in filtered_tickets:
                    print(f"{ticket.ticket_id}: Customer Name: {ticket.customer_name}, Issue Description: {ticket.issue_description}, Status: {ticket.status}")
            else:
                print("No tickets with the specified status.")
        else:
            for ticket in self.tickets:
                print(f"{ticket.ticket_id}, Customer Name: {ticket.customer_name}, Issue Description: {ticket.issue_description}, Status: {ticket.status}")


ticket_system = TicketingSystem()

print('''  ______     ___       __       __      
 /      |   /   \     |  |     |  |     
|  ,----'  /  ^  \    |  |     |  |     
|  |      /  /_\  \   |  |     |  |     
|  `----./  _____  \  |  `----.|  `----.
 \______/__/     \__\ |_______||_______|
                                        
  ______  _______ .__   __. .___________. _______ .______      
 /      ||   ____||  \ |  | |           ||   ____||   _  \     
|  ,----'|  |__   |   \|  | `---|  |----`|  |__   |  |_)  |    
|  |     |   __|  |  . `  |     |  |     |   __|  |      /     
|  `----.|  |____ |  |\   |     |  |     |  |____ |  |\  \----.
 \______||_______||__| \__|     |__|     |_______|| _| `._____|
                                                               ''')

while True:
    print("\n1. Open a new ticket")
    print("2. Update ticket status")
    print("3. Display all tickets")
    print("4. Display tickets by status")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_name = input("Enter customer name: ")
        issue_description = input("Enter issue description: ")
        ticket_system.open_new_ticket(customer_name, issue_description)
        print("Ticket opened successfully!")

    elif choice == "2":
        ticket_id = input("Enter ticket ID: "))         #changed input into int 
        new_status = input("Enter new status (Open/Closed): ")
        if ticket_system.update_ticket_status(ticket_id, new_status):
            print("Ticket status updated successfully!")
        else:
            print("Ticket not found.")

    elif choice == "3":
        ticket_system.display_tickets()

    elif choice == "4":
        status_filter = input("Enter status to filter by (Open/Closed): ")
        ticket_system.display_tickets(status_filter)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

