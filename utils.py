import json


def load_candidates_from_json(path):
    with open(path, encoding='UTF-8') as f:
        f = json.load(f)
    return f


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json('candidates.json'):
        if candidate['id'] == candidate_id:
            return candidate
    return 'Not found'


def get_candidate_by_name(candidate_name):
    for candidate in load_candidates_from_json('candidates.json'):
        if candidate_name.lower() in candidate["name"].lower():
            return candidate
    return 'Not found'


def get_candidate_by_skill(skill_name):
    res = []

    for c in load_candidates_from_json('candidates.json'):
        if skill_name.lower() in c['skills'].lower():
            res.append(c)

    return res
