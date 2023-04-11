from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
company = Blueprint('company', __name__, url_prefix='/company')
@company.route("/search", methods=["GET"])
def search(): #ucid - sg342 04/03/2023
    name = request.args.get("name")
    city = request.args.get("city")
    country = request.args.get("country")
    state = request.args.get("state")
    col = request.args.get("col")
    order = request.args.get("order")
    limit = request.args.get("limit",10)
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees
    #  for the company  # don't do SELECT * ucid - sg342 04/03/2023
    query = """SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website, 
    (SELECT count(1) FROM IS601_MP3_Employees e where e.companies_id = IS601_MP3_Companies.id) 
    from IS601_MP3_Companies c, IS601_MP3_Employees e WHERE 1=1 """
    args = {"name":" ","country":" ","state":" ","col":" ","order":" ","limit":" "} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += "AND name like %s"
        rows.append(f"%{name}%")
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += "AND country == %s"
        rows.append(f'%{country}%')
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += "AND state == %s"
        rows.append(f'%{state}%')
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if col in ["name","city","country","state"] \
        and order in ["asc", "desc"]:
        query += f" ORDER BY {col} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        rows.append(int(limit))
    else:
        print("the limit is out of bounds ")
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds  
    limit = +1 # TODO change this per the above requirements
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(f"The error while fetching query results is {str(e)}", "danger")
        error = e
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation   
    allowed_columns =[('name','name'),('city','city'),('country','country'),('state','state')] 
    return render_template("list_companies.html",allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add(): #ucid - sg342 date - 04/03/2023
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.args.get("name")
        address = request.args.get("address")
        city = request.args.get("city")
        state = request.args.get("state")
        country = request.args.get("country")
        zip = request.args.get("zip")
        website = request.args.get("website")
        resp = None
        # TODO add-2 name is required (flash proper error message)
        if name == " ":
            flash('name must be present ','error')
        # TODO add-3 address is required (flash proper error message)
        if address == " ":
            flash('address is required','error')
        # TODO add-4 city is required (flash proper error message)
        if city == " ":
            flash('city is required','error')
        # TODO add-5 state is required (flash proper error message)
        if state ==" ":
            flash('Please enter a state ','error')
        country_code = request.args.get("country_code", default="", type=str)
        states = []
        if country_code.strip():
            states = pycountry.subdivisions.get(country_code=country_code.strip())
        if state not in states:
            flash("Select a state within the country")
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        if country ==" "or country!=list(pycountry.countries):
            flash('Please enter country name','error')     
        # TODO add-6 country is required (flash proper error message) country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        if website == " ":
            flash('website is not required','info')
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        if zip == " ":
            flash('zip code is required please enter properly ','error')
        has_error = False # use this to control whether or not an insert occurs      
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",name,address,city,country,state,zip,website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
                    resp = "Saved record"
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(f'The company was not added to the Table Sorry!!! Try again {str(e)}', "danger")
                resp = e
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit(): # ucid - sg342 date - 04/03/2023
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    row = None
    if not id: # TODO update this for TODO edit-1
        flash('ID is required !!!','error')
    else:
        if request.method == "POST" and request.form.get("name","address","city","state","country","zip","website"):
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name")
            address = request.form.get("address")
            country = request.form.get("country")
            state = request.form.get("state")
            city = request.form.get("city")
            zip = request.form.get("zip")
            website = request.form.get("website")
            print(request.form)
            # TODO edit-2 name is required (flash proper error message)
            if name == " " or None:
                flash('name must be present for updating','error')
            # TODO edit-3 address is required (flash proper error message)
            if address == " " or None:
                flash('address is required for updating','error')
            # TODO edit-4 city is required (flash proper error message)
            if city == " " or None:
                flash('city is required for updating','error')
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation            
            if state ==" " or None:
                flash('Please enter a state ','error')
            country_code = request.args.get("country_code", default="", type=str)
            states = []
            if country_code.strip():
                states = pycountry.subdivisions.get(country_code=country_code.strip())
            if state not in states:
                flash("Select a state within the country")
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            if country ==" "or country!=list(pycountry.countries) or None:
                flash('Please enter a valid country name for updating','error')     
            # TODO edit-7 website is not required
            if website == " " or None:
                flash('website is not required for updating','info')
            # TODO edit-8 zipcode is required (flash proper error message)            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            if zip == " " or None:
                flash('zip code is required please enter properly ','error')
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs            
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""UPDATE IS601_MP3_Companies SET name = %s, address = %s, city = %s,
                    state = %s, country = %s, zip = %s, website = %s WHERE id = %s""", name,address,city,state,country,zip,website,id)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                        row = result.row
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash(f'The company information was not updated due to this error {str(e)}', "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP3_Companies WHERE id = %s",id)
            if result.status:
                row = result.row                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(f'Please address this issue so we can proceed with the information update {str(e)}', "danger")
    # TODO edit-13 pass the company data to the render template
        row = {(name,name),(address,address),(city,city),(state,state),(country,country),(zip,zip),(website,website)}
    return render_template("edit_company.html",row=row)

@company.route("/delete", methods=["GET"])
def delete(): #ucid - sg342 date - 04/03/2023
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    id = request.args.get("id")
    # TODO delete-2 redirect to company search
    args = {**request.args}
    # TODO delete-3 pass all argument except id to this route
    search(args["name"],args["country"],args["state"])
    # TODO delete-4 ensure a flash message shows for successful delete
    if id:
        result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s",id)
        flash("The company was successfully deleted ","info")
        change = DB.update("UPDATE IS601_MP3_Employees WHERE company_id=%s SET company_id=%s",id,None)
    else:
        flash("This id is not present in our database please recheck the id","error")
        search(args["name"],args["country"],args["state"])
    del args[id]
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    return redirect(url_for("company.search"),**args)
    