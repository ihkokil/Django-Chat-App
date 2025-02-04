# Simple Chat System using Django

![Python](https://img.shields.io/badge/Python-3.9.1-blue) ![Django](https://img.shields.io/badge/Django-3.2.3-green) ![License](https://img.shields.io/badge/License-Free%20for%20Educational%20Use-orange)

A simple chat web application built using Python and Django. This project demonstrates the basic functionality of a chat system, including user authentication, real-time messaging, and user management. It is designed to help new programmers understand how to implement a chat system using Django.

---

## Features

- **User Authentication**: Login and registration pages for user management.
- **User List**: Displays all registered users in the chatbox.
- **Conversation Box**: Allows users to chat with each other.
- **Real-Time Messaging**: Automatically loads new messages in the active conversation.
- **Profile Page**: Displays user profile information.
- **Responsive Design**: Built with Bootstrap for a clean and responsive UI.

---

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, JavaScript (jQuery, Ajax), Bootstrap
- **Database**: SQLite

---

## How to Run the Project

### Prerequisites

Before running the project, ensure you have the following installed:

- **Python** (v3.9.1 or higher)
- **Django** (v3.2.3 or higher)
- **PIP** (for installing Python modules)

### Installation Steps

1. **Download the Source Code**:
   - Download and extract the provided source code zip file.

2. **Navigate to the Project Directory**:
   - Open your terminal or command prompt.
   - Change the working directory to the extracted source code folder:
     ```bash
     cd path/to/extracted/folder
     ```

3. **Install Required Dependencies**:
   - Run the following commands to install Django and other required libraries:
     ```bash
     pip install Django
     pip install django-crispy-forms
     ```

4. **Set Up the Database**:
   - Run the following command to apply migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the Development Server**:
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```

6. **Access the Application**:
   - Open your web browser and navigate to:
     ```
     http://localhost:8000/ or http://127.0.0.1:8000/
     ```

---

## Access Information

### SuperUser (Admin)
- **Username**: `admin`
- **Password**: `admin123`

### Sample User 1
- **Username**: `jsmith`
- **Password**: `test12345`

### Sample User 2
- **Username**: `cblake`
- **Password**: `test12345`

---

## Notes

- This project is for **educational purposes only**.
- Feel free to modify and extend the source code as needed.
- If you encounter any missing modules, install them using `pip`.

---

## License

This project is free to use for educational purposes. The source code is provided as-is, without any warranties.

---

## Acknowledgments

- Developed by **Md. Iqbal Haider Khan**.
- Submitted on **February 2, 2025**.

---

Enjoy exploring the Simple Chat System! If you have any questions or feedback, feel free to reach out.
