# The Tortoise Book Prize 

## Code Institute Milestone Project 3: Backend Development 
The Tortoise Book Prize Review Scheme that allows schools to engage with the book award, by students reading each of the nominated books and publishing reviews, under the supervision of their teacher. The website tracks how many books a student has reviewed, and readers are encouraged to review all nominations by offering a certificate of completion and a book token at the end. 

# Initial Design
### Strategy
## Owner Key Goals:
- to create engagement and grow interest in the Book Prize
- to build momentum for the announcement of the prize winner
- to spark conversation and critical analysis in the book nominees
- to encourage reading in students
- to give students an opportunity to write and share reviews
## User Key Goals
- to provide students with a supervised, safe online environment to publish their work
- to practise writing book reviews and articulating their views in a critical format
- to be able to reward students when they have read and reviewed all nominees
## Key Design Decisions
From the initial strategy goals, the following issues were identified that determined design decisions:
## 1. Creating two User categories
### Problem: 
Need to have students' work supervised, including their account name and a check on the quality of their reviews.
### Solution:
Have students and teachers as separate 'accounts' by holding each within separate tables, and giving teachers the ability to oversee their associated students' work.
## 2. Decision to use a relational database structure
### Problem:
Students need to be created with an association to a teacher, and have limited information available for privacy
### Solution:
Teachers complete initial registration, and then once logged in are able to create students. Each student when added is automatically linked to that teacher's id as a foreign key. The Student's unique detail is their (presumably school) email address, and then teacher can enter a first name and a surname initial. Reviews for general public do not display student's school, so only shows name in First. S format.
In order to achieve this, a relational database management system is required, and Postgres has been selected for this as it fulfills the requirements.
## 3. Creating the concept of Roles within the database
### Problem:
Teacher's actions are very different to the students i.e. students will write reviews, but teachers will only be managing and supervising the students' work.
### Solution:
Create a role concept within the database, where the actions page (i.e. Account) is determined by the role id assigned to each user (Teacher role or Student role).

## Database Design
Based on the above initial designs, the database was designed with the following relationships using Figma:
![database initial design](../book-awards/bookreviews/static/assets/design-images/Tortoise%20Prize%20DB%20Design.png)
- Teachers are linked to each of their students by their primary key
- Students are linked to each of their reviews by their primary key
- Students and Teachers both have roles assigned by linking to the Role's primary key
- Each review will be linked to a book by the latter's primary key.

# Scope
### General Website User Stories
#### As a user who has not logged in, I want to...
- Be able to view information about the review scheme, so I can find out what it is and if it's something I can participate in
- View reviews that have been published with minimal author information for privacy
### Teacher User Stories
#### As a teacher, I want to be able to...
- Register my school/class for the review project
- Update my own details if I need
- Register each of my students
- Update my student' details as necessary
- Delete a student account, and by default also delete all of their reviews.
- View all of my student' reviews on a dedicated page
- Delete a student's review if needed
- Track how many reviews each student has published
### Student User Stories
#### As a student, I want to be able to...
- View my details eg. my name, so I can let my teacher know if there is a typo as it will be published on each review
- Create one review per nominated book
- View reviews I have already published
- Update any review I have created
- Delete any review I have created and be able to create a fresh review for that book if I choose
- See how many books I have left to review
### User Profile
- In general, the majority of users would access the site during school hours, on school computers.
- For this reason, it is determined that the website should be designed primarily for laptops and desktops.
- However, users may well want to view reviews and access their account via a mobile device. It's therefore important the website is usable on smaller screens. 

# Frontend Design
## Wireframes
Provided are scans of the original wireframes.
The conclusion from the websites was that the site is going to be text heavy, and therefore it is imperative that each review is clearly distinguishable from one another.
It is also noted that the user's Account screen, where they complete the majority of actions, will needed to be as simple as possible in layout, in order to facilitate the varying activities to be completed. 
## Colour Scheme
- Colour scheme was determined by the academic setting of the website's users
- The website is text heavy, and often pages are loaded with information (reviews, account actions). Decision made to keep colour scheme simplistic with a primary colour for background, a neutral for legibility of the text, and an accent colour for occasional colour pops. 
![colour scheme](../book-awards/bookreviews/static/assets/design-images/Tortoise%20Prize%20colour%20scheme.png)
- As the website is primarily intended for 11-16 year old students, the starting point was a dark plue initially inspired by 'Oxford blue', but made more fun by selecting something a little brighter and lighter.
- Once selected on ColorSpace, the application showed various options, with one providing a cream for text backgrounds and a fun turquoise green as an accent that reflects the youthful intended audience. 
- The lilac shade was decided against for the sake of simplicity. 
## Typography
- The fonts were selected to provide an academic vibe that wasn't overly formal. 
- From Google Fonts, 'Nanum Myeongjo' was selected for the Book Prize's logo, anbd is only visible in the logo's header
- For all other text, 'Playfair Display' was selected as it was similar to the logo, but felt contemporary and easy to read in large paragraphs. 
## Frontend Structure
The website is broken down into 15 pages, each stored in a respective html file. 
### Home 
#### base.html
- Home page accessible to everyone, available content not affected by having a user logged in.
- Primary aim is to show the nominated books for 2023 
### About
#### about.html
- About page is accessible to everyone, available content not affected by having a user logged in.
- Gives a little more background about the Book Prize and Review Scheme
### Reviews
#### reviews.html
- Reviews page accessible to everyone, available content not affected by having a user logged in.
- Shows all published reviews
### Register
#### register.html
- Form where teachers can sign up to the review scheme as the supervisor for their class
### Login
#### login.html
- User is asked whether they are logging in as a student or teacher.
- Select an option to move to the correct log-in screen
### Login as Teacher
#### login-teacher.html
- Teacher can enter their email and password to log in
### Login as Student
#### login-student.html
- Student can enter their email and password to log in
### Account
#### account.html
- User can manage their account and complete actions depending on their role.
Teachers can:
- View and edit their details
- Create, view, update, or delete a student account
- See a list of students and how many reviews they have published
- View and delete reviews published by students they have registered
Students can:
- View their details
- View, update and delete their published reviews
- See how many books they have left to review
- Create new reviews
### Update Details (Teacher)
#### update-teacher.html
- a Teacher can view and update their own details as needed
### Create Student (Teacher)
#### student-register.html
- Teachers can create a new student by entering mandatory information
### Update Student (Teacher)
#### update-student.html
- Teachers can update a student's details as needed
### View Students' Reviews (Teacher)
#### view-reviews.html
- Teachers can view all reviews created by their registered students
- Teachers can delete reviews if needed
### Add Review (Student)
#### add-review.html
- Students can create a new review
### My Reviews (Student)
#### my-reviews.html
- Students can see all reviews they have published
- From here, they can delete or update a review as needed
### Update Review (Student)
#### update-review.html
- Students can amend a review they have already published

