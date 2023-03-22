# The Tortoise Book Prize 

## Code Institute Milestone Project 3: Backend Development 
The Tortoise Book Prize Review Scheme that allows schools to engage with the book award, by students reading each of the nominated books and publishing reviews, under the supervision of their teacher. The website tracks how many books a student has reviewed, and readers are encouraged to review all nominations by offering a certificate of completion and a book token at the end. 

## Initial Design
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
## 1. Teacher Users & Student Users
### Problem: 
Need to have students' work supervised, including their account name and a check on the quality of their reviews.
### Solution:
Have students and teachers as separate 'accounts' by holding each within separate tables, and giving teachers the ability to oversee their associated students' work.
## 2. Relational database
### Problem:
Students need to be created with an association to a teacher, and have limited information available for privacy
### Solution:
Teachers complete initial registration, and then once logged in are able to create students. Each student when added is automatically linked to that teacher's id as a foreign key. The Student's unique detail is their (presumably school) email address, and then teacher can enter a first name and a surname initial. Reviews for general public do not display student's school, so only shows name in First. S format.
In order to achieve this, a relational database management system is required.
## 3. Role concept
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

## Scope
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
