
---

# Event Management Dashboard  

*Event Management Dashboard* is a web-based application designed to streamline event planning and management. It enables organizations to create, manage, and track events efficiently, along with their associated attendees and tasks.

---

## 🚀 Features  

### Event Management  
- Perform CRUD operations on events.  
- Display event details including:  
  - Name  
  - Description  
  - Location  
  - Date  
- Calendar View: Visualize all events in a calendar interface.  

### Attendee Management  
- View, add, or remove attendees.  
- Assign attendees to specific events.  

### Task Tracker  
- Manage tasks associated with events.  
- Update task statuses (Pending or Completed).  
- Assign tasks to events and attendees.  
- View task progress in a user-friendly interface.  

### Calendar Integration  
- Visual representation of events using a calendar.  
- Task deadlines tied to specific events and attendees.  

### Responsive Design  
- Works seamlessly on both mobile and desktop devices.  

---

## 🛠 Technology Stack  

### Frontend  
- HTML  
- CSS  
- JavaScript  
- jQuery  
- AJAX  

### Backend  
- Python  
- Django REST Framework (DRF)  

### Database  
- SQLite3 (Django's default database)  

---

## 📖 API Endpoints  

### Event Management API  
- *Create Event:* POST /api/events/  
- *Get All Events:* GET /api/events/  
- *Update Event:* PUT /api/events/{id}/  
- *Delete Event:* DELETE /api/events/{id}/  

### Attendee Management API  
- *Add Attendee:* POST /api/attendees/  
- *Get All Attendees:* GET /api/attendees/  
- *Delete Attendee:* DELETE /api/attendees/{id}/  

### Task Management API  
- *Create Task:* POST /api/tasks/  
- *Get Tasks by Event:* GET /api/tasks/?event_id={event_id}  
- *Update Task Status:* PATCH /api/tasks/{id}/  
- *Delete Task:* DELETE /api/tasks/{id}/  

---

## 🗂 Models  

### Event  
- name: CharField  
- description: TextField  
- location: CharField  
- date: DateField  
- attendees: ManyToManyField (linked to Attendee)  

### Attendee  
- name: CharField  
- email: EmailField  
- assigned_event: ForeignKey (linked to Event, nullable)  

### Task  
- name: CharField  
- deadline: DateField  
- status: CharField (choices: Pending, Completed)  
- event: ForeignKey (linked to Event)  
- assigned_attendee: ForeignKey (linked to Attendee, nullable)  

---

## 📋 Installation and Setup  

Follow the steps below to set up and run the *Event Management Dashboard* application on your local machine:

### 1. Clone the Repository  
Clone the project repository from GitHub to your local system:  
bash
git clone https://github.com/sahanac2004/Event-Management-Dashboardpostman.git
cd Event-Management-Dashboardpostman


### 2. Set Up a Virtual Environment  
Create and activate a virtual environment to manage project dependencies:  
- *For macOS/Linux:*  
  bash
  python -m venv venv
  source venv/bin/activate
  
- *For Windows:*  
  bash
  python -m venv venv
  venv\Scripts\activate
  

### 3. Install Dependencies  
Install the required Python packages using pip:  
bash
pip install -r requirements.txt


### 4. Apply Migrations  
Set up the database by applying migrations:  
bash
python manage.py makemigrations
python manage.py migrate


### 5. Run the Development Server  
Start the Django development server:  
bash
python manage.py runserver


### 6. Access the Application  
Open your browser and navigate to the following URL to access the application:  

http://127.0.0.1:8000


---


## 📂 Usage  

### Event Management Page  
- Add, edit, and delete events.  
- Visualize events on a calendar view.  

### Attendee Management Page  
- View, add, and remove attendees.  
- Assign attendees to specific events.  

### Task Tracker Page  
- View tasks for events.  
- Assign tasks to specific events and attendees.  
- Update task statuses (Pending or Completed).  

### Calendar View  
- Displays events and their associated dates in a calendar format.  
- Allows users to see all upcoming events at a glance.  

---

## 🔧 Backend Integration  

The frontend communicates with the backend using AJAX for seamless user interactions, such as success/error messages during API calls.

---

## 🌟 Future Enhancements  

- Add authentication and user roles (e.g., Admin, Event Manager).  
- Export data to CSV/Excel for reporting.  
- Integrate Google Calendar for real-time synchronization of events.  
- Add support for push notifications for task deadlines.  

---

## 📧 Contact  

For any questions, feedback, or suggestions, feel free to reach out:  
- *Email:* [sahanac629@gmail.com](mailto:sahanac629@gmail.com)  

---
