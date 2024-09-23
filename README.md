# Friend Store using Flask and React

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

This project is a **Friend Store** web application, where users can manage their list of friends. Built with Flask on the backend and React on the frontend, the application offers an intuitive UI, full CRUD functionality, and a responsive design. It supports both light and dark modes for a personalized user experience.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Contributing](#contributing)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Overview

The **Friend Store** is a web-based platform that allows users to add, update, delete, and view their list of friends. This project demonstrates the integration of Flask for server-side logic with React for the front-end interface. SQLite is used for database management, and Chakra UI enhances the interface with a sleek design.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Key Features

- **Add, Edit, and Delete Friends**: Full CRUD functionality for managing a list of friends.
- **User Authentication**: Secure login and registration system.
- **Responsive UI**: Fully responsive design, working seamlessly on mobile, tablet, and desktop devices.
- **Light/Dark Mode**: Switch between light and dark themes for a personalized experience.
- **SQLite Database**: Efficiently store and manage data using SQLite with SQLAlchemy for ORM.
- **RESTful API**: Implements a RESTful API for smooth data communication between the front-end and back-end.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Technologies Used

- **Python** (Flask, SQLAlchemy)
- **React** (JavaScript)
- **Chakra UI** (UI framework)
- **SQLite** (Database)
- **Jinja2** (Template engine for Flask)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Installation and Setup

To run this project locally, follow the steps below:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/friend-store.git
   cd friend-store
   ```
   
2. **Set up the backend (Flask)**:

  ```bash
  cd backend
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

3. **Set up the frontend (React)**:

  ```bash
  cd ../frontend
  npm install
  npm run build
  ```

4. **Create the SQLite database**:

  ```bash
  flask shell
  >>> from app import db
  >>> db.create_all()
  ```

5. **Run the Flask application**:

  ```bash
  flask run
  ```

6. **Access the application**:
  Open your browser and navigate to http://localhost:5000/ to view the Friend Store.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Usage

- **Homepage**: View the list of friends.
- **Add Friend**: Add a new friend to the store.
- **Edit Friend**: Update details of an existing friend.
- **Delete Friend**: Remove a friend from the list.
- **Switch Mode**: Toggle between light and dark mode for the user interface.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## Contributing

Contributions to this project are welcome! Feel free to submit bug fixes or suggest improvements via pull requests.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)
