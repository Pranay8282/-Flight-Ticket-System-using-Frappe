# Airplane Mode App

## ✈️ Overview
The **Airplane Mode App** is a Frappe-based project designed to manage flights, passengers, and ticket bookings efficiently. It provides a structured system for handling airplane schedules, reservations, and airport operations.

## 🚀 Features
- **Flight Management**: Add, update, and track flights with departure and arrival details.
- **Passenger Management**: Maintain records of passengers, their bookings, and flight history.
- **Ticket Booking System**: Assign seats, check-in, and manage ticket statuses (Booked, Checked-In, Boarded).
- **Web View Pages**: Display available flights and allow booking via custom templates.
- **Flight Departure Notification**: Sends system notifications to System Managers 24 hours before flight departure.
- **User Roles & Permissions**: Secure access control with predefined roles:
  - **Airport Authority Personnel**: Manages Airlines, Flights, and Airports.
  - **Fleet Manager**: Maintains airplanes.
  - **Travel Agent**: Books tickets and manages passengers.
  - **Flight Crew Member**: Access to necessary flight details.

## 🛠️ Installation
To install and set up the Airplane Mode App, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Pranay8282/Flight-Ticket-System-using-Frappe.git

# Change directory
cd airplane-mode

# Install the app in your Frappe site
bench get-app airplane_mode
bench --site yoursite install-app airplane_mode

# Migrate and restart the server
bench migrate
bench restart
```

## 🎯 Usage
1. **Create Flights**: Add flights with details like departure, destination, duration, and status.
2. **Manage Passengers**: Register passengers and link them to flights.
3. **Book Tickets**: Issue tickets, assign seats, and track flight details.
4. **Check-In & Boarding**: Change ticket status based on passenger progress.
5. **View Web Pages**: Use `/flights` route to list available flights.

## 📜 API Endpoints
The project includes REST API support for integration. Some available endpoints:

- `GET /api/resource/Airplane Flight` - Retrieve all flights.
- `POST /api/resource/Airplane Ticket` - Book a flight ticket.
- `GET /api/resource/Flight Passenger` - Fetch passenger details.

## 🔧 Configuration
Modify `hooks.py` and `custom_scripts` to customize the application behavior, notifications, and workflows as per your requirements.

## 🛡️ Security & Permissions
- Role-Based Access Control (RBAC) implemented.
- Webhooks can be configured for external system integration.

## 🏗️ Future Enhancements
- Flight status automation based on time.
- Payment gateway integration for online booking.
- Dynamic dashboard with real-time updates.

## 📌 Contributing
Contributions are welcome! Feel free to fork the repo, raise issues, or submit pull requests.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
#### 🌟 Developed with ❤️ using Frappe Framework

