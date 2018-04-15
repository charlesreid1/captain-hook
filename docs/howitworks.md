# How Captain Hook Works

Captain Hook is a flask web server that runs in Python.

Captain Hook provides URL endpoints that web services
can use to pass JSON data into Captain Hook. That JSON
data contains information about the event that occurred.
For example, it might contain information about a git
commit to a repository, and information about the 
repository, and the user, etc.

Flask makes it easy to define routes that serve as 
API endpoints, and it allows parsing the JSON data
in Python and using Python functionality to perform
the webhook actions desired.

When an event occurs, the web service will send off
a JSON payload to Captain Hook, which will accept it
and run whichever Python function was associated with
that endpoint route.

Captain Hook runs on #blackbeard.

