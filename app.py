from flask import Flask, request, render_template
import logging
import os


from model.model import En_Fre_Translation

# define model path
model_path ='./model/En_Fr_Translation.h5'
#model_path ='model\En_Fr_Translation.h5'

app = Flask(__name__)  

# create instance
model = En_Fre_Translation(model_path)
logging.basicConfig(level=logging.INFO)

def translate(sentence):
    logging.info("translation request received!")
    prediction = model.translate(sentence,21)
    logging.info("translation from model",prediction)

    return prediction

@app.route("/")
def my_form():
    return render_template('index.html')

@app.route("/", methods=['GET','POST'])
def input_text():
    if request.method == 'POST':
        text=request.form['en_sent']
        logging.info("input sentence is =",  text)
        translated = translate(text)
        logging.info("Send translation request!")

    return translate(text)

def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=8000, debug=True) 


if __name__ == "__main__":
    main()
