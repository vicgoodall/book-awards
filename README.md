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
Based on the above initial designs, the database was designed with the following relationships:
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
