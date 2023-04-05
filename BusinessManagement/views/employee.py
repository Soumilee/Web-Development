from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')
import re


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT e.id, e.first_name, e.last_name, e.company_id, c.name
     FROM employees e LEFT JOIN companies c ON e.company_id = c.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    email = request.args.get("email")
    company_id = request.args.get("company_id")
    col = request.args.get("col")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    # TODO search-3 append like filter for first_name if provided
    if first_name:
        query += "AND name like %s"
        args.append(f"%{first_name}%")
    # TODO search-4 append like filter for last_name if provided
    if last_name:
        query += "AND name like %s"
        args.append(f"%{last_name}%")
    # TODO search-5 append like filter for email if provided
    if email:
        query += "AND name like %s"
        args.append(f"%{email}%")
    # TODO search-6 append equality filter for company_id if provided
    if company_id:
        query += "AND country == %s"
        args.append(f'%{company_id}%')
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if col in ["name","city","country","state"] \
        and order in ["asc", "desc"]:
        query += f" ORDER BY {col} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    else:
        print("Limit out of bounds")
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    limit = +1 # TODO change this per the above requirements
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation   
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        first_name = request.args.get("first_name")
        last_name = request.args.get("last_name")
        company_id = request.args.get("company_id")
        email = request.args.get("email")
        # TODO add-2 first_name is required (flash proper error message)
        if first_name == " ":
            flash(" The first name of employee is rquired ","error")
        # TODO add-3 last_name is required (flash proper error message)
        if last_name == " ":
            flash(" The last name of employee is rquired ","error")
        # TODO add-4 company (may be None)
        if company_id == None:
            flash(" The company id maybe empty ","info")
        # TODO add-5 email is required (flash proper error message)
        if email == " ":
            flash(" The first name of employee is rquired ","error")
        # TODO add-5a verify email is in the correct format
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex,email)):
            print("The email is valid")
        has_error = False # use this to control whether or not an insert occurs            
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees VALUES (first_name,last_name,company_id,email) VALUES (%s,%s,%s,%s)
                """,first_name,last_name,company_id,email) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(f'The insertion could not be completed du to thid error {str(e)}', "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get(id)
    if not id: # TODO update this for TODO edit-1
        flash("Id is required for editing !!! ","error")
    else:
        if request.method == "POST":            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            company_id = request.args.get("company_id")
            email = request.args.get("email")
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == " ":
                flash("Warning First name of employee required !!","error")
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == " ":
                flash(" The last name of employee is rquired ","error")
            # TODO edit-4 company (may be None)
            if company_id == None:
                flash(" The company id maybe empty ","info")
            # TODO edit-5 email is required (flash proper error message)
            if email == " ":
                flash(" The first name of employee is rquired ","error")
            # TODO edit-5a verify email is in the correct format
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(regex,email)):
                print("The email is valid")
            has_error = False # use this to control whether or not an insert occurs
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s""",
                    first_name,last_name,company_id,email,id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash(f'The updation was not done due to {str(e)}', "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.company_id, e.email FROM IS601_MP3_Employees e 
            LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id = %s WHERE 1=1 """, id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html",row=row, result=result)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    id = request.args.get(id)
    # TODO delete-2 redirect to employee search
    args = {**request.args}
    # TODO delete-3 pass all argument except id to this route
    if id:
        result = DB.delete( "DELETE FROM IS601_MP3_Employees WHERE id = %s",id)
        del args["id"]
        flash("The employee was successfully deleted from DB","info")
    else:
        flash("Without id deletion cannot be performed","warning")
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    return redirect(url_for("employee.search", **args))