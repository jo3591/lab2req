from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get form data
    employee_id = request.form['id']
    name = request.form['name']
    department = request.form['department']
    mobile = request.form['mobile']
    salary = request.form['salary']
    
    # Pass the data to the result template
    return render_template('result.html', 
                           employee_id=employee_id,
                           name=name,
                           department=department,
                           mobile=mobile,
                           salary=salary)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
