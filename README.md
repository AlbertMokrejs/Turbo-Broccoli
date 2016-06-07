# Calendar-based Club Management System


##General Proposal:
**Replace the Stuyvesant Student Union's current google calendar with one that**

1. makes sense with the current design.
2. has features not provided by google calender but required by the client

##Goals:
1. 5/13/16
  * ~~General Proposal~~
  * ~~Goals~~
2. 5/16/16
  * Implement javascript so that the calender automatically formats to current month.
  * Find appropriate bootstrap.
3. 5/20/16
  * Complete the form required to reserve the room.
4. 5/25/16
  * Adjust the calendar to fit the needs of club managers.
5. 5/27/16
  * Include maps of rooms
6. 6/6/16
  * Finish extraneous bugs and design choices

##ChangeList:
1. (Shawn) 05/11/16: Made readme skeleton
  * Need general proposal
  * Need to determine schedule/goals
2. (Sarah) 05/11/16: Made basic calendar css
3. (Derry) 5/18/16: Path file started. Login and Register paths set up
4. (Derry, Albert) 5/20/16: Login and Register both function. Now needs some css.
5. (Sarah) 5/23/16: Calender css updated, Calender js up
6. (Derry, Albert, Shawn) 5/25/16: JS for login and register up, form js up, form currently being worked on
7. (Shawn, Sarah) 5/26/16: Form working, calender updated
8. (Shawn) 5/27/16: home.html janga up, working on redirects on the homepage
9. (Derry, Albert, Shawn) 5/28/16: Specific reservations page added, route added, functions in backend added

## Contributors
|**Profile Picture**|    **Name**    |    **Role**    |    **Github**    |
|-------------------|:--------------:|:--------------:|:----------------:|
|<img src="images/albert.jpg" width="100" height="100" />|Albert Mokrejs|Back End|[@AlbertMokrejs](https://github.com/AlbertMokrejs/)|
|<img src="images/shawn.jpg" width="100" height="100" />|Shawn Li|Front End|[@TyranitarShawn](https://github.com/TyranitarShawn/)|
|<img src="images/derry.jpg" width="100" height="100" />|Derry|Middleware|[@Ericil](https://github.com/Ericil/)|
|<img src="images/sarah.jpg" width="100" height="100" />|Sarah Joseph|Front/Middle|[@sarahjoseph723](https://github.com/sarahjoseph723/)|

## Deployment

* run the following code:

> sudo apt-get update

> sudo apt-get install python-pip python-dev nginx

> sudo pip install virtualenv

> mkdir ~/stuylendar

> cd ~/stuylendar

> virtualenv stuylendarenv

> source stuylendarenv/bin/activate

> pip install uwsgi flask

* open stuylendar.conf
 * replace all instances of "<user>" within the file so that "/home/<user>/myproject/stuylendarenv/bin" points to the app's virtual enviroment
 * move the file to "/etc/init/stuylendar.conf" (this enables auto-startup)

* open stuylendar (the file with no file extension)
 * replace "<IP/Domain>" with the website's Domain
 * replace "<user>" so that "/home/<user>/stuylendar/stuylendar.sock" points to the project's socket file
 * move the file to "/etc/nginx/sites-available/stuylendar"

* run the following code:

> sudo ln -s /etc/nginx/sites-available/stuylendar /etc/nginx/sites-enabled

> sudo service nginx restart

This guide and all files are based on [This guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)
