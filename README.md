# Lifestyle Tracker

##### What does this project do?
- Lifestyle Tracker is a web application that keeps track of your lifestyle daily, so that you will understand more about your lifestyle and then act to achieve your goals.
- Lifestyle Tracker keeps track of your sleep time, weight, and whether you exercised and ate your meals.
- You can track your data through ine charts showing how long you've slept and your weight over days, as well as pie charts showing how many days you've exercised, ate breakfast, lunch and dinner.
- Each chart has a title showing more information such as average sleep duration, average weight, and fraction of days you've exercised, ate breakfast, lunch and dinner.
- It is an open-source project, so you may edit your inputs and outputs to create a personalized application.

##### Why is this project useful?
- Lifestyle Tracker is useful because it is free and open-source!
- There are many health trackers available.
- Some require you to manually input your health data everyday, but these inputs may not be what you want to keep track of!
- Others automatically keep track of your health data (e.g. apple watch), but they are very pricey!
- With this free, open-source project, you can create a custom web application for free!
- Of course, you have to manually input data everyday, but by doing this, you can actually become more conscious about your lifestyle!

##### How to get started?
- Start by git cloning this project.
- Python 3.7 or above is required and flask, flask-sqlalchemy, and flask-login must be installed through pip or conda.
- You have to run the following command:
  `export FLASK_APP=main.py`
  `flask run --host=0.0.0.0`
- After that, an http link to the web app is displayed.
- Note: you can only enter the web app if you are connected to the same wifi.

##### Where can people get more help if needed?
- For help, you may send an email to habinbea@handong.ac.kr.
- If there are any problems, please write them in the issues board.

##### Presentation (YouTube) link
- 

##### Github repository link of backbone code
- https://github.com/techwithtim/Flask-Web-App-Tutorial

##### Contribution
- Created an input page where users can input the date of entry, sleep start time, sleep end time, weight, whether they exercised, and whether they ate breakfast, lunch and dinner.
- Created an output page where users can see their lifestyle through charts and raw data
  - Charts include a line graph of sleep duration over days, a line graph of weight over days, a pie chart of days exercised and skipped exercise, a pie chart of days ate breakfast and skipped breakfast, a pie chart of days ate lunch and skipped lunch, and a pie chart of days ate dinner and skipped dinner.
  - The title of the charts also show the average sleep duration, average weight, the number of days exercised, ate breakfast, lucnh and dinner out of total number of days
  - The raw data shows the raw data in the database whose columns are: date, sleep start, sleep end, sleep duration, weight, exercise, breakfast, lunch, and dinner.
  - From the raw data, users can click the "x" button on the right side of an entry to delete it in the database. When this is done, the charts and data are updated immediately.
