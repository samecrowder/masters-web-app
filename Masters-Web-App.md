# Masters-Web-App

This simple web application is intended to faciliate a masters pick-em pool.  It takes a *CSV* with the names of the competitors in the pool and their top 6 golfer picks.  The program then pulls golfer scores from ESPN and displays the standings of the pool, via the templated *masters.html*.  The program is intended to be run through an Apache HTTPD.

## Setup

* Install *apache2* and *mod_wsgi*
* Install *flask* and *jinja2*
* Add `WSGIScriptAlias / /var/www/html/masters/masters.wsgi` to the `/etc/apache2/apache2.conf` file
* Download these files to `/var/www/html/masters`
* Edit *masters.csv*
* Downlaod [jq](https://stedolan.github.io/jq/download/) to `/var/www/html/masters` or to a default binary path
* Start the apache2 daemon

## License

MIT License

Copyright (c) 2016 - 2017 Will Markley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.