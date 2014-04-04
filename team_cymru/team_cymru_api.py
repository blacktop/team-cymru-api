import re
import socket
from time import localtime, strftime

__author__ = 'Josh Maine'

class TeamCymruApi():
    def __init__(self):
        self.cymru = 'hash.cymru.com'

    def get_cymru(self, this_hash):
        """
            Return Team Cymru Malware Hash Database results.
            source: http://code.google.com/p/malwarecookbook/
            site : http://www.team-cymru.org/Services/MHR/
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
                result = "\n\tLast Seen:\t%s\n\tDetected:\t%s" % \
                         (strftime("%b %d %Y", localtime(int(match.group(1)))), match.group(2))
        except socket.error:
            result = "Error"

        print result.lstrip()
        return result