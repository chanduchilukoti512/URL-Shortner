Project Overview:
The URL Shortener is a web application that allows users to input long URLs and get shortened versions that are easier to share. The application uses a backend built with FastAPI, a Python framework, to generate a unique short URL for each long URL. Users can also visit the short URL, which will redirect them to the original long URL.

Key Features:
Shorten Long URLs: Users can input a long URL, and the system will generate a shorter version of the URL.
Redirect Functionality: When the user accesses the shortened URL, the application will automatically redirect them to the original long URL.
User-Friendly Interface: The application has a simple and intuitive front-end built using HTML, CSS, and JavaScript to allow users to input URLs and view results.
Database Integration (Optional): The shortened URLs and their corresponding long URLs are stored in a database for permanent storage and retrieval.

Tech Stack:
Backend: FastAPI (Python)
Frontend: HTML, CSS, JavaScript
Database (Optional): SQLite, MongoDB, or any other database to store the URLs (if desired)

How It Works:
The user enters a long URL into a form on the front-end.
The backend generates a unique short URL and stores it in the database (if applicable).
The system returns the shortened URL to the user, which can then be shared.
When someone visits the short URL, the system looks up the original long URL in the database and redirects the user accordingly.
