# eventmgtapi
Event Management API
Description
This Django-based Event Management API is designed for creating and managing events and handling basic ticket purchasing. The project supports role-based access with two roles: Admin and User. The admin can create events and both roles can view events, but only users can purchase tickets. Basic JWT-based authentication is implemented for secure access.

Features
User Registration: Admin and User roles can be registered.
Event Creation (Admin Only): Admins can create events.
Ticket Purchase (User Only): Users can purchase tickets for an event, with real-time validation for available tickets.
Role-Based Access Control: Different endpoints for Admin and User.
JWT Authentication: Secure authentication for users using JWT tokens.
Tech Stack
Django
Django Rest Framework (DRF)
PostgreSQL / MySQL
JWT Authentication (via djangorestframework_simplejwt)
Installation
1. Clone the Repository
bash
Copy code
git clone https://https://github.com/Hi-Uday/eventmgtapi
cd EventAPI
2. Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure the Database
Open EventAPI/settings.py and configure your PostgreSQL or MySQL settings:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',  # for PostgreSQL; for MySQL use '3306'
    }
}
5. Apply Migrations
bash
Copy code
python manage.py migrate
6. Create a Superuser
bash
Copy code
python manage.py createsuperuser
Follow the prompts to create an admin user.

7. Run the Development Server
bash
Copy code
python manage.py runserver
API Endpoints
Authentication
User Registration:
POST /api/register/
Example Request Body:

json
Copy code
{
  "username": "example",
  "password": "password123",
  "role": "admin"  // or "user"
}
Login & JWT Token Generation:
POST /api/token/
Example Request Body:

json
Copy code
{
  "username": "example",
  "password": "password123"
}
Example Response:

json
Copy code
{
  "access": "your_jwt_access_token",
  "refresh": "your_jwt_refresh_token"
}
Event Management (Admin Only)
Create Event:
POST /api/events/
Example Request Body (Admin Only):

json
Copy code
{
  "name": "Music Concert",
  "date": "2024-11-01",
  "total_tickets": 100
}
Required Headers:
Authorization: Bearer <your_jwt_access_token>

List All Events:
GET /api/events/
Accessible by both Admin and Users.

Ticket Purchase (User Only)
Purchase Tickets:
POST /api/events/{id}/purchase/
Example Request Body:
json
Copy code
{
  "quantity": 2
}
Required Headers:
Authorization: Bearer <your_jwt_access_token>
Custom SQL Query
To fetch the top 3 events with the most tickets sold, you can use this SQL query:

sql
Copy code
SELECT id, name, date, total_tickets, tickets_sold
FROM events_event
ORDER BY tickets_sold DESC
LIMIT 3;
Important Considerations
Ticket Purchase Validation: Before completing a ticket purchase, the API checks if the number of tickets requested exceeds the available tickets (tickets_sold + quantity > total_tickets). If so, an error message is returned.

JWT-Based Authentication: Only authenticated users can access API endpoints. Ensure to pass the Authorization: Bearer <token> header in requests.

Testing the API
You can use tools like Postman or cURL to test the API endpoints.

Future Enhancements
Extend the API to support event updates and deletion (Admin only).
Add additional role-based permission levels (e.g., event organizers).
Implement a frontend for the API using React or another JavaScript framework.
