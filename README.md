# The Tortoise Book Prize 

## Code Institute Milestone Project 3: Backend Development 
The Tortoise Book Prize is a children's book award given to one work of fiction annually. The Review Scheme is a project that allows schools to engage with the book award, by students reading each of the nominated books and publishing reviews, under the supervision of their teacher. The website tracks how many books a student has reviewed, and readers are encouraged to review all nominations by offering a certificate of completion and a book token at the end. 

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
## 4. Using start-up code to add values to two tables
### Problem:
I want my roles and books within their own tables, but I do not want the user to have access to this. I would prefer not to create a system admin, as this would place too much emphasis on user authentication rather than demonstrating CRUD functionality
### Solution:
Run start up code post deployment, then comment it out, so the book and roles values are added into their respective tables. I have left in this code with a note to explain its intent, just for information to show how I completed this. 


## Database Design
Based on the above initial designs, the database was designed with the following relationships using Figma:
![database initial design](https://github.com/vicgoodall/book-awards/blob/assets/design-images/TortoisePrizeDBDesign.png)
- Teachers are linked to each of their students by their primary key
- Students are linked to each of their reviews by their primary key
- Students and Teachers both have roles assigned by linking to the Role's primary key
- Each review will be linked to a book by the latter's primary key.

# Scope
### General Website User Stories
### As a user who has not logged in, I want to...
- Be able to view information about the review scheme, so I can find out what it is and if it's something I can participate in
- View reviews that have been published with minimal author information for privacy
### Teacher User Stories
### As a teacher, I want to be able to...
- Register my school/class for the review project
- Update my own details if I need
- Register each of my students
- Update my student' details as necessary
- Delete a student account, and by default also delete all of their reviews.
- View all of my student' reviews on a dedicated page
- Delete a student's review if needed
- Track how many reviews each student has published
### Student User Stories
### As a student, I want to be able to...
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
![Home screen wireframe](https://github.com/vicgoodall/book-awards/bookreviews/static/assets/design-images/homescreenwireframe.png)
![Account wireframe](https://github.com/vicgoodall/book-awards/bookreviews/static/assets/design-images/accountwireframe.png)
![Register wireframe](https://github.com/vicgoodall/book-awards/bookreviews/static/assets/design-images/registrationwireframe.png)
![Reviews wireframe](https://github.com/vicgoodall/book-awards/bookreviews/static/assets/design-images/reviewswireframe.png)
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
The website is broken down into 15 pages, each stored in a respective html file. The [Materialize](https://materializecss.com/) framework has been used to create a consistent, simple card-based structure throughout the project, that can manage the text-heavy nature of the website.
### Home 
### base.html
- Home page accessible to everyone, available content not affected by having a user logged in.
- Primary aim is to show the nominated books for 2023 
### About
### about.html
- About page is accessible to everyone, available content not affected by having a user logged in.
- Gives a little more background about the Book Prize and Review Scheme
### Reviews
### reviews.html
- Reviews page accessible to everyone, available content not affected by having a user logged in.
- Shows all published reviews
### Register
### register.html
- Form where teachers can sign up to the review scheme as the supervisor for their class
### Login
### login.html
- User is asked whether they are logging in as a student or teacher.
- Select an option to move to the correct log-in screen
### Login as Teacher
### login-teacher.html
- Teacher can enter their email and password to log in
### Login as Student
### login-student.html
- Student can enter their email and password to log in
### Account
### account.html
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
### update-teacher.html
- a Teacher can view and update their own details as needed
### Create Student (Teacher)
### student-register.html
- Teachers can create a new student by entering mandatory information
### Update Student (Teacher)
### update-student.html
- Teachers can update a student's details as needed
### View Students' Reviews (Teacher)
### view-reviews.html
- Teachers can view all reviews created by their registered students
- Teachers can delete reviews if needed
### Add Review (Student)
### add-review.html
- Students can create a new review
### My Reviews (Student)
### my-reviews.html
- Students can see all reviews they have published
- From here, they can delete or update a review as needed
### Update Review (Student)
### update-review.html
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
- Thus the [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/) extension is used to combine both resources

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
- **Please note that user authentication for a SQL based database was not within the course. However, I discovered it was within the bonus content, and watched some of the videos there to learn how this worked. The Code Institute [GitHub](https://github.com/Code-Institute-Solutions/CombinedTaskManager2022) shows the project that taught me the majority of my understanding. I was also helped by this [Youtube](https://www.youtube.com/watch?v=1nxzOrLWiic&t=374s) video by Tech by Tim which gave me another perspective on managing users simply** 
## Create a Student account
![create student account screen](../book-awards/bookreviews/static/assets/design-images/Create%20Student%20Account.png)
- Teachers create student accounts, which enables them to be associated easily
- The student's details are purposely sparse to retain their privacy when publishing reviews
- In order to enable a login, the password field is also here. This is admittedly poor practice, but as this project isn't an exercise in user authentication, it was determined as the simplest way to get the students logged in. It would be straightforward to add a password change option within a student's account, or alternatively look into OTP options. (Alternatively, students could participate in creating their own accounts, and enter their own password).
- When the completed form is submitted, in the backend a new row is added to the Students table. By default the row's teacher and school values are filled by taking them from the Teacher's ID and School values.
- The Student's primary key, their ID, will enable them to be identified as the author of any reviews they publish. Their email, used to login, is also unique; as with the Teacher registration, the application will prevent another Student being created with the same email address.
- The value books_read is also added to the newly created Student record and set to 0. This value is used to track how many reviews the Student has created.
- A Student record by default is given the value 2 in its Roles column. 

## Login Pages
![login screen](../book-awards/bookreviews/static/assets/design-images/login.png)
- Because of the separation needed between Teachers and Students, I split the login into three pages: One asking whether the user is a Teacher or Student, and then an actual log-in form for each user type. This allows both pages to run separate queries to their respective Tables, to find the user.
- There are probably more elegant solutions for this. However, user authentication is a new challenge and for my first attempt I wanted to simplify the process. 

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
![create review screen](../book-awards/bookreviews/static/assets/design-images/create%20review.png)
- Only Students can create reviews
- They can select the book they wish to review via dropdown. To enable this, a query was created that first checked which books the user had reviewed within the Reviews table. A second query, this time in the Books table, subtracts that list from the six results available, and the remainder is shown to the user.
- The concept of subqueries was very new, and supplied by a lot of searching and eventually finding this suggestion in [Stack Overflow](https://stackoverflow.com/questions/38878897/how-to-make-a-subquery-in-sqlalchemy)
- The user must complete all fields to submit the form.
- When the form is submitted, a new record is added to the Reviews table, where the Review is tied to the Student's ID as it's 'author' value, and the book's ID as it's 'book' field.
- When a review is successfully added, the user's books_read is incremented by 1.

## Update Review
- A student is able to update any review they have published. The values are pre-filled with their original content, and the record cannot be updated if the user clears a field and leaves it blank.
- Once the form is submitted, the record is updated in the backend within the Reviews table.

## Delete Review
- If the user opts to delete a review, a modal appears asking them to confirm. 
- When they confirm, the record is deleted in the Reviews table.
- This then decrements their books_read by 1, and also will allow them to create a fresh Review (i.e. a brand new record) within the Reviews table.

## Update Teacher Details
- A teacher may update their own details 
- The values are pre-filled with their original content, and the record cannot be updated if the user clears a field and leaves it blank.
- Once the form is submitted, the record is updated in the backend within the Teachers table.

## Update Student Details
- A teacher may update their associated student's details.
- The values are pre-filled with their original content, and the record cannot be updated if the user clears a field and leaves it blank.
- Once the form is submitted, the record is updated in the backend within the Students table.

## Delete Student Details
- A teacher can delete an associated student's account
- If the user presses Delete, a modal appears asking them to confirm.
- When they confirm, the record is deleted within the Students table.
- This will also by default delete any review(s) published by the Student within the Reviews table. 

## Delete a Student's Review
![delete review screen](../book-awards/bookreviews/static/assets/design-images/delete%20review.png)
- In order to accomplish the supervision element of the scope, if a teacher determines a review is unsuitable to be visible to other readers (eg. bad language), they can delete an associated Student's review. 
- A modal appears asking the user to confirm the review deletion.
- On confirming, the Student who wrote the review will have their books_read decremented by 1 the same as if the Student had deleted the review

## View all reviews
- Anyone who visits the site can view all reviews
- The only details about the author are their first name and initial, maintaining privacy
- Initially the reviews were displayed in order of ID, which kept the list static. This felt unfair to reviewers who publish later, who are less likely to get their work read.
- To fix this, I looked into how to randomly display all results, and this post from [Stack Overflow](https://stackoverflow.com/questions/66247588/randomly-shuffle-query-results-where-values-are-the-same) contained the code that enabled this to occur. 

# Testing
## Static Testing

### HTML Validation
[W3C](https://validator.w3.org/) was used to validate the HTML. Where the user had to log in, I navigated to 'View Page Source" and pasted the contents into the validator. 
#### identified issues
[alt tags](../book-awards/bookreviews/static/assets/design-images/alt%20image.png)
- identified no alt tags were added to my images; this is now fixed.

### CSS Validation 
[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
![Jigsaw validation](../book-awards/bookreviews/static/assets/design-images/Jigsaw%20validation.png)
No issues identified.

### JQuery Validation
[JSHint](https://jshint.com/) was used to validate the JQuery.
![JSHint validation](../book-awards/bookreviews/static/assets/design-images/jshint%20validation.png)
- an unnecessary semicolon was at the end of the code. This has been removed.

### Python Validation
[CI Pep8 Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code. 
![Python linter](../book-awards/bookreviews/static/assets/design-images/Pep8%20linter.png)
- received no errors on routes.py & models.py

## Dynamic Testing

### Functional System Tests

### Users not logged in
| ID | Test Case | Description | Result |
| ---|-----------|-------------|--------|
| 001 | Home page | The user is able to view the book titles on the home page | Pass |
| 002 | About | The user can view the About page and its text contents | Pass |
| 003 | Reviews | The user can see all presently published reviews | Pass |
| 004 | Review randomization | On navigating back to the Reviews page, the reviews are displayed in a different order. | Pass |
| 005 | Prohibited views | The user cannot view the Account or Logout buttons | Pass |
| 006 | Login or Register | The user can view the Login and Register screens, and the forms load correctly | Pass |
| 007 | Social links | When the user presses the social links, they load the corresponding websites | Pass |

### Users are Teachers
| ID | Test Case | Description | Result |
| ---|-----------|-------------|--------|
| 008| Incomplete form | On the register page, the user cannot proceed if they have blank fields on the form | Fail |
| 009| Existing email | On the registration page, if the user enters the email of a pre-existing Teacher account, the system will inform them on submitting the form that the user already exists | Pass|
| 010| Register teacher | Once all fields have been entered, when the user presses the Register button they are successfully registered and logged in | Pass |
| 011| View details | In the Account page, the teacher is able to view their details as entered previously | Pass |
| 012| Update details incomplete | On attempting to enter their details, the user cannot proceed if any fields are blank. | Pass |
| 013| Update details | On amending any or all fields, the user will be able to successfully update their details | Pass |
| 014| Create student | On the creation page, the user cannot proceed if they have blank fields on the form | Fail |
| 015| Existing student | If another Student record already exists with the same email address, the user will be notified on submission that the user already exists | Pass |
| 016 | Register student | Once all fields have been entered, the user will successfully create a Student account | Pass | 
| 017| View all students | All created student accounts will be visible in a list in the teacher's Account, with 'Update' and 'Delete' buttons available next to each Student name | Pass |
| 018| Update student details incomplete |  On attempting to update student details, if a field is blank, the user cannot proceed | Pass |
| 019 | Update student details | On amending field(s), when all fields are complete, the user will be able to successfully update the student account | Pass |
| 020 | Delete student modal | On pressing the Delete button next to a student, a modal will appear. Pressing Cancel will return the user with no change to the account | Pass |
| 021 | Delete student confirm | On pressing the Delete button and confirming within the Modal, the student will be deleted | Pass |
| 022 | Delete student with published reviews | On deleting a student with published reviews, the reviews will also be deleted | Pass |
| 023 | Display student review tally | The teacher will be able to see a list of associated student names, and the number of reviews they have created, which is 0 at minimum and 6 as maximum | Pass |
| 024 | View all reviews | The teacher is able to view all reviews published by associated students in a dedicated page | Pass |
| 025 | Delete review modal | For each review, the user is able to press a Delete button, which causes a modal to appear. On pressing Cancel, the box will disappear and the reviews page will be unchnaged. | Pass |
| 026 | Confirm review delete | If the user confirms in the modal to delete a student's review, the the record is deleted, removed from the Reviews page and the student's books_read will reduce by 1. This will be visible within the tally on the Teacher's account page, and in the Student's Accout page | Pass |
| 027| Press Register or Login | If the logged in user presses Register or Log Out buttons, they will be redirected to their Account page with an informative message | Pass |
| 028 | Logout | On pressing the Log Out button, the user is logged out of their account and returned to the Login Page | 
| 029 | Login without password | If the teacher tries to log in with incorrect details, they will be unsuccessful and an informagtive message is displayed | Pass |
| 030| Log in as teacher | User is able to log back into their account with email and password | Pass |


### Users are Students

| ID | Test Case | Description | Result |
| ---|-----------|-------------|--------|
| 031| Login with missing details | The student needs the correct email and password to login, otherwise are met with an informative message | Pass |
| 032| Log in as student | User is able to log in with their email and password | Pass |
| 033| View details | In the user's Account page, they can view their details in a read-only display. | Pass |
| 034 | Display number of books to review | In the user's Account page, they will see how many books they have left to review, or else a message congratulating them on reviewing all books | Pass |
| 035 | Create review books available | When creating a new review, only books the user has not yet reviewed will be available in the dropdown | Pass |
| 036 | Create review incomplete fields | The user cannot proceed when review fields are missing content | Pass |
| 037 | Create review | On completing all fields, the user can publish a review successfully. It will be immediately displayed in the list in their Account, and their books available will reduce by 1 | Pass | 
| 038 | Update review required fields missing | If the user tries to update a review, they will be unable to proceed if fields are blank | Pass |
| 039 | Update review | On changing field(s), when the user submits then the review is updated and changes are reflected immediately. | Pass |
| 040 | View reviews | The user is able to view all their reviews in full, with buttons to update or delete each one | Pass |
| 041| Delete review modal | If the user presses the Delete button, a modal appears asking them if they are sure. If they press Cancel the box closes, and their reviews are left unchanged. | Pass |
| 042 | Confirm deletion | If the user confirms deleting their review, then the review is removed from their reviews page successfully, their books_read is decremented by 1, the review is removed from the list in their Account page, and the associated book becomes available to review again. | Pass |
| 043| All books reviewed | When the user has submitted a review for each book, they can no longer access the create review screen. Instead they have a notification congratulating them on their work. | Pass |
| 044| Log out | On pressing the log out button, the user is logged out of their account and returned to the login page | Pass |


- It was identified that form fields were still missing 'Required' tags, causing tests to fail. This has been resolved.

## Known Defect
- During testing it became evident that a defect exists within both student and teacher update forms, where the user is able to update the user's email to an address that exists within another account. 
- In a live system, this would be unlikely to happen but where it did, probably through user error, it would cause significant issues for the affected records.
- I tried to remedy this by adding logic to check if the email address already exists, but that prevents the update altogether. 
- The form update as it is relies on the email address; I am reluctant to change this by removing the email from the form, as I do not have sufficient time to conduct regression testing against the change I would need to make to two different methods. 
- The defect is therefore staying in the system, and is a lesson learned in regards to authentication for myself. 

## Device & Browser testing 
- System testing took place on the follwoing devices:
- MacBook Air
- iPhone 12
- Unfortunately, no tablet was available for testing. I have used Chrome's Inspect tool for various tablets, however I know from experience this has limited accuracy. 

And on the following browsers:
- Safari
- Chrome
- Mozilla Firefox

## UI defect
- One particularly unwanted deviation from my initial design is the layout of the reviews as they are created
- I wanted to have, on desktop/laptop, neat rows of several reviews for the user to select and read as they please.
- I failed to appreciate that it is difficult for the system to know how to lay this out when there is no set number to display; once it reached the end of the first row, it didn't know where to place other cards, causing issues such as this:
![review display defect](../book-awards/bookreviews/static/assets/design-images/review%20display%20defect.png)
- I reluctantly changed it so that, like with mobile, reviews were limited to one per row. 
- I would like to return to this in future to see if there is a better way to write my code to enable an improved format on larger screens. 

## Performance Testing 
- Lighthouse was used to test performance
![Lighthouse home screen](../book-awards/bookreviews/static/assets/design-images/lighthouse1.png)
![Lighthouse login screen](../book-awards/bookreviews/static/assets/design-images/lighthouse2.png)
![Lighthouse about screen](../book-awards/bookreviews/static/assets/design-images/lighthouse3.png)
- I have tried to keep the code as simple as possible, creating a simple user interface structure to mitigate the amound of requests from my code. 
- However, I know this is something I need to work on in future, and consider how I can simplify tasks more to improve performance. 

# Deployment 
The following outlines the steps required to deploy the site:

## ElephantSQL
ElephantSQL was used to host the database.
- Navigate to [ElephantSQL](https://elephantsql.com)
- Click ‘Get a managed Database today”
- Select the Tiny Turtle option
- Select ‘Login with GitHub’ and authorize connection with your GitHub account
- Enter a team name and your email address, agree to ToS & GDPR then click ‘Create Team’
- Click ‘Create New Instance’
- Give your new plan a name and select the Tiny Turtle plan
- Press ’Select Region’ and pick the nearest location to yourself
- Click ‘Review’ and check your details are correct
- Click ‘Create Instance’

## Program modification
In order to connect with Heroku, the following amendments are required to the program:
- In your command line, enter: pip freeze — local > requirements.txt
- Within the root directory, create a file called Profile
- Enter in this file: “web: python run.py”
- Open your init file and make the following amendments to your if/else statement: 
if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
 else:
     uri = os.environ.get("DATABASE_URL")
     if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
     app.config["SQLALCHEMY_DATABASE_URI"] = uri
- Save, push and commit changes

## Heroku
- Log into [Heroku](https://heroku.com), click ‘New’ 
- Click ‘Create a new app’
- Choose a unique name
- Select the region closest to yourself
- Click ‘ Create app’
- Go to Settings of the app
- Click ‘Reveal Config Vars’
- Return to ElephantSQ: and copy the database URL found within Details
- In Heroic, add a Config Var called DATABASE_URL and paste the ElephantSQL URL in, then press ‘Add’
- Add every environment variable: IP, PORT, SECRET_KEY
- Navigate to ‘Deploy’
- Select ‘Connect to GitHub’
- Search for your repository then click ‘Connect’
- Within Manual Deploy, click ‘Deploy Branch’
- Click ‘More’ then ‘Run console’
- Type ‘python3’ and click Run
- Type: from app name import db
    db.create_all()
- exit() and hit Enter 

# References

## Code
- The image banner: [w3Schools](https://www.w3schools.com/howto/howto_css_images_side_by_side.asp)
- Enabling all images to be the same height: [Stack Overflow](https://stackoverflow.com/questions/19414856/how-can-i-make-all-images-of-different-height-and-width-the-same-via-css)
- Flask SQL Users [Tech with Tim](https://www.youtube.com/watch?v=1nxzOrLWiic&t=374s) Youtube tutorial as a crash course in user creation 
- subquerying for the books to review tally courtesy of this post on [Stack Overflow](https://stackoverflow.com/questions/38878897/how-to-make-a-subquery-in-sqlalchemy)
- Randomizing query displays thanks to this post on [Stack Overflow](https://stackoverflow.com/questions/66247588/randomly-shuffle-query-results-where-values-are-the-same) 
- Sticky footer CSS code is from [Materialize](https://materializecss.com/footer.html)
- Disabling horizontal scroll code is from [Stack Overflow](https://stackoverflow.com/questions/4192277/disable-horizontal-scroll-on-mobile-web)

## Books
The books used for this database were books I read as a child. Here are their details based on their publication in the UK:
- A Gathering Light, Jennifer Donnelly, Harcourt, 2003
- Bloomability, Sharon Creech, HarperCollins, 1998
- Private Peaceful, Michael Morpurgo, HarperCollins, 2003
- How I Live Now, Meg Rosoff, Penguin, 2004
- Red Sky in the Morning, Elizabeth Laird, Heinemann, 1998
- Journey to the River Sea, Eva Ibbotson, Macmillan, 2001

## Images
For each of the books, the URLs for the book cover images:
- [A Gathering Light](https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/510DfH53Q1L.jpg)
- [Bloomability](https://productimages.worldofbooks.com/0330397842.jpg)
- [Private Peaceful](https://d3ddkgxe55ca6c.cloudfront.net/assets/t1497828499/a/e4/31/84824-ml-78873.jpg)
- [How I Live Now](https://d3ddkgxe55ca6c.cloudfront.net/assets/t1497828499/a/e4/31/84824-ml-78873.jpg)
- [Journey to the River Sea](https://pictures.abebooks.com/isbn/9780330397155-uk.jpg)
- [Red Sky in the Morning](https://pictures.abebooks.com/isbn/9781509802937-uk.jpg)

## Media
- [Font Awesome](https://fontawesome.com/) for icons throughout the project
- [Google Fonts](https://fonts.google.com/) for the fonts used in the project
- [ColorSpace](https://mycolor.space/) for the colour scheme selection

## Acknowledgement
This project was inspired by the Carnegie Medal Shadowing Project in which I participated as a child. It still exists today [here](https://yotocarnegies.co.uk/take-part/).















