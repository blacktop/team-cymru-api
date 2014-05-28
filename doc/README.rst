.. image:: https://raw.githubusercontent.com/blacktop/team-cymru-api/master/doc/logo.png

team-cymru-api
==============

.. image:: https://travis-ci.org/blacktop/team-cymru-api.svg?branch=master
    :target: https://travis-ci.org/blacktop/team-cymru-api

.. image:: https://badge.fury.io/py/team-cymru-api.png
    :target: http://badge.fury.io/py/team-cymru-api

.. image:: https://pypip.in/d/team-cymru-api/badge.png
        :target: https://crate.io/team-cymru-api/requests/

.. image:: http://img.shields.io/gittip/blacktop.svg
        :target: https://www.gittip.com/blacktop/

Team Cymru - Malware Hash Registry API

https://www.team-cymru.org/Services/

Installation
------------
.. code-block:: bash

    $ pip install team-cymru-api


Usage
-----
.. code-block:: python

    import json
    from team_cymru.team_cymru_api import TeamCymruApi

    team_cymru = TeamCymruApi()

    response =  team_cymru.get_cymru('039ea049f6d0f36f55ec064b3b371c46')
    print json.dumps(response, sort_keys=False, indent=4)


Output:
-------
.. code-block:: json

    {
        "last_seen_utc": "2014-01-06T22:34:57Z",
        "response_code": 200,
        "detected": "86"
    }


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
