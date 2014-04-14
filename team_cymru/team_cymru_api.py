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

        source: http://code.google.com/p/malwarecookbook/
        site : http://www.team-cymru.org/Services/MHR/
        """
        if vaildate_input(this_hash):
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
                    if 'NO_DATA' in match.group(2):
                        return dict(last_seen_utc=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(int(match.group(1)))),
                                    detected=match.group(2), response_code=404)
                    else:
                        return dict(last_seen_utc=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(int(match.group(1)))),
                                    detected=match.group(2), response_code=200)
            except socket.error:
                return dict(error='socket error', response_code=500)
        else:
            return dict(error='Bad Input', response_code=400)


def vaildate_input(user_input):
    """ Validate File Hash Input.

    :param user_input: Input string
    :return: str Single hash string
    """
    #: Check that input is a string
    #: Check that it is at least as long as a md5 hash
    if len(user_input) >= 32 and isinstance(user_input, basestring):
        found_md5s = __extract_md5_from_hash_list(user_input)
        found_sha1s = __extract_sha1_from_hash_list(user_input)
        #: Check that hash list is not empty or mixed
        if found_md5s and not found_sha1s:
            return found_md5s
        elif found_sha1s and not found_md5s:
            return found_sha1s
        else:
            return False
    return False


def __extract_md5_from_hash_list(data):
    """ Extract all md5 hashes from a string.

    :param data: Input string
    :return: List of md5 hashes or single md5 hash
    """
    found_md5_hashes = re.findall(r'(?i)(?<![a-zA-Z0-9])[a-fA-F0-9]{32}(?![a-zA-Z0-9])', data)
    hash_list = list(set(found_md5_hashes))
    if len(hash_list) == 1:
        return hash_list[0]
    else:
        return hash_list


def __extract_sha1_from_hash_list(data):
    """ Extract all sha1 hashes from a string.

    :param data: Input string
    :return: List of sha1 hashes or single sha1 hash
    """
    found_sha1_hashes = re.findall(r'(?i)(?<![a-zA-Z0-9])[a-fA-F0-9]{40}(?![a-zA-Z0-9])', data)
    hash_list = list(set(found_sha1_hashes))
    if len(hash_list) == 1:
        return hash_list[0]
    else:
        return hash_list