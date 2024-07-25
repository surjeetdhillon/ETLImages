from flask import Flask, render_template, g, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


import collections
def sort_dict(d):    
    return collections.OrderedDict(sorted(d.items()))

@app.route('/all')
def all():
    original_items = [{'item 1': "Banana", 'item 2': "Car"}, {'item 1': "Apple", 'item 2': "Bike"}]
    ods = [sort_dict(d) for d in original_items]
    table_items = [ list(v for _,v in od.items()) for od in ods]
    headers = [k for k,_ in ods[0].items()]
    return render_template('index.html', headers=headers, objects=table_items)