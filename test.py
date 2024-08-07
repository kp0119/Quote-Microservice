import zmq

def fetch():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string("Get Quote")
    response = socket.recv_string()

    return response
def quote_1():
    quote = fetch()
    print(quote)

def quote_2():
    quote = fetch()
    print(quote)

def quote_3():
    quote = fetch()
    print(quote)

if __name__ == "__main__":
    quote_1()
    quote_2()
    quote_3()
