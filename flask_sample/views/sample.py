from flask import Blueprint, redirect, request, render_template, url_for, flash
import random
from sql.db import DB
sample = Blueprint('sample', __name__, url_prefix='/sample')
@sample.route('/add', methods=['GET', 'POST'])
def create_account():
    account_type = request.form.get("type", None)
    deposit = request.form.get("deposit", None)
    if account_type and deposit>=5:
        try:           
            account_no = "%0.12d" % random.randint(0,999999999999)
            result = DB.insertOne(
                """INSERT INTO IS601_Accounts (account_number,balance,account_type) 
                   VALUES(%s, %s, %s)""",account_no,deposit,account_type)
            if result.status:
                flash("Created Account", "success")
        except Exception as e:
            flash(e, "danger")
    else:
        flash("The account type must be checking and minimum deposit must be 5$","error")
    return render_template("create_account.html")

@sample.route('/list', methods=['GET'])
def list_account():
    account_number = request.args.get("account_number")
    account_type = request.args.get("account_type")
    created = request.args.get("created")
    limit = request.args.get("limit", 5)
    args = []
    query = "SELECT account_number, user_id, balance, account_type, created, modified from IS601_Accounts WHERE 1=1"
    if account_number:
        query += " AND account_number == %s"
        args.append(f"%{account_number}%")
    if account_type:
        query += " AND account_type LIKE %s"
        args.append(f"%{account_type}%")
    if created:
        query += " AND created == %s"
        args.append(f"%{created}%")
    if limit and int(limit) > 0 and int(limit) <= 5:
        query += " LIMIT %s"
        args.append(int(limit))
    rows = []
    try:
        # convert our list to args via *
        print(query)
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        flash(e, "danger")    
    return render_template("list_account.html", resp=rows)

@sample.route('/transaction', methods=['GET','POST']) # will perform transaction in between accounts
def commit_transaction():
    source_account = request.form.get("name")
    destination_account = request.form.get("col")
    amount = request.form.get("order")
    transaction_type = request.form.get("limit", 5)
    memo = request.form.get("memo")
    if source_account is None:
        flash("The Source Bank Account must be inserted","error")
        return redirect("sample.commit_transaction")
    if destination_account is None:
        flash("The destination account must be inserted","error")
        return redirect("sample.commit_transaction")
    if amount is None:
        flash("There must be a minimum amount of 1.00$","warning")
        return redirect("sample.commit_transaction")
    else:
        if request.method == "POST":
            try:
                result = DB.insertOne("""INSERT INTO IS601_Transactions (account_src,account_dest,balance_change,transaction_type,memo) 
                   VALUES(%s, %s, %s,%s,%s)""",source_account,destination_account,amount,transaction_type,memo)
                balance = "SELECT balance FROM IS601_Accounts WHERE 1=1"
                balance = +amount
                deposit = DB.update("""UPDATE IS601_Accounts SET balance = %s WHERE account_number = %s """,balance,source_account)
                if result.status and deposit.status:
                    flash("The transaction was complete","message")
            except Exception as e:
                flash(e, "danger")    
    return render_template("transactions.html")

@sample.route('/deposit', methods=['GET','POST']) #this will perform deposit in which user will deposit money into their account from world account
def deposit():
    acc_no = request.form.get("acc_no")
    type = request.form.get("type")
    amt = request.form.get("amt")
    if acc_no is None:
        flash("Please select the account for deposit","error")
    if type is None:
        flash("Please select the type of account","error")
    if amt<=1:
        flash('Please select an amount greater than 1$',"error")
    else:
        if request.method == "POST":
            try:                
                balance = "SELECT balance FROM IS601_Accounts WHERE 1=1"
                balance = + amt
                world_bal = ("SELECT balance FROM IS601_Accounts WHERE account_umber = %s","000000000000")
                result = DB.update("""UPDATE IS601_Accounts SET balance = %s WHERE account_number = %s """,balance,acc_no)
                query = DB.insertOne("""INSERT INTO IS601_Transactions VALUES (account_src,account_dest,balance_change,transaction_type,memo) 
                    VALUES(%s, %s, %s,%s,%s)""","000000000000",acc_no,amt,"deposit","deposit done by self")
                world_bal = world_bal - amt
                world_acc = DB.update("UPDATE IS601_Accounts SET balance = %s WHERE account_number = %s ",world_bal,"000000000000")
                if result.status and query and world_acc:
                    flash("The deposit has been submitted","message")
            except Exception as e:
                flash(e,"danger")
    return render_template("deposit_into_acc.html")
@sample.route('/withdraw', methods=['GET','POST']) #this will perform withdraw in which user will withdraw money from their account
def withdraw():
    acc_no = request.form.get("acc_no")
    type = request.form.get("type")
    amt = request.form.get("amt")
    balance = "SELECT balance FROM IS601_Accounts WHERE 1=1"
    if acc_no is None:
        flash("Please select the account for deposit","error")
    if type is None:
        flash("Please select the type of account","error")
    if amt<=1 or amt > balance:
        flash('Please select an amount greater than 1$ and less than your total balance',"error")
    else:
        if request.method == "POST":
            try:
                balance = -amt
                result = DB.update("UPDATE IS601_Accounts SET balance = %s WHERE account_number = %s ",balance,acc_no)
                if result.status:
                    flash("The money has been withdrawn","message")
            except Exception as e:
                flash(e,"danger")
    return render_template("withdraw_from_acc.html")

