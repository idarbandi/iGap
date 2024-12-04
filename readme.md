# 
██╗ ██████╗  █████╗ ██████╗ 
██║██╔════╝ ██╔══██╗██╔══██╗
██║██║  ███╗███████║██████╔╝
██║██║   ██║██╔══██║██╔═══╝ 
██║╚██████╔╝██║  ██║██║     
╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     

## Revolutionizing Real-Time Communication with Django and React

---

**Author:** idarbandi  
**Email:** [darbandidr99@gmail.com](mailto:darbandidr99@gmail.com)  
**GitHub:** [idarbandi](https://github.com/idarbandi)

---

Welcome to the iGap project! iGap is an innovative platform designed to transform online communication by leveraging the power of Django for backend development and React for frontend development. This project combines real-time chat functionality, robust data management, and advanced security measures to create a seamless and secure user experience.

## 🚀 Key Features

### 1. Real-time WebSocket Chat
The core feature of iGap is its real-time chat functionality, powered by WebSocket connections. The **WebChatConsumer** class handles message reception and broadcasting, ensuring instant communication between users. JWT authentication enhances security by verifying user identities.

### 2. Efficient Data Management
iGap efficiently manages servers, channels, and members using Django's ORM. The **ServerFilter** class allows users to filter servers based on various criteria, improving accessibility and usability. The **ServerSerializer** class ensures dynamic and context-aware serialization of server data.

### 3. Custom Middleware for Security
The custom **JWTAuthMiddleware** enhances security by authenticating WebSocket connections using JWT tokens. This middleware extracts tokens from cookies, verifies them, and attaches authenticated user information to the WebSocket scope.

### 4. Comprehensive Validation
Robust validation functions, such as **validate_icon_image_size** and **validate_image_file_extension**, ensure the integrity of uploaded image files. These functions check for appropriate dimensions and file types, maintaining platform standards.

### 5. Structured Models
iGap includes well-defined models for managing categories, servers, channels, and members. Each model comes with clear attributes and relationships, supporting robust data management and enhancing readability.

### 6. API Documentation
Using **drf_spectacular**, iGap provides comprehensive API documentation. The **extend_schema** decorator defines the responses and parameters for API endpoints, ensuring clear and user-friendly documentation.

## 📈 Conclusion
The iGap project sets a new standard for online interaction platforms by combining real-time communication capabilities, robust data management, advanced security features, and comprehensive validation. This project is a testament to the power of modern web development frameworks and offers a scalable and secure solution for digital communication.

## 🛠️ Get Started
Follow the steps below to set up and run the iGap project on your local machine.

### Prerequisites
- Python 3.7+
- Django 3.2+
- Channels 3.0+
- Node.js and npm (for React)
- PostgreSQL

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/idarbandi/iGap.git
    ```

2. Navigate to the project directory:
    ```bash
    cd iGap
    ```

3. Backend Setup:
    - Create a virtual environment:
      ```bash
      python3 -m venv env
      source env/bin/activate
      ```
    - Install the required packages:
      ```bash
      pip install -r requirements.txt
      ```
    - Set up the database:
      ```bash
      python manage.py migrate
      ```
    - Create a superuser:
      ```bash
      python manage.py createsuperuser
      ```

4. Frontend Setup:
    - Navigate to the frontend directory:
      ```bash
      cd frontend
      ```
    - Install the required packages:
      ```bash
      npm install
      ```
    - Start the React development server:
      ```bash
      npm start
      ```

5. Run the backend server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/` for the Django backend and `http://localhost:3000/` for the React frontend.

### 📖 Usage
To start using the real-time chat functionality, log in with your user credentials and join a chat channel.

### 🤝 Contributions
Contributions are welcome! Please fork the repository and submit a pull request.

### 📜 License
This project is licensed under the MIT License.

---

Happy coding! If you encounter any issues or have any questions, feel free to open an issue or contact me at [darbandidr99@gmail.com](mailto:darbandidr99@gmail.com).
