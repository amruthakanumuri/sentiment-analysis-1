from flask import Flask, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template('index.html')

@app.route('/review', methods=['POST', 'GET'])
def review():
    if request.method == 'POST':
        paragraph = request.form['text']
        analyser = SentimentIntensityAnalyzer()
        result = analyser.polarity_scores(paragraph)
        score = result['compound']
        senti = None
        score = round(score,1)
        if (score<=1 and score>=0.5):
          senti ='V.Positive'
        elif (score<0.5 and score>0):
          senti = 'Positive'
        elif (score==0):
          senti = 'Neutral'
        elif (score<0 and score>=-0.5):
          senti = 'Negative'
        else:
           senti = 'V.Negative'
        return render_template('sentiment.html',value=score,sentiment=senti)

    else:
        return render_template('error.html')



if __name__ == "__main__":
    app.run(debug=True)