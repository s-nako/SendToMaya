'''
open the saved script and send it to Maya from editor
'''
import socket
import sys
import textwrap
import os
from optparse import OptionParser


parser = OptionParser()

parser.add_option("--file", dest="file", help="The file")
parser.add_option("--host", dest="host", help="The host for the connection to Maya")
parser.add_option("--port", dest="port", help="The port for the connection to Maya")

(options, args) = parser.parse_args()

if options.host is None:
    host = "127.0.0.1".encode('utf-8')
else:
    host = options.host
if options.port is None:
    port = int(7002)
else:
    port = options.port

def SendToMaya(options):
    '''
        send and execute the script
    '''
    PY_CMD_TEMPLATE = textwrap.dedent('''
        import traceback
        import __main__

        namespace = __main__.__dict__
        filepath = 0
        if '__file__' in namespace:
            filepath = namespace['__file__']
        namespace['__file__'] = {2!r}
        print namespace['__file__']
        try:
            {0}({1!r}, namespace, namespace)
        except:
            traceback.print_exc()
        if  filepath:
            namespace['__file__'] = filepath
        else:
            del namespace['__file__']

	''')
    
    file_name = os.path.abspath(options.file)
    command_tpl = PY_CMD_TEMPLATE.format('execfile', file_name, file_name)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print "connected"

    client.send(command_tpl.encode('utf-8'))

    client.shutdown(1)
    while True:
        recvs = client.recv(1024)
        if not recvs:
            break
        else:
            print recvs
    client.close()
    print "closed"

if __name__ == '__main__':
    if options.file:
        SendToMaya(options)
    else:
        sys.exit("No command given")
        