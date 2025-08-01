# Testing
---
## Contents

* [Browser Compatibility](#browser-compatibility)
* [Responsiveness](#responsiveness)
* [Manual Testing](#manual-testing)
* [User Stories Testing](#user-stories-testing)
* [Lighthouse Testing](#lighthouse-testing)
* [Validator Testing](#validator-testing)
* [Bugs](#bugs)
---

Some sections below contain collapsible screenshots and validation outputs — click each summary to expand and view details.

## Browser Compatibility

The website was tested on multiple browsers to confirm full compatibility and consistent rendering across platforms.

<details>
<summary>Click here to view Chrome screenshot - <strong>Working as Expected</strong></summary>

![Chrome Screenshot](/documentation/compatability/chrome.png)

</details>

<details>
<summary>Click here to view Firefox screenshot - <strong>Working as Expected</strong></summary>

![Firefox Screenshot](/documentation/compatability/firefox.png)

</details>

<details>
<summary>Click here to view Edge screenshot - <strong>Working as Expected</strong></summary>

![Edge Screenshot](/documentation/compatability/edge.png)

</details>

<details>
<summary>Click here to view Opera screenshot - <strong>Working as Expected</strong></summary>

![Opera Screenshot](/documentation/compatability/opera.png)

</details>

## Responsiveness
The site was tested for responsive behaviour across multiple screen sizes and devices. All major content, forms, and controls adjust fluidly across viewport sizes with no layout-breaking issues observed.

**Tested Devices:**
- Google Pixel 8 Pro (Portrait and Landscape)
- 24" 1440p Desktop Monitor
- 24" 1080p Landscape Desktop Monitor
- 24" 1080p Portrait Desktop Monitor
- 34" 1440p Ultra-Wide Monitor

In addition to real device testing, Chrome DevTools’ responsive mode was used throughout development to verify breakpoints and content flow.

<details>
<summary>Click here to view 24" 1440p Desktop Monitor screenshot – <strong>Works as expected</strong></summary>

![1440p Desktop Screenshot](/documentation/responsive/1440p_desktop.png)

</details>

<details>
<summary>Click here to view 24" 1080p Landscape Desktop Monitor screenshot – <strong>Works as expected</strong></summary>

![1080p Landscape Desktop Screenshot](/documentation/responsive/1080p_desktop.png)

</details>

<details>
<summary>Click here to view 24" 1080p Portrait Desktop Monitor screenshot – <strong>Works as expected</strong></summary>

![1080p Portrait Desktop Screenshot](/documentation/responsive/1080p_portrait_desktop.png)

</details>

<details>
<summary>Click here to view 34" 1440p Ultra-Wide Monitor screenshot – <strong>Works as expected</strong></summary>

![Ultra-Wide Screenshot](/documentation/responsive/ultrawide_1440p.png)

</details>

<details>
<summary>Click here to view Google Pixel 8 Pro (Portrait) screenshot – <strong>Works as expected</strong></summary>

![Pixel 8 Pro Portrait Screenshot](/documentation/responsive/pixel8pro_portrait.png)

</details>

<details>
<summary>Click here to view Google Pixel 8 Pro (Landscape) screenshot – <strong>Works as expected</strong></summary>

![Pixel 8 Pro Landscape Screenshot](/documentation/responsive/pixel8pro_landscape.png)

</details>

----
Responsiveness was also demonstrated using short video recordings of real device testing:

- [Google Pixel 8 Pro – Portrait Test](https://drive.google.com/file/d/10eUMt4fQAiNPTXftHLw7Ml7OJQt9P0Wp/view?usp=drive_link)  
- [Google Pixel 8 Pro – Landscape Test](https://drive.google.com/file/d/1Q2A0s3Khq_xtYin5kUAfGEvWzmfDBPma/view?usp=drive_link)

All navigation menus, forms, buttons, summaries, and tables were confirmed to be usable at small screen widths. The layout adapts seamlessly.


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
| Create trip form           | Form Submit| Does not allow trips to overlap                        | Works as expected  |

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

All key user stories were implemented and tested. Screenshots demonstrating the implementation of each user story can be found in the [README User Stories section](/README.md#user-stories).

### Must Have

| User Story                                                                 | Feature or Page           | Test Description                                                                 | Works?             |
|----------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|---------------------|
| As a first-time user, I want to register and log in so I can access my logs. | Authentication (Allauth)  | Registered and logged in using form; redirects to dashboard                     | Works as expected   |
| As a returning user, I want to log trips with start and finish times.     | Trip Form (Dashboard)     | Trip input saved with start/finish; JS + backend validation used                | Works as expected   |
| As a user, I want to view today’s trips and see total drive time.         | Dashboard summary + Daily Summary | Trips shown in list with total time updated dynamically                         | Works as expected   |
| As a user, I want to edit or delete trips in case I make a mistake.       | Trip list (Daily Summary)     | Each trip can be edited and deleted           | Works as expected   |
| As a user, I want to know if I’ve exceeded my daily or trip time limits.  | Dashboard and daily summary| limits exceeded warnings show on dashboard and daily summary page           | Works as expected   |
| As a user, I want my data to be private and secure (only visible to me).  | Backend models/views       | Trips are user-linked via ForeignKey; only authenticated user can access them   | Works as expected   |
| As an admin, I want to view/edit/delete any records from the admin panel. | Django Admin               | Admin tested for access to DayLogs, Trips, and Settings                         | Works as expected   |

### Should Have

| User Story                                                                 | Feature or Page           | Test Description                                                                 | Works?             |
|----------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|---------------------|
| Ability to edit Day Logs                                                  | Dashboard / Not available | This can be done via the history page only                                        | Works as expected     |
| Visual cues when over driving limits                                    | Dashboard/daily summary alerts| Red text appear showing when limits exceeded (daily or per trip)            | Works as expected   |
| Input validation: cannot input a trip end time before start unless overnight | Trip form (JS + backend)  | JS blocks invalid times; backend also validates and raises `ValidationError`    | Works as expected   |

### Could Have (Future Development)

| User Story                                                                 | Feature or Page           | Test Description                                                                 | Works?             |
|----------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|---------------------|
| Customizable driving time limits per user *(now implemented)*            | Settings Page             | User can update max trip & daily drive time via a form; new values enforced     | Works as expected   |
| Weekly/monthly driving summaries                                          | Not implemented           | Could be added using date filtering and aggregation                             | Not implemented     |
| CSV export of logs                                                        | Not implemented           | Feature not available in current release                                        | Not implemented     |
| Graphical reports or charts                                               | Not implemented           | No visualisation or charting tools added yet                                   | Not implemented     |

## Lighthouse Testing

Pages were tested using [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) to assess performance, accessibility, best practices, SEO, and PWA readiness.

### Dashboard Page

![Dashboard Lighthouse Report](/documentation/lighthouse/dashboard_lighthouse.png)

### Home Page

![Home Lighthouse Report](/documentation/lighthouse/home_lighthouse.png)

### Daylog Summary Page

![Daylog Summary Report](/documentation/lighthouse/summary_lighthouse.png)

### Settings Page

![Settings Lighthouse Report](/documentation/lighthouse/settings_lighthouse.png)

All scores were consistently high across all categories. Minor accessibility suggestions were already addressed manually, such as ARIA labels and semantic headings.


## Validator Testing

### HTML

All key templates were tested using the [W3C HTML Validator](https://validator.w3.org/).

#### Home Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/home_validation.png)

</details>

#### Dashboard Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/dashboard_validation.png)

</details>

#### Day Summary Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/day_summary_validation.png)

</details>

#### History Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/history_validation.png)

</details>

#### Settings Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/settings_validation.png)

</details>

#### Daylog Form Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/daylog_form_validation.png)

</details>

#### Login Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/login_validation.png)

</details>

#### Logout Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/logout_validation.png)

</details>

#### 404 Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![HTML Validator Result](/documentation/validators/404_validation.png)

</details>

---

### CSS Validation

The custom CSS file was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no errors were found.

<details>
<summary>Click to view validation result - No issues</summary>

![CSS Validation Result](/documentation/validators/css_validation.png)

</details>

---

### JavaScript Validation

Custom JavaScript was tested using [JSHint](https://jshint.com/). The following files were validated:

#### Base Javascript
<details>
<summary>Click to view validation result - No functional issues (some ES6 warnings)</summary>

![JSHint Validator Result](/documentation/validators/base_jshint.png)

</details>

#### Daylog Form Javascript
<details>
<summary>Click to view validation result - No functional issues (some ES6 warnings)</summary>

![JSHint Validator Result](/documentation/validators/daylog_form_jshint.png)

</details>

#### Trip Form Javascript
<details>
<summary>Click to view validation result - No functional issues (some ES6 warnings)</summary>

![JSHint Validator Result](/documentation/validators/trip_form_jshint.png)

</details>

---

### Python (PEP8)

The Python codebase was validated using the [CI Python Linter](https://pep8ci.herokuapp.com/) provided by Code Institute. All files passed without issues. 

#### logger models.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/models_linter.png)

</details>

#### logger views.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/views_linter.png)

</details>

#### logger urls.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/urls_linter.png)

</details>

#### logger forms.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/forms_linter.png)

</details>

#### logger apps.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/apps_linter.png)

</details>

#### logger admin.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/admin_linter.png)

</details>

#### wsgi.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/wsgi_linter.png)

</details>

#### urls.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/root_urls_linter.png)

</details>

#### asgi.py
<details>
<summary>Click to view example linter output</summary>

![Linter Validator Result](/documentation/validators/asgi_linter.png)

</details>

## Bugs

The following bugs were discovered and resolved during development and testing:

---

### Bug: Home page would not render when extending `base.html`

**Issue:**  
The home page failed to load due to a missing template configuration.

![Template does not exist](/documentation/bugs/template_bug.png)

**Solution:**  
Added the required template directory configuration to `settings.py`.

![Missing code](/documentation/bugs/template_bug_solution.png)

---

### Bug: "Time Left to Drive" did not reflect user-defined limits

**Issue:**  
The "Time Left" calculation was using the default limit instead of the user’s custom settings.

![Time left bug](/documentation/bugs/time_left_bug.png)

**Solution:**  
Updated the logic to reference the correct user-specific settings variable.

![Adjusted Code](/documentation/bugs/time_left_bug_solution.png)

---

### Bug: "Reset to Default" button misaligned on Settings page

**Issue:**  
The button alignment was inconsistent due to Bootstrap spacing conflicts.

![Alignment bug](/documentation/bugs/alignment_bug.png)

**Solution:**  
Applied a custom CSS override using `!important` to ensure proper alignment.

![Adjusted Code](/documentation/bugs/alignment_bug_solution.png)

---

**All known bugs have been resolved.** No unresolved issues remain at the time of submission.

---

* [Back To Top](#testing)
