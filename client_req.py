import zmq
import threading

context = zmq.Context()

def make_request(a):
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5556')
    print(f'Sending request {a} ...')
    socket.send_string(str(a))
    message = socket.recv_string()
    print(f'Received reply from request {a} [{message}]')

for a in range(10):
    thread = threading.Thread(target=make_request, args=(a,))
    thread.start()
