# Masters-Web-App

This simple web application is intended to faciliate a masters pick-em pool.  It takes a *CSV* with the names of the competitors in the pool and their top 6 golfer picks.  The program then pulls golfer scores from ESPN and displays the standings of the pool, via the templated *masters.html*.

## Setup

* Create a cloud formation stack in AWS using `masters-cf-template.yml`

* Create a Zip Archive for Lambda by:

```
## download and unzip the files in this gist
chmod +x golfers.sh

## get jinja and requests dependency
#### assumes virtualenv is installed
virtualenv env
source env/bin/activate
pip install jinja2 -t .
pip install requests -t .
deactivate
rm -rf env

## edit masters.csv with final entries

## zip for lambda
zip -r lambda.zip *

## upload lambda.zip to lambda
```

## License

MIT License

Copyright (c) 2016 - 2023 Will Markley

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
