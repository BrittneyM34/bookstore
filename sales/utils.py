from books.models import Book
from io import BytesIO
import base64
import  matplotlib.pyplot as plt

# define a function that takes the ID
def get_bookname_from_id(val):
    # this ID is used to retrieve the name from the record
    bookname=Book.objects.get(id=val)
    return bookname

def get_graph():
    # create a BytesIO buffer for the image
    buffer = BytesIO()

    # create a plot with a bytesIO object as a file-like object
    plt.savefig(buffer, format='png')

    # set cursor to the beginning of the stream
    buffer.seek(0)

    # retrieve the content of the file
    image_png = buffer.getvalue()

    # encode the bytes-like object
    graph = base64.b64decode(image_png)

    # decode to get the string as output
    graph = graph.decode('utf-8')

    # free up the memory of buffer
    buffer.close()

    # return the image/graph
    return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    # switch plot backed to Anti-Grain Geometry - to write to file
    plt.switch_backend('AGG')

    # specify figure size
    fig=plt.figure(figsize=(6,3))

    # select chart_type based on user input from the form
    if chart_type == "#1":
        # plot bar chart between date on x-axis and quantity on y-axis
        plt.bar(data['date_created'], data['quantity'])

    elif chart_type == '#2':
        # generate pit chart based on the price
        # the book titles are sent from the view as labels
        labels=kwargs.get('labels')
        plt.pie(data['price'], lables=labels)

    elif chart_type == '#3':
        # plot line chart based on date on x-axis and price on y-axis
        plt.plot(data['date_created'], data['price'])
    else:
        print('unknown chart type')

    # specify layout details
    plt.tight_layout()

    # render the graph to file
    chart = get_graph()
    return chart