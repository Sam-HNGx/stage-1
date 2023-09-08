from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api')
def home():
    name = request.args.get('slack_name')
    track = request.args.get('track')
    today = datetime.datetime.now().date().strftime('%A')

    try:
        res = {
            "slack_name": name,
            "current_day": today,
            "utc_time": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": track,
            "github_file_url": "https://github.com/Sam-HNGx/stage-1/blob/3fc862ee6851e969802bc4c12256052dedc87fd8/app.py",
            "github_repo_url": "https://github.com/Sam-HNGx/stage-1.git",
            "status_code": 200
        }

        return jsonify(res)
    except:
        return 'Error fetching queries', 400

if __name__ == '__main__':
    app.run(debug=True)
