from flask import Flask,jsonify,request
import csv

all_articles=[]

with open('articles.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
disliked_articles=[]
not_watched=[]

app=Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked-articles",methods=["POST"])
def liked_articles():
    articles=all_articles[0]
    some_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-articles",methods=["POST"])
def disliked_articles():
    articles=all_articles[0]
    some_articles=all_articles[1:]
    disliked_articles.append(articles)
    return jsonify({
        "status":"success"
    }),201

@app.route("/not-watched",methods=["POST"])
def not_watched():
    articles=all_articles[0]
    some_articles=all_articles[1:]
    not_watched.append(articles)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()    