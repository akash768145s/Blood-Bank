# Blood Bank Management System

## Overview

The Blood Bank Management System helps organize blood donations, donors, and requests. Users can:

- Sign up as donors
- Search for blood donors
- Manage their donor information
- Track blood inventory
- Receive notifications for blood donation requests

## Features

### User Features

1. User Registration, Login, and Logout
2. Profile Management (Update/Delete)
3. Request/Contact for Blood
4. Notification System for Requests
5. Blood Availability Search

### Admin Features

1. Dashboard Overview
2. Blood Bank Inventory Management
3. Edit Blood Donation Details
4. User Management
5. Delete Users/Entries

## Admin Credentials

- Email: admin@bloodbank.com
- Password: admin

## Setup Instructions

### Prerequisites

- Python 3.x installed
- Git (optional, for cloning)

### Installation Steps

1. Clone or download the repository

   ```bash
   git clone [repository-url]
   # or download and extract the ZIP file
   ```

2. Navigate to project directory

   ```bash
   cd Blood-Bank
   ```

3. Create a virtual environment

   ```bash
   # On Windows
   python -m venv env

   # On macOS/Linux
   python3 -m venv env
   ```

4. Activate the virtual environment

   ```bash
   # On Windows PowerShell
   .\env\Scripts\Activate.ps1

   # On Windows Command Prompt
   .\env\Scripts\activate.bat

   # On macOS/Linux
   source env/bin/activate
   ```

5. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

6. Run the server

   ```bash
   # On Windows
   python server.py

   # On macOS/Linux
   python3 server.py
   ```

7. Access the application
   - Open your web browser
   - Go to: http://127.0.0.1:5000/
   - Register as a new user or login with admin credentials

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'flask'**

   - Make sure you've activated the virtual environment
   - Try reinstalling requirements: `pip install -r requirements.txt`

2. **Database Issues**

   - The system will automatically create a new database if none exists
   - If you encounter database errors, delete `database.db` and restart the server

3. **Port Already in Use**
   - If port 5000 is busy, you'll need to kill the existing process or use a different port

### File Structure

```
Blood-Bank/
├── server.py          # Main application file
├── database.db        # SQLite database
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates
├── static/           # Static files (CSS, JS, images)
└── env/              # Virtual environment (created during setup)
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.
