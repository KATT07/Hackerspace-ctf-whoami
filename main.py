from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def hello():
    site = '''<html>
<title>Hey whats my name</title>
<style>
    p{
    color:white;
    }
</style>
<h1>What's my name</h1>
<p>text is hidden somewhere on the site fine out where</p>
</html>
'''
    response = make_response(site)
    response.set_cookie("Identity","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYWNrZXJ7VV9HMFRfMUhFX0ozVF9GTDhHfSIsIm5hbWUiOiJIZWlzZW5iZXJnIiwiaWF0IjoxNTE2MjM5MDIyfQ.aaJGEWFer2En4lEh-_z4VMY8grHhtO0hAMWzoUnpNrw")
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
