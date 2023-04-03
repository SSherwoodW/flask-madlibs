from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "do_not_share"
debug = DebugToolbarExtension(app)

@app.route("/")
def get_template():
    """show list of stories form."""
    return render_template("select-story.html", stories=stories.values())

@app.route("/questions")
def get_form():

    story_id = request.args["story_id"]
    story = stories[story_id]
    
    prompts = story.prompts

    return render_template("questions.html", story_id=story_id, title=story.title, prompts=prompts)

@app.route("/story")
def get_story():

    story_id = request.args["story_id"]
    story = stories[story_id]
    
    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)