#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import socket
from time import strftime, gmtime

__author__ = 'Josh Maine'


class TeamCymruApi():
    def __init__(self):
        self.cymru = 'hash.cymru.com'

    def get_cymru(self, this_hash):
        """ Return Team Cymru Malware Hash Database results.

        The Malware Hash Registry (MHR) project is a look-up service similar to
        the Team Cymru IP address to ASN mapping project. This project differs
        however, in that you can query our service for a computed MD5 or SHA-1
        hash of a file and, if it is malware and we know about it, we return the
        last time we've seen it along with an approximate anti-virus detection percentage.

        :param this_hash: Can be a md5 or sha1 hash.
        :return: result dictionary or socket error

        Example Output::

            {
                'detected': '86',
                'last_seen': '01-06-2014T22:34:57Z'
            }

        """
        request = '%s\r\n' % this_hash
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.cymru, 43))
            s.send('begin\r\n')
            s.recv(1024)
            s.send(request)
            response = s.recv(1024)
            s.send('end\r\n')
            s.close()
            if len(response) > 0:
                resp_re = re.compile('\S+ (\d+) (\S+)')
                match = resp_re.match(response)
                return {'last_seen': strftime("%m-%d-%YT%H:%M:%SZ", gmtime(int(match.group(1)))),
                        'detected': match.group(2)}
        except socket.error:
            return dict(error='socket error')
