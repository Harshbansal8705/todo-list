from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

rows = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        file = open("static/files/todo-data.csv")
        csvreader = csv.reader(file)
        # next(csvreader)
    return render_template("index.html", csvreader=csvreader)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        file = open("static/files/todo-data.csv")
        csvreader = csv.reader(file)
        # next(csvreader)
        return render_template("index.html", csvreader=csvreader, form=True, sno=None)
    if request.method == "POST":
        task = request.form.get('task')
        sno = request.form.get("sno")
        status = request.form.get("status")
        if not task:
            return redirect("/")
        # print(sno==None)
        # print(task)
        # print(status)
        if not sno:
            with open("static/files/todo-data.csv", "r") as file:
                csvReader = csv.reader(file)
                # next(csvReader)
                for row in csvReader:
                    # print(type(row[0]))
                    sno = int(row[0]) + 1
        # with open("static/files/todo-data.csv", "a") as file:
        #     csvWriter = csv.writer(file)
        #     csvWriter.writerow([sno, task, status])
        lines = list()
        with open("static/files/todo-data.csv", "r") as file:
            csvreader = csv.reader(file)
            # next(csvreader)
            print(type(sno), ":", sno)
            for row in csvreader:
                if row[0] != sno:
                    lines.append(row)
                else:
                    lines.append([sno, task, status])
                print(lines)

        with open("static/files/todo-data.csv", "w") as file:
            csvwriter = csv.writer(file)
            # csvwriter.writerow(["sno", "task", "status"])
            csvwriter.writerows(lines)
            
    return redirect("/")

@app.route("/delete/<string:sno>")
def delete(sno):
    lines = list()
    with open("static/files/todo-data.csv", "r") as file:
        csvreader = csv.reader(file)
        # next(csvreader)
        print(type(sno), ":", sno)
        for row in csvreader:
            if row[0] != sno:
                lines.append(row)
            print(lines)

    with open("static/files/todo-data.csv", "w") as file:
        csvwriter = csv.writer(file)
        # csvwriter.writerow(["sno", "task", "status"])
        csvwriter.writerows(lines)
    return redirect("/")

@app.route("/edit/<string:sno>", methods = ["GET", "POST"])
def edit(sno):
    if request.method == "GET":
        file = open("static/files/todo-data.csv", "r")
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == sno:
                status = row[2]
                task = row[1]
                return render_template("index.html", sno=sno, status=status, task=task, csvreader=csvreader, form=True)
    
    if request.method == "POST":
        sno = request.form.get("sno")
        task = request.form.get("task")
        status = request.form.get("status")
        print(sno, task, status)
        lines = list()
        with open("static/files/todo-data.csv", "r") as file:
            csvreader = csv.reader(file)
            # next(csvreader)
            print(type(sno), ":", sno)
            for row in csvreader:
                if row[0] != sno:
                    lines.append(row)
                else:
                    lines.append(sno, task, status)
                print(lines)

        with open("static/files/todo-data.csv", "w") as file:
            csvwriter = csv.writer(file)
            # csvwriter.writerow(["sno", "task", "status"])
            csvwriter.writerows(lines)

    return redirect("/")
    # lines = list()
    # with open("static/files/todo-data.csv", "r") as file:
    #     csvreader = csv.reader(file)
    #     for row in csvreader:

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)