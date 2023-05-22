# Online Course Platform

The Online Course Platform is a web application designed and developed by Gyan to provide online learning materials and conduct exams for users. It allows users to access course content, take exams, and view their exam results. This project serves as a practice exercise for building web applications and can be used as a foundation for larger projects.

## Motivation

The motivation behind developing this web app is to create a platform that offers a user-friendly interface for online learning. The app aims to provide a seamless experience for users to access course materials, study at their own pace, and assess their knowledge through interactive exams. By building this app, I wanted to enhance my skills in web development, Django, and front-end technologies while gaining experience for future designing and implementing of full-stack applications.

## Features

- User authentication: Users can create an account, log in, and log out of the platform.
- Course listing: Users can view a list of available courses and select a course to access its lessons and exams.
- Lesson content: Each course contains multiple lessons with detailed content for learning.
- Exam functionality: Users can take exams associated with a course and submit their answers for evaluation.
- Exam results: After completing an exam, users can view their exam results, including a breakdown of correct and incorrect answers.

## Local Development

To run the Online Course Platform on your local environment, follow these steps:

1. Create a virtual environment and activate it:

   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

2. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```shell
   python manage.py migrate
   ```

4. Create a superuser (admin) account:

   ```shell
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```shell
   python manage.py runserver
   ```

6. Access the application in your web browser at `http://localhost:8000/onlinecourse`.

7. Access the Django Admin interface at `http://localhost:8000/admin`.

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap

## Future Enhancements

- User profile management
- Course enrollment and progress tracking
- Interactive quizzes and assignments
- Discussion forums for course-related discussions
- Integration with payment gateways for premium courses
