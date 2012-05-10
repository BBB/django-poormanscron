Django Poor Man's Cron is Django app which makes use of spambots, search engine indexing robots and alike to run scheduled tasks in approximately regular intervals.

This app isn't meant to be a fully-featured project, but rather a modifiable experimental concept.

To install the app, do the following:

+ Check it out and put it somewhere under python path.
+ Add the app to INSTALLED_APPS and its PoorMansCronMiddleware class to MIDDLEWARE_CLASSES in your project settings.
+ Run python manage.py syncdb to update the DB schema.
+ Create management commands for scheduled tasks (probably you can also use Django Command Extensions).
+ Create ScheduledTask objects in Django administration.

	INSTALLED_APPS = (
	    # ...
	    "poormanscron",
	    )

	MIDDLEWARE_CLASSES = (
	    # ...
	    "poormanscron.middleware.PoorMansCronMiddleware",
	    )
	    
The included initial_data fixture serves as an example where "cleanup" command is called every day after 3 am.