## CRUD Functionality
### CREATE
- Teachers can create their own account
- Teachers can create student accounts associated to their own account
- Students can create their own reviews

### READ
- Any website visitor can view the nominated books
- Any website visitor can view the published reviews
- Teachers can view their own account details
- Teachers can view their students' details
- Teachers can view their students' reviews
- Students can view their account details
- Students can view their own reviews

### UPDATE
- Teachers can update their own account details
- Teachers can update their associated stuidents' account details
- Students can update their own reviews

### DELETE
- Teachers can delete an associated student's account, which will also delete that student's reviews
- Teachers can delete an associated student's reviews
- Students can delete their own reviews

## Backend Frameworks
- Python was used as the backend programming language.
- The Flask framework was selected as an ideal way to implement Python as it enables use of Jinja to interact with the frontend, and Werkzeug to facilitate user authentication. 
- As a PostgreSQL database is being used, SQL Alchemy was selected as the best toolkit with which to compose queries.
- Thus the Flask-SQLAlchemy extension is used to combine both resources

# Features
## Home Screen Display of Books
![home screen](../book-awards/bookreviews/static/assets/design-images/Home%20screen.png)
- The books were entered into the application on first access (the code is available to view, commented out, for information only in the routes file). This prevents the user being able to adapt the table in any way, as this particular table will not require amending.
- They are listed on the home page using Jinja as an announcement of the nominees to commence this year's reviews.
- A row of images, the cover of each book, is visible below the announcement card. 
- A tutorial page at [w3Schools](https://www.w3schools.com/howto/howto_css_images_side_by_side.asp) enabled this banner to be created, by modifying the code provided. 
- A post on [Stack Overflow](https://stackoverflow.com/questions/19414856/how-can-i-make-all-images-of-different-height-and-width-the-same-via-css) provided code which when modified, was able to create consistency in height  between the six images.

## Register as Teacher
![register as teacher screen](../book-awards/bookreviews/static/assets/design-images/Register%20teacher.png)
- Teachers enter their details into the form, which is then used to create a new row in the Teachers table.
- The primary key, id, is the unique value used in the backend to associate teachers to students, in a one to many relationship. 
- This could be built upon in future, to be able to delete teachers fairly easily, as it would cascade down to delete their students' accounts and in turn their reviews, as currently composed within the model. 
- The user's email is used as their login id, and therefore is also unique. The system prohibits another user being created with the same email address. 
- A Teacher record by default is given the value 1 in its Roles column. 

## Create a Student account
![create student account screen](../book-awards/bookreviews/static/assets/design-images/Create%20Student%20Account.png)
- Teachers create student accounts, which enables them to be associated easily
- The student's details are purposely sparse to retain their privacy when publishing reviews
- In order to enable a login, the password field is also here. This is admittedly poor practice, but as this project isn't an exercise in user authentication, it was determined as the simplest way to get the students logged in. It would be straightforward to add a password change option within a student's account, or alternatively look into OTP options. (Alternatively, students could participate in creating their own accounts, and enter their own password).
- When the completed form is submitted, in the backend a new row is added to the Students table. By default the row's teacher and school values are filled by taking them from the Teacher's ID and School values.
- The Student's primary key, their ID, will enable them to be identified as the author of any reviews they publish. Their email, used to login, is also unique; as with the Teacher registration, the application will prevent another Student being created with the same email address.
- The value books_read is also added to the newly created Student record and set to 0. This value is used to track how many reviews the Student has created.
- A Student record by default is given the value 2 in its Roles column. 

## Account page 
![teacher account screen](../book-awards/bookreviews/static/assets/design-images/teacher%20account.png)
![student account page](../book-awards/bookreviews/static/assets/design-images/student%20account.png)
- The Role id within each user determines the view on this page: 1 = Teacher, 2 = Student.
Teachers have the following features: 
- They can view their own details
- They can view each student and have the option to update or delete
- They have a list of each student again, but this time it shows how many reviews each has written. They can navigate to read their students' reviews.
While Students have these features:
- They can see their own details but cannot edit (if they felt it needed updating, they could speak to their teacher)
- They can see a list of reviews they have written so far and can navigate to view them in full
- They can see how many books are left to review, made possible by the books_read value attached to each Student record. If they have reviewed all 6 books, an alternative message is shown informing them they are eligible to receive their certificate and book token
- If they do have books left to review, they can navigate from here to create a new review (this button is unavailable if their books_read = 6)

## Create Review 





