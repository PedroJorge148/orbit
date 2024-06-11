from flask import Flask, render_template, request, jsonify
import cmath

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve_quadratic():
    data = request.json
    a = float(data["a"])
    b = float(data["b"])
    c = float(data["c"])

    if a == 0:
        return jsonify({"result": "Coefficient 'a' cannot be zero."})

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        result = f"Two dicdinct real roots: {root1.real:.2f} and {root2.real:.2f}"
    elif discriminant == 0:
        root = -b / (2 * a)
        result = f"One real root: {root:.2f}"
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        result = f"Two complex roots: {root1} and {root2}"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
