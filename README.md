<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT NAME -->
<h3 align="center">Active Gym Admin App Project</h3>

  <p align="center">
    This project is my first one ever. It was created four weeks into the 16 week CodeClan Software Developer Bootcamp.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

After four weeks of intensive learning when, on day one, it was assumed we hadn't done any coding before, it was time for our first full stack project. 

We were given a choice of briefs which varied in complexity of database relationships (ie either a one-to-many or a many-to-many relationship). I ended up adding an extra table, so this app utilises both the many-to-many and a one-to-many relationship.

Here's the brief:

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.
MVP

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

Extensions That I Added:

- Classes could have a maximum capacity, and users can only be added while there is space remaining.
- Users cannot be added twice to one class
- The app has Instructors who can be assigned to a class



<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* HTML
* CSS
* Python
* Flask
* Postgresql


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

To run this app, you must have: 
* psychopg
  ```sh
  pip3 install psycopg2
  ```

* Flask
  ```sh
  pip3 install Flask
  ```

* Postgresql

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HelenLangers/CC_Gym_App_Project.git
   ```
2. Navigate via Terminal to the folder
3. Create the database
  ```sh
  psql -d gym_app -f db/gym_app.sql
   ```
4. Populate the database with pre-set objects
  ```sh
  python3 console.py
  ```
5. Run Flask
  ```sh
  flask run
  ```
6. Open in Chrome: http://127.0.0.1:4999
7. To stop the server enter ctrl + c in your Terminal

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Helen Langridge - [Twitter](https://twitter.com/HelenCycling) - [LinkedIn](https://www.linkedin.com/in/helen-langridge-62b32b166/)

Project Link: [https://github.com/HelenLangers/CC_Gym_App_Project](https://github.com/HelenLangers/CC_Gym_App_Project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [CodeClan](https://codeclan.com/)
* [FontAwesome](https://fontawesome.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

