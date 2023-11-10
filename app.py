from flask import Flask, render_template, jsonify,  request, redirect, url_for
from card_employees import data
from labs import card_data
from contact_card import contact_card_list
from timetable import time_table
import pickle
import sqlite3


app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/history')
def history():
    return render_template("history.html",  active_page = 'hist')


@app.route('/labs')
def labs():
    return render_template("labs.html",card_data=card_data, active_page = 'lab')


@app.route('/study')
def study():
    return render_template("study.html", active_page = 'stud')


@app.route('/getTable/<class_id>')
def get_table(class_id):
    if class_id in time_table:
        class_data = time_table[class_id]
        return jsonify(class_data)
    else:
        return jsonify({"error": "Class not found"}), 404


@app.route('/articles')
def articl():
    return render_template("articl.html", active_page = 'articl')

@app.route('/conf')
def conf():
    return render_template("conf.html", active_page = 'conf')

@app.route('/employees')
def empl():
    # conn = sqlite3.connect('polymer_lab.db')
    # cursor = conn.cursor()
    #
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    # table_rows = cursor.fetchall()
    # tables = [row[0] for row in table_rows]
    #
    # data = {}  # Создаем словарь для хранения данных разделов
    #
    # for table in tables:
    #     cursor.execute(f"SELECT * FROM {table}")
    #     employees_list = cursor.fetchall()
    #     data[table] = employees_list
    #
    # conn.close()
    # return render_template('employees.html', data=data, tables=tables, active_page = 'employ')
    return render_template("employees.html", data=data, active_page = 'employ')

def insert_data(cursor, table_name, data):
    placeholders = ', '.join(['?' for _ in data])
    column_names = ', '.join(data.keys())
    query = f'INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})'
    values = tuple(data.values())
    cursor.execute(query, values)

@app.route('/update_employee')
def index():
    return render_template('employee_update.html')

@app.route('/submit', methods=['POST'])
def submit():
    fio = request.form['fio']
    position = request.form['position']
    degree = request.form['degree']
    title = request.form['title']
    phone = request.form['phone']
    email = request.form['email']
    workplace = request.form['workplace']

    conn = sqlite3.connect('polymer_lab.db')
    cursor = conn.cursor()

    data = {
        'employee_id': fio.split()[0],
        'img': 'blue_logo.png',
        'name': fio,
        'dolzh': position,
        'sci_step': degree,
        'sci_zvan': title,
        'phone': phone,
        'email': email
    }
    insert_data(cursor, workplace, data)

    conn.commit()
    conn.close()

    return redirect('update_employee')


@app.route('/contacts')
def contact():
    return render_template("contacts.html", contact_card_list=contact_card_list, active_page = 'contact')

@app.route('/get_employee_data/<string:employee_id>', methods=['GET'])
def get_employee_data(employee_id):
    try:
        with open('employees_modal.pkl', 'rb') as file:
            employee_data = pickle.load(file)
    except FileNotFoundError:
        employee_data = {}
    data = employee_data.get(employee_id, {})
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
