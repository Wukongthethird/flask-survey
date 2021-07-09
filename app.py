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
def survey_page():
    """Shows the title, the instructions, and a button to start the survey. Directs user to questions/0"""
    return render_template(
        "survey_start.html",
        title = survey.title,
        instructions = survey.instructions
    )

#get makes a request/ or retrieve from cache adn not let domain know.
# post actually does the request, like a log out button
# something to redirect
@app.route('/begin', methods=["POST"])
def begin_page():
    """Shows the title, the instructions, and a button to start the survey. Directs user to questions/0"""
    responses.clear()
    return redirect(
        "/questions/0"
    )

# redirect url param 
# for each questions submitted
#question page location should only be the question form
# just a get
#determines if questions are done are not based of len(repsonse )
# passed as data in the template
# redirect if out of order 
# when to render and when to redirect

@app.route('/questions/<int:question_number>')
def question_page_location(question_number):
    """questions page"""
    current_survey = survey.questions[question_number]

    #var = redirect(f"/questions/{len(responses)}/")
  
    return render_template(
        "question.html",
        question =  current_survey.question,
        choices =  current_survey.choices,
        number = question_number+1
    )


# goes to answser
# saves response and redirect to another questions
#did they complete the survey?
# after every question we should come here
# always redirect from a post when successful not render

@app.route('/answers' , methods = ["POST"])
def question_page_redirector():
    """questions repsonse append"""
    answer = request.form.get("answer")
    responses.append(answer)

    var = None

    if len(responses) == len(survey.questions):
        var = ("/completion")
    else:
        var = (f"/questions/{len(responses)}")

    print("I AM HERE THE RESPONSE", responses)

    return redirect(var)

@app.route('/completion')
def end_page():
    """Shows the title, the instructions, and a button to start the survey. Directs user to questions/0"""
    return render_template("completion.html")





