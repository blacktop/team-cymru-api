![cymru-api logo](https://raw.githubusercontent.com/blacktop/team-cymru-api/master/doc/logo.png)

team-cymru-api
=========
[![PyPI version](https://badge.fury.io/py/team-cymru-api.svg)](http://badge.fury.io/py/team-cymru-api) [![Build Status](https://travis-ci.org/blacktop/team-cymru-api.svg?branch=master)](https://travis-ci.org/blacktop/team-cymru-api) [![Downloads](https://pypip.in/download/team-cymru-api/badge.png)](https://pypi.python.org/pypi/team-cymru-api/) [![Support blacktop via Gittip](http://img.shields.io/gittip/blacktop.svg)](https://www.gittip.com/blacktop/)

Team Cymru - Malware Hash Registry API

https://www.team-cymru.org/Services/

Installation
-----------

    $ pip install team-cymru-api


Usage
-----
```python
import json
from team_cymru_api import TeamCymruApi

team_cymru = TeamCymruApi()

response =  team_cymru.get_cymru('039ea049f6d0f36f55ec064b3b371c46')
print json.dumps(response, sort_keys=False, indent=4)
```

#### Output:
```json
{
    "last_seen_utc": "2014-01-06T22:34:57Z",
    "response_code": 200,
    "detected": "86"
}
```

Testing
-------

To run the tests:

    $ ./tests

Contributing
------------

1. Fork it.
2. Create a branch (`git checkout -b my_team_cymru_api`)
3. Commit your changes (`git commit -am "Added Something Cool"`)
4. Push to the branch (`git push origin my_team_cymru_api`)
5. Open a [Pull Request](https://github.com/blacktop/team-cymru-api/pulls)
6. Wait for me to figure out what the heck a pull request is...
