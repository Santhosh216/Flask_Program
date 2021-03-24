from exceptions import *
from operations import *
from flask import Flask

app = Flask(__name__)

@app.route('/<function>/<int:a>/<int:b>')
def performing_operations(function, a, b):
    obj = Operations(a, b)

    if function == 'add':
        try:
            if a>10 or b >10:
                raise ValueToLarge('value should not greater than 10')
            else:
                return str(obj.add())
        except ValueToLarge as e:
            return str(e)

    elif function == 'sub':
        try:
            if a<b:
                raise ValueToSmall('a value must greater than b')
            else:
                return str(obj.sub())
        except ValueToSmall as s:
            return str(s)
            
    elif function == 'mul':
        return str(obj.mul())
            
    elif function == 'div':
        try:
            if a==0 or b==0:
                raise ZeroNotDivisible('divisible by zero not possible')
            else:
                return str(obj.div())
        except ZeroNotDivisible as d:
            return str(d)

    else:
        return 'Entered function is not valid'
    


if __name__ == '__main__':
    app.run(debug = True, port = 5008)