from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# as the user answers questions, their answers get stored in here:
responses = []

@app.route('/')
def survey():
    """Shows the title, the instructions, and a button to start the survey. Directs user to questions/0"""


    return render_template(
        "survey_start.html",
        #title = survey.title
    )

#@app.route('/questions/0')
