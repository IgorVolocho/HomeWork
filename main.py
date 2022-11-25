from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate(pk)
    if candidate == 'Not found':
        return "Не найдено"
    return render_template('candidate.html', candidate=candidate)


@app.route("/candidate/<skill>")
def get_candidate_by_skill(skill):
    candidates = utils.get_candidate_by_skill(skill)
    candidate_amount = len(candidates)
    return render_template('skills.html',
                           candidates=candidates,
                           candidate_amount=candidate_amount,
                           skill=skill)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    candidates = utils.get_candidate_by_name(candidate_name)
    candidate_amount = len(candidates)
    if candidates == "Not found":
        return "Not found"
    return render_template('search.html',
                           candidates=candidates,
                           candidate_amount=candidate_amount)


app.run()
