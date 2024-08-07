import pandas as pd
import random
import zmq

file = pd.read_csv('quotes.csv')

# function takes random number and returns the quote + author based on the index in the csv
def get_quote(file):
    randomIndex = random.choice(file.index)
    quote_row = file.loc[randomIndex]
    return quote_row['quote'], quote_row['author']

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Server is running...")

while True:
    message = socket.recv_string()

    if message == 'Get Quote':
        quote, author = get_quote(file)
        response = f'"{quote}" — {author}'
        socket.send_string(response)

    else:
        socket.send_string("Exception occurred")


