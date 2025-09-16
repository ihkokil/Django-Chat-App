# Django Chat App

A real-time chat application built with Django. This project includes user authentication (registration and login), private messaging, and user profile management.

## Features

* **User Authentication:** Users can create an account, log in, and log out.
* **Private Messaging:** Logged-in users can send and receive private messages from other users.
* **User Profiles:** Users can view and edit their profiles.
* **Admin Panel:** An admin user can manage users and messages.

## Screenshots

| Login Page                                     | Register Page                                      |
| ---------------------------------------------- | -------------------------------------------------- |
|           |            |
| **Chat Page** | **Profile Page** |
|  |  |

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* pip

### Installation and Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ihkokil/Django-Chat-App.git
    cd Django-Chat-App
    ```

2.  **Create and activate a virtual environment:**
    * **On macOS and Linux:**
        ```sh
        python3 -m venv env
        source env/bin/activate
        ```
    * **On Windows:**
        ```sh
        python -m venv env
        .\env\Scripts\activate
        ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file. See the section below.)*

4.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at http://127.0.0.1:8000/.

## Demo Credentials

### Admin User

  * **Username:** Admin
  * **Password:** Demo1234

### Demo Users

1.    * **Username:** iqbal
      * **Password:** Demo1234
2.    * **Username:** khan
      * **Password:** Demo1234

## Connect with me

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40'\>](https://www.linkedin.com/in/ihkokil/)