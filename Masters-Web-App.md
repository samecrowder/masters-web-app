# Masters-Web-App

This simple web application is intended to faciliate a masters pick-em pool.  It takes a *CSV* with the names of the competitors in the pool and their top 6 golfer picks.  The program then pulls golfer scores from ESPN and displays the standings of the pool, via the templated *masters.html*.  The program is intended to be run through an Apache HTTPD.

## Setup

* Install *apache2* and *mod_wsgi*
* Add `WSGIScriptAlias / /var/www/html/masters/masters.wsgi` to the `/etc/apache2/apache2.conf` file
* Download these files to `/var/www/html/masters`
* Edit *masters.csv*
* Downlaod [jq](https://stedolan.github.io/jq/download/) to `/var/www/html/masters` or to a default binary path
* Start the apache2 daemon