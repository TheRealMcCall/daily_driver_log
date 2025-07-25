
---

# *Daily Driver Log*

![Responsive Mockup](documentation/responsive/responsive_preview.png)

The site can be accessed by this [link](https://daily-driver-log-0742a8bbde1f.herokuapp.com/)

## Contents

* [Project Overview](#project-overview)
* [User Stories](#user-stories)
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Testing](#testing)
* [Acknowledgements](#credits)
---

## Project Overview

Daily Driver Log helps professional or frequent drivers manage their driving hours by:
-   Logging individual trips with start/finish times
-	Automatically calculating trip durations
-	Summing up total daily driving time
-	Alerting when trip or daily limits are exceeded


## User Stories

### Must Have
-	As a first-time user, I want to register and log in so I can access my logs.
-	As a returning user, I want to log trips with start and finish times.
-	As a user, I want to view today’s trips and see total drive time.
-	As a user, I want to edit or delete trips in case I make a mistake.
-	As a user, I want to know if I’ve exceeded my daily or trip time limits.
-	As a user, I want my data to be private and secure (only visible to me).
-	As an admin, I want to view/edit/delete any records from the admin panel.

### Should Have
-	Ability to edit Day Logs.
-	Warning banner or visual cues when over driving limits.
-	Input validation. e.g. Cannot input a trip end time thats before a trip start time unless an overnight trip.

### Could Have (Future Development)
-	Customizable driving time limits per user.
-	Weekly/monthly driving summaries.
-	CSV export of logs.
-	Graphical reports or charts.

## Features

| Feature | Description |
| --- | --- |
|User Authentication| Ability to register, log in, and log out.|
|Create/Edit/Delete Day Logs| Users can manage logs for each driving day.
|Create/Edit/Delete Trips|Each day log supports creating multiple trip entries with time tracking which can be edited or deleted.
|Time Calculations | Trip and daily durations are automatically calculated
|Limit Warnings | User are alerted when a trip exceeds 5.5 hours or the daily driving time exceeds 10 hours
|Mobile Responsive Design | Fully functional across all devices and screen sizes.
|Secure User Access | Only authenticated users can access and manage their own logs.
|Admin Panel Access | Admin users can view and manage all data in Django admin.

## Design

### Workflow Diagram

<details>
<summary>Click here to view the workflow diagram.</summary>

![Workflow Diagram](documentation/workflow_diagram.png)
</details>

### Entity Relationship Diagram

<details>
<summary>Click here to view the entity relationship diagram.</summary>

![Entity Relationship Diagram](documentation/entity_relationship_diagram.png)
</details>

### Wireframes

Click each section to expand and view the wireframe for that page.

<details>
<summary>Home Page Wireframe</summary>

![Home page wireframe](documentation/wireframes/home_page.png)
</details>

<details>
<summary>Register Page Wireframe</summary>

![Register page wireframe](documentation/wireframes/register_page.png)
</details>

<details>
<summary>Login Page Wireframe</summary>

![Login page wireframe](documentation/wireframes/login_page.png)
</details>

<details>
<summary>New Trip Page Wireframe</summary>

![New trip page wireframe](documentation/wireframes/new_trip_page.png)
</details>

<details>
<summary>Day Summary Page Wireframe</summary>

![Day summary page wireframe](documentation/wireframes/day_summary_page.png)
</details>

<details>
<summary>Dashboard Page Wireframe</summary>

![Dashboard page wireframe](documentation/wireframes/dashboard_page.png)
</details>

<details>
<summary>Settings Page Wireframe</summary>

![Dashboard page wireframe](documentation/wireframes/settings_page.png)
</details>

## Technologies Used

- Technologies used to create the site include:

    * [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Used to create the templates.
    * [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - Used for styling of the templates.
    * [Django](https://www.djangoproject.com/) - Framework used.
    * [VSCode](https://code.visualstudio.com/) - IDE Used.
    * [Git](https://www.git-scm.com/) - was used for website version control.
    * [GitHub](https://github.com/) - was used for hosting of the repository.
    * [Markdown](https://en.wikipedia.org/wiki/Markdown) readme formatting
    * [Google Chrome](https://www.google.co.uk/chrome/) browser and testing.


## Deployment

- The Daily Driver Log app is deployed to [Heroku](https://heroku.com/).
- The app can be reached by clicking this [link](https://daily-driver-log-0742a8bbde1f.herokuapp.com/).
- [Github](https://github.com/) was used for version control and repository.

### Local deployment

To run this project locally:

*Note:*
  - This project requires to install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/TheRealMcCall/daily_driver_log).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
`git clone https://github.com/TheRealMcCall/daily_driver_log.git`
--
- Install dependancies:
 `pip3 install -r requirements.txt`

Create a .env file in the toor directory and add:

(Set debug to false for production)

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_postgres_url
```
Apply migrations and create a superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Run the server
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in a browser to view the app.

### Heroku Deployment (Using Code Institute PostgreSQL)

This project was deployed using Heroku and Code Institute’s free PostgreSQL database.

#### Prepare for deployment


  - Add all dependencies to ```requirements.txt```:
      ```
      pip3 freeze > requirements.txt
      ```

  - Add the following to ```settings.py```:
      ```
      import dj_database_url DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
      ```
  - Set DEBUG = False for production and add your heroku app URL to ``ALLOWED_HOSTS``:
      ```
      ALLOWED_HOSTS = [.herokuapp.com]
      ```

#### Create Heroku app
    
- Go to https://dashboard.heroku.com/
- Click "New > Create New App"
- Chooses a unique app name and region.

#### Connect Github

- In the Heroku app dashboard, go to Deploy > Deployment Method > GitHub
- Connect your GitHub repository.

#### Set config vars
- In Settings > Reveal Config Vars, set:
      ```
      SECRET_KEY = your_django_secret_key
      DATABASE_URL = (provided by Code Institute)
      ```
#### Buildpacks
- Under settings, confirm the following buildpack is present:
      ```
      heroku/python
      ```

#### Deploy

-  Either enable Automatic Deploys or click Deploy Branch manually.

## Testing

## Credits

## Acknowledgements

- [Code Institute](https://codeinstitute.net/) - for the educational content and support throughout the course.
- [Iuliia Konovalova](https://github.com/IuliiaKonovalova) - my mentor for her kind support, constructive feedback, and continuous guidance.
- [Lewis Dillon](https://github.com/LewisMDillon) - Code Institute Cohort Facilitator, for his motivational support and for always being willing to answer my questions when needed.



* [Back To Top](#contents)