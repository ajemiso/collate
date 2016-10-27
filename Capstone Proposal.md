## Capstone Proposal

### Product Name

#### **_Collate_**

### Product Overview

**_Collate_** was initially designed to work in conjunction with an existing loan processing web application, minimizing loan processing tasks in order to decrease redundancy & increase productivity.  Simple tasks such as calculating income & modifying email templates made easy.

### Specific Functionality

#### _Minimum Feature Set_

The main component of the application is the **loan application page**.  The goal is to create a single page form that utilizes AJAX & minimizes the need for navigation & page loading. 

After the user logs in, they will be presented with a **Dashboard**, which lists each user's applications in progress/completed. 

The **Navigation** area at the top of the screen will allow the user to go back to the main page of this dashboard via the **Home** link, allow any input data to be saved to the database via the **Save** link, and allow for the creation of a new file via the **New File** link.

**Section One** of the the dashboard contains fields for borrower name(s), loan account number, loan officer name, and type of loan.

**Section Two** of the dashboard will take borrower(s) income infomation (employer name, job start date, monthly income amount, paystub period end date, and pay schedule type), and will output a concatenated string for the user to input back into their main loan application.  

_example: B1: Employed with the Portland Trailblazers for 4 years, semi-monthly pay, $40,000.00/mo, good through 11/01/2016_

Section Two will also allow input of tax, insurance, and homeowner's association dues information (see Further Work section.)

**Section Three** will be a quick navigation area, which may not contain links until the MVP is completed.

[Splash Screen Wireframe](https://wireframe.cc/LHxTck)

[Dashboard Wireframe - _click link for annotations_](https://wireframe.cc/LHxTck)

### Data Model

The relational database will be structured as follows:

**User Table:**

* Username
* Password (hashed)
* First Name
* Last Name
* User ID
* Email Address
* Date Account Created

**File Table**

* Loan Number 
* Account Type
* Loan Processor (Foreign Key)
* Loan Officer
* Loan Story
* Subject Property Address
* Subject Property City
* Subject Property State
* Subject Property Zip Code
* Property Appraisal Value
* Member One First Name
* Member One Last Name
* Member Two First Name
* Member Two Last Name
* Member One Employer Name
* Member Two Employer Name
* Member One Phone Number
* Member Two Phone Number
* SMS Templates
* SMS Message
* Member One Email Address
* Member Two Email Address
* Email Templates
* Email Message
* Member One Hire Date
* Member Two Hire Date
* Member One Income Amount
* Member Two Income Amount
* Member One Pay Frequency
* Member Two Pay Frequency
* Member One Period Ending Date
* Member Two Period Ending Date
* Member One Income Output
* Member Two Income Output
* Date Created/Last Updated

### Technical Components

Django framework will require modules that can preform the following tasks: 

* Register a new user
* Allow user to log in
* Allow user to create a new file
* Allow user to to save, load, and delete file data
* Calculate income based on pay cycle

### Further Work

* Implementing Email Templates
* Adding Tax, Insurance, & HOA elements






















