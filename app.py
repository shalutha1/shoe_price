import string
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def prediction(lst):
    filename = 'D:\ML\sample pro\Regression\shoe price\shoe\model\shoe_predictor (1).pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value



@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0  # Initialize pred with a default value

    if request.method == 'POST':
        brand = request.form['brand']
        type = request.form['type']
        sex = request.form['sex']
        size = request.form['size']
        color = request.form['color']
        material = request.form['material']
       

        feature_list = []
        
        

        brand_list = ['nike', 'adidas', 'reebok', 'converse', 'puma', 'vans', 'new balance', 'asics', 'fila', 'skechers']
        type_list = ['sport', 'casual', 'fashion', 'lifestyle', 'slides', 'retro']
        feature_list.append(float(size))
        color_list = ['black', 'white', 'grey', 'black/white', 'pink', 'other']
        material_list = ['mesh', 'leather', 'canvas', 'primeknit', 'leather/synthetic', 'synthetic','mesh/synthetic', 'suede/mesh', 'suede/canvas', 'suede', 'flyknit', 'knit', 'nylon', 'other']
        gender_list = ['male',"female"]

        

        def traverse(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)


        traverse(brand_list, brand)
        traverse(type_list, type)
        traverse(color_list, color)
        traverse(material_list, material)
        traverse(gender_list, sex)

        #print(feature_list)

        pred = prediction(feature_list)*300
        pred = np.round(pred[0])

    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
