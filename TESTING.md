# Testing
---
# Contents

## Browser Compatibility

## Responsiveness

## Manual Testing

Thorough manual testing was done for all critical user interactions across pages.

### Global Navigation

| Feature        | Action | Expected Result                                                                          | Works?              |
|----------------|--------|------------------------------------------------------------------------------------------|---------------------|
| Brand Name     | Click  | Goes to homepage                                                                         | Works as expected   |
| Nav links      | Hover  | Visual feedback - font colour changes to white and link underlined                       | Works as expected   |
| Nav links      | Click  | Page changes to relevant page                                                            | Works as expected   |
| Messages       | Timeout| Auto-dismiss after 4s                                                                    | Works as expected   |
| Logout         | Click  | User redirected to logout confirmation page                                              | Works as expected   |
| Footer Link    | Hover  | Visual feedback - font colour darkens                                                    | Works as expected   |
| Footer Link    | Click  | Page opens up a new tab to github account                                                | Works as expected   |
| Hamburger Menu | Click  | When in mobile (logged out) hamburger menu does not bring up nav links                   | Works as expected   |
| Hamburger Menu | Click  | When in mobile (logged in) hamburger bring up working nav links                          | Works as expected   |

### Home Page

| Feature           | Action    | Expected Result                       | Works?              |
|-------------------|-----------|---------------------------------------|---------------------|
| Introduction Text | View      | Clear site intro                      | Works as expected   |
| Login Button      | Hover     | Visual Feedback                       | Works as expected   |
| Login Button      | Click     | User redirected to login page         | Works as expected   |
| Register Button   | Hover     | Visual Feedback                       | Works as expected   |
| Register Button   | Click     | User redirected to signup page        | Works as expected   |

### Login Page

| Feature         | Action              | Expected Result                                      | Works?             |
|-----------------|---------------------|------------------------------------------------------|---------------------|
| Login form      | View                | Form is visible with username/email and password fields | Works as expected   |
| Empty fields    | Submit empty form   | Error message shown; form not submitted              | Works as expected   |
| Invalid details | Submit wrong login  | Error message shown; user not logged in              | Works as expected   |
| Valid login     | Submit correct login| User is redirected to dashboard                      | Works as expected   |
| Message display | After login         | Login success message shown briefly                  | Works as expected   |

### Register Page

| Feature             | Action                  | Expected Result                                         | Works?             |
|---------------------|-------------------------|---------------------------------------------------------|---------------------|
| Register form       | View                    | Form with required fields (username, email, password) is visible | Works as expected   |
| Password help text  | View                    | Help text describing password requirements is shown     | Works as expected   |
| Validation          | Submit mismatched passwords | Error shown; user not registered                     | Works as expected   |
| Duplicate email     | Submit existing email    | Error shown; user not registered                        | Works as expected   |
| Valid registration  | Submit correct details   | Account created and user redirected to dashboard        | Works as expected   |
| Message display     | After registration       | Registration success message shown briefly              | Works as expected   |

### Dashboard Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|
| View today's summary       | View       | Shows total driving time and alerts                    | Works as expected   |
| Add trip button            | Hover      | Visual Feedback                                        | Works as expected   |
| Add trip button            | Click      | Redirects user to daily log summary page               | Works as expected   |
| Create todays' log button  | Hover      | Visual Feedback                                        | Works as expected   |
| Create todays' log button  | Click      | Create a new log for that day and shows confirmation message | Works as expected   |
| Delete todays' log button  | Hover      | Visual Feedback                                        | Works as expected   |
| Delete todays' log button  | Click      | Pops up confirmation message and allows user to cancel or delete log| Works as expected   |
| Edit limits button         | Hover      | Visual Feedback                                        | Works as expected   |
| Edit limits button         | Click      | Redirects user to settings page                        | Works as expected   |
| Log History button         | Hover      | Visual Feedback                                        | Works as expected   |
| Log History button         | Click      | Redirects user to log history page                     | Works as expected   |
| View Driving Limits        | View       | Shows Daily and trip limit that is customisable by user| Works as expected   |

### Log Summary Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|
| View today's summary       | View       | Shows total driving time, time remaining and alerts    | Works as expected   |
| Trip Summary (when none)   | View       | Clearly states No trips logged for this day            | Works as expected   |
| Trip Summary               | View       | List's trips start time and end time and duration      | Works as expected   |
| Trip Summary               | View       | Displays whether trip exceeded user parameters         | Works as expected   |
| Add trip button            | Hover      | Visual Feedback                                        | Works as expected   |
| Add trip button            | Click      | Redirects user to create trip form                     | Works as expected   |
| Edit trip button           | Hover      | Visual Feedback                                        | Works as expected   |
| Edit trip button           | Click      | Redirects user to trip form                            | Works as expected   |
| Delete trip button         | Hover      | Visual Feedback                                        | Works as expected   |
| Delete trip button         | Click      | Pops up confirmation message and allows user to cancel or delete trip| Works as expected  |
| View Driving Limits        | View       | Shows Daily and trip limit that is customisable by user| Works as expected   |
| Edit limits button         | Hover      | Visual Feedback                                        | Works as expected   |
| Edit limits button         | Click      | Redirects user to settings page                        | Works as expected   |
| Log History button         | Hover      | Visual Feedback                                        | Works as expected   |
| Log History button         | Click      | Redirects user to log history page                     | Works as expected   |
| Back to dashboard button   | Hover      | Visual Feedback                                        | Works as expected   |
| Back to dashboard button   | Click      | Redirects user to Dashboard page                       | Works as expected   |
| Create trip form           | Choose start and finish time | allows user to create a trip         | Works as expected  |
| Create trip form           | Overnight trip| allows user to have an end time before start time if over night trip | Works as expected  |
| Create trip form           | Does not allow trips to overlap                                     | Works as expected  |

### Settings Page

| Feature         | Action           | Expected Result                     | Works?              |
|-----------------|------------------|-------------------------------------|---------------------|
| Change max hours| Submit           | New values saved                    | Works as expected   |
| Form validation | Incomplete fields| Prevents submission                 | Works as expected   |
| Back to default button    | Hover  | Visual Feedback                     | Works as expected   |
| Reset to default  button    | Click| Resets driving limits to default    | Works as expected   |
| Reset to default  button    | Click| Shows message confirming reset      | Works as expected   |
| Back to dashboard button    | Hover| Visual Feedback                     | Works as expected   |
| Back to dashboard button   | Click | Redirects user to Dashboard page    | Works as expected   |

---

### History Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|
| History of logs            | View       | Shows log history with total time driven for each day  | Works as expected   |
| History of logs            | View       | Shows if time driven for day was in limit              | Works as expected   |
| View log button            | Hover      | Visual Feedback                                        | Works as expected   |
| View log button            | Click      | redirects to day summary for specific day              | Works as expected   |
| Delete log button          | Hover      | Visual Feedback                                        | Works as expected   |
| Delete log button          | Click      | Pops up confirmation message and allows user to cancel or delete log| Works as expected  |
| Back to dashboard button   | Hover      | Visual Feedback                                        | Works as expected   |
| Back to dashboard button   | Click      | Redirects user to Dashboard page                       | Works as expected   |
| Create log button          | Click      | Redirects user to Create log form                      | Works as expected  |
| Create log form            | Choose day | Only allows user to create a day 2 days before         | Works as expected  |
| Create log form            | Duplicate  | error message if user tries to create duplicate log    | Works as expected  |

## User Stories Testing

## Validator Testing

## Bugs


---

* [Back To Top](#Testing)