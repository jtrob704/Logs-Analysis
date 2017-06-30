# Logs Analysis - Udacity
---
## About
This application is an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The application will output the results of 3 SQL queries. The queries will
answer the following three questions

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started

### Requirements
1. Python 3
2. Vagrant
3. VirtualBox

### Setup
1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Download VagrantFile and `newsdata.sql` file from Udacity
4. Clone this repository

### Running
1. Open a terminal window and type `vagrant up` to start a vagrant session
2. Type `vagrant ssh` to securely log into the vagrant session
3.  `cd` to the folder containing the `logs.py` file
4. Type `python logs.py` to run the Logs Analysis application
