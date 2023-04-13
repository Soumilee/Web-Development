from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')
import re


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS ucid - sg342 date 04/04/2023
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT e.id, e.first_name, e.last_name, e.company_id, c.name
     FROM IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1"""
    args = {"first_name":"","last_name":"","email":"","company_id":"","col":"","order":"","limit":""} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args ucid - sg342 date 04/04/2023
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    email = request.args.get("email")
    company_id = request.args.get("company_id")
    col = request.args.get("col")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    print(request.args)
    print(request.form)
    # TODO search-3 append like filter for first_name if provided ucid - sg342 date 04/04/2023
    if first_name:
        query += "AND first_name like %s"
        args["first_name"] = (f"{first_name}")
    # TODO search-4 append like filter for last_name if provided ucid - sg342 date 04/04/2023
    if last_name:
        query += "AND last_name like %s"
        args["last_name"] = (f"{last_name}")
    # TODO search-5 append like filter for email if provided ucid - sg342 date 04/04/2023
    if email:
        query += "AND email like %s"
        args["email"] = (f"{email}")
    # TODO search-6 append equality filter for company_id if provided ucid - sg342 date 04/04/2023
    if company_id:
        query += "AND company_id == %s"
        args["company_id"] = (f'{company_id}')
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if col and order:
        if col in ["name","city","country","state"] \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100 ucid - sg342 date 04/04/2023
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %(limit)s"
    else:
        print("Limit out of bounds")
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    limit = +1 # TODO change this per the above requirements
   
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly ucid - sg342 date 04/04/2023
        flash(e, "error")
        error = e
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation 
    allowed_columns = [('first_name','first_name'),('last_name','last_name'),('email','email'),('company_name','company_name')]  
    return render_template("list_employees.html", allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email ucid - sg342 date 04/04/2023
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        company_id = request.form.get("company_id")
        email = request.form.get("email")
        print(request.args)
        print(request.form)
        print("The values that are received is : ",first_name, last_name, email, company_id )
        resp = None
        # TODO add-2 first_name is required (flash proper error message) ucid - sg342 date 04/04/2023
        if first_name == " "or None:
            flash(" The first name of employee is rquired ","error")
        # TODO add-3 last_name is required (flash proper error message) ucid - sg342 date 04/04/2023
        if last_name == " " or None:
            flash(" The last name of employee is rquired ","error")
        # TODO add-4 company (may be None)
        if company_id == " " or None:
            flash(" The company id maybe empty ","info")
        # TODO add-5 email is required (flash proper error message) ucid - sg342 date 04/04/2023
        if email == " " or None:
            flash(" The email is required ","error")
        # TODO add-5a verify email is in the correct format ucid - sg342 date 04/04/2023
        if email != None:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(regex,email)):
                print("The email is valid")
        has_error = False # use this to control whether or not an insert occurs            
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name,last_name,company_id,email) VALUES (%s,%s,%s,%s)
                """,first_name,last_name,company_id,email) # <-- TODO add-6 add query and add arguments ucid - sg342 date 04/04/2023
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly ucid - sg342 date 04/04/2023
                flash(f'The insertion could not be completed due to this error {str(e)}', "danger")
                resp = e
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message) ucid - sg342 date 04/04/2023
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Id is required for editing !!! ","error")
    else:
        if request.method == "POST":            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email ucid - sg342 date 04/04/2023
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            company_id = request.args.get("company_id")
            email = request.args.get("email")
            # TODO edit-2 first_name is required (flash proper error message) ucid - sg342 date 04/04/2023
            if first_name == " " or None:
                flash("Warning First name of employee required !!","error")
            # TODO edit-3 last_name is required (flash proper error message) ucid - sg342 date 04/04/2023
            if last_name == " " or None:
                flash(" The last name of employee is rquired ","error")
            # TODO edit-4 company (may be None)
            if company_id == None:
                flash(" The company id maybe empty ","info")
            # TODO edit-5 email is required (flash proper error message) ucid - sg342 date 04/04/2023
            if email == " " or None:
                flash(" The first name of employee is rquired ","error")
            # TODO edit-5a verify email is in the correct format ucid - sg342 date 04/04/2023
            if email != None:
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if(re.fullmatch(regex,email)):
                    print("The email is valid")
            has_error = False # use this to control whether or not an insert occurs
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query ucid - sg342 date 04/04/2023
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s""",
                    first_name,last_name,company_id,email,id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly ucid - sg342 date 04/04/2023
                    flash(f'The updation was not done due to {str(e)}', "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data ucid - sg342 date 04/04/2023
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.company_id, e.email FROM IS601_MP3_Employees e 
            LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id = %s WHERE 1=1 """, id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly ucid - sg342 date 04/04/2023
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template ucid - sg342 date 04/04/2023
    return render_template("edit_employee.html",row=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id ucid - sg342 date 04/04/2023
    id = request.args.get(id)
    # TODO delete-2 redirect to employee search ucid - sg342 date 04/04/2023
    args = {**request.args}
    # TODO delete-3 pass all argument except id to this route ucid - sg342 date 04/04/2023
    if id:
        result = DB.delete( "DELETE FROM IS601_MP3_Employees WHERE id = %s",id)
        del args["id"]
        flash("The employee was successfully deleted from DB","info")
    else:
        flash("Without id deletion cannot be performed","warning")
    # TODO delete-4 ensure a flash message shows for successful delete ucid - sg342 date 04/04/2023
    # TODO delete-5 if id is missing, flash necessary message and redirect to search ucid - sg342 date 04/04/2023
    return redirect(url_for("employee.search", **args))