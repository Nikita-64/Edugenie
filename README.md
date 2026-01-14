
# EduGenie
An AI-powered web application designed to automate the creation of structured educational curricula and course materials.

## Live Demo
The application is live and can be accessed here: https://edugenie-qc4r.onrender.com

## Project Overview
This application is a Flask-based web service that leverages the OpenAI GPT-3.5 model to generate academic content. EduGenie allows users to input a course title and instantly receive a complete course objective, sample syllabus, learning outcomes, and assessment methods.

## Technical Implementation
### AI Curricula Generation
The system utilizes the boltiotai wrapper for the OpenAI API to process natural language prompts. It is engineered with specific system roles to ensure the output follows academic standards for syllabus construction and measurable learning objectives.

### Web Interface and Backend
The backend is built with Flask, utilizing a single-route architecture to handle both GET and POST requests. The frontend is integrated using Bootstrap for a responsive, clean user interface, allowing for seamless content rendering and high readability.

### Error Handling and Scalability
The application includes robust exception handling to manage API latency or connection issues. It is configured for deployment on cloud platforms like Render, using environment variables for secure API key management and dynamic port binding.

### Security
All sensitive credentials and API keys are strictly managed through environment variables. This professional standard prevents the exposure of secrets within the version control system and ensures the integrity of the repository.

## Project Structure
app.py: Core application file containing Flask server logic and OpenAI integration.

requirements.txt: Project dependencies including Flask and boltiotai.
