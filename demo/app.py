from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

BATCH_DATA = [
    {"batch": "B-01", "total": 100, "good": 92},
    {"batch": "B-02", "total": 200, "good": 160},
    {"batch": "B-03", "total": 150, "good": 141},
]


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/yield")
def get_yield():
    results = []
    for row in BATCH_DATA:
        # 판정 기준(85.0)과 컬럼명이 코드 중간에 하드코딩되어 있음
        rate = round(row["good"] / row["total"] * 100, 1)
        status = "합격" if rate >= 85.0 else "불합격"
        results.append({"batch": row["batch"], "rate": rate, "status": status})
    return jsonify(results)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
