# IRD Assignment

## Overview
This repository contains the code for the Islamic Religious Discourse (IRD) assignment. The project aims to develop a web application that handles various aspects of Islamic religious content, including chapters, hadiths, and sections.

## Technology Stack
- **Language**: Python
- **Framework**: Django

## Project Structure
The project is organized into the following directories:
- `app/`: Contains the main application code.
- `templates/`: Holds HTML templates for the web application.
- `static/`: Contains static files like CSS and JavaScript.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/TheReinforce43/ird_assignment.git
   cd ird_assignment
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage
Once the server is running, you can navigate through the application to explore its features related to Islamic religious content.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project does not currently have a specified license. Please check back later for updates.

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/3/)
