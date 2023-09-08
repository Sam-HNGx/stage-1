from flask import Flask, request, jsonify
import datetime, time

app = Flask(__name__)

@app.route('/api')
def home():
    name = request.args.get('name')
    track = request.args.get('track')
    today = datetime.date.today()
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    try:
        res = {
            "slack_name": name,
            "current_day": days_of_the_week[datetime.date.weekday(today)],
            "time": time.strftime("%H:%M:%S", time.localtime()),
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
