from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated Cat behavior data

cat_behavior = {
    "state": "sleeping",
    "hunger": 5,
    "energy": 10
}


@app.route('/')
def home():
    return "Welcome to the Cat Simulator!"


@app.route('/cat/status', methods=['GET'])
def get_status():
    return jsonify(cat_behavior)


@app.route('/cat/feed', methods=['POST'])
def feed_cat():
    if cat_behavior['hunger'] > 0:
        cat_behavior['hunger'] -= 1
        response = "You fed the cat. Hunger level now {}.".format(cat_behavior['hunger'])
    else:
        response = "The cat is not hungry."
    return jsonify({"message": response, "cat": cat_behavior})


@app.route('/cat/play', methods=['POST'])
def play_with_cat():
    if cat_behavior['energy'] > 0:
        cat_behavior['energy'] -= 1
        cat_behavior['state'] = "playing"
        response = "You played with the cat. Energy level now {}.".format(cat_behavior['energy'])
    else:
        response = "The cat too tired to play"
    return jsonify({"message": response, "cat": cat_behavior})


@app.route('/cat/sleep', methods=['POST'])
def cet_sleep():
    cat_behavior['energy'] += 1
    cat_behavior['state'] = "sleeping"
    response = "The cat sleeping now. Energy level now {}.".format(cat_behavior['energy'])
    return jsonify({"message": response, "cat": cat_behavior})


if __name__ == "__main__":
    app.run(debug=True)
