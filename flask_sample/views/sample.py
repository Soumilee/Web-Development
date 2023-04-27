from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_required, current_user
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
            result = DB.insertOne("INSERT INTO IS601_Accounts (account_number,balance,account_type) VALUES(%s, %s, %s)",account_no,deposit,account_type)
            #after the new account is created an id is generated so we have to get that id and insert it into the transaction table
            acc_id = DB.selectOne("SELECT id FROM IS601_Accounts WHERE 1=1")
            #we also have to get the world acc id cannot hard code it since id may change later
            world_id = DB.selectOne("SELECT id FROM IS601_Accounts WHERE account_number = %s","000000000000")
            query = DB.insertOne("""INSERT INTO IS601_Transactions (account_src_id,account_dest_id,balance_change,transaction_type,memo,expected_total) 
                                VALUES(%s, %s, %s, %s, %s, %s)""",acc_id,world_id,deposit,"deposit","account creation",deposit)
            world_bal = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s",world_id)
            world_bal = world_bal - 5 
            query2 = DB.insertOne("""INSERT INTO IS601_Transactions (account_src_id, account_dest_id, balance_change, transaction_type, memo, expected_total)
                                VALUES (%s,%s,%s,%s,%s,%s)""",world_id,acc_id,deposit,"withdraw","withdrawn for account creation",world_bal)
            world_acc = DB.update("UPDATE IS601_Accounts SET balance = %s WHERE id = %s",world_bal,world_id)
            if result.status and query.status and world_acc.status and query2.status:
                flash("Created Account", "success")
                return redirect("list_account.html")
        except Exception as e:
            flash(e, "danger")
            print(e)
    else:
        flash("The account type must be checking and minimum deposit must be 5$","error")
    return render_template("create_account.html")

@sample.route('/list', methods=['GET'])
def list_account():
    user_id = current_user.get_id()
    args = []
    query = "SELECT id,account_number,balance,account_type,created,modified FROM IS601_Accounts WHERE user_id = %s",user_id
    limit = request.args.get("limit", 5)
    if limit and int(limit)>0 and int(limit)<=5:
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
        print(e) 
    return render_template("list_account.html", resp=rows)

@sample.route('/list_transaction', methods=['GET']) # transaction account source and destination will contain the account id NOT account number
def list_transactions():
    user_id = current_user.get_id()
    args = []
    query = "SELECT account_src_id, account_dest_id, balance_change, transaction_type, memo, expected_total, created, modified FROM IS601_Transactions WHERE user_id = %s",user_id
    limit = request.args.get("limit",10)
    if limit and int(limit) > 0 and int(limit) >=10:
        query += " LIMIT %s"
        args.append(int(limit))
    rows = []
    try:
        print(query)
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        flash(e,"danger")
        print(e)
    return render_template("list_transactions.html", resp=rows)

@sample.route('/commit_transaction', methods=['GET','POST']) # will perform transaction in between accounts
def commit_transaction():
    source_account_id = DB.selectAll("SELECT id FROM IS601_Accounts WHERE 1=1")
    destination_account_id = DB.selectAll("SELECT id FROM IS601_Accounts WHERE 1=1")
    amount = request.form.get("amt")
    transaction_type = request.form.get("type")
    memo = request.form.get("memo")
    if source_account_id is None:
        flash("The Source Bank Account must be inserted","error")
        return redirect("sample.commit_transaction")
    if destination_account_id is None:
        flash("The destination account must be inserted","error")
        return redirect("sample.commit_transaction")
    if amount is None:
        flash("There must be a minimum amount of 1.00$","warning")
        return redirect("sample.commit_transaction")
    else:
        if request.method == "POST":
            try:
                result = DB.insertOne("""INSERT INTO IS601_Transactions (account_src,account_dest,balance_change,transaction_type,memo,balance_change) 
                   VALUES(%s, %s, %s,%s,%s)""",source_account_id,destination_account_id,amount,transaction_type,memo)
                balance = "SELECT balance FROM IS601_Accounts WHERE 1=1"
                balance = +amount
                deposit = DB.update("""UPDATE IS601_Accounts SET balance = %s WHERE account_number = %s """,balance,source_account_id)
                if result.status and deposit.status:
                    flash("The transaction was complete","message")
            except Exception as e:
                flash(e, "danger")    
    return render_template("commit_transaction.html",source_account_id=source_account_id,destination_account_id=destination_account_id)

@sample.route('/deposit', methods=['GET','POST']) #this will perform deposit in which user will deposit money into their account from world account
def deposit():
    acc_no = request.form.get("acc_no")
    type = request.form.get("type")
    amt = request.form.get("amt")
    if acc_no is None:
        flash("Please select the account for deposit","error")
    if type is None:
        flash("Please select the type of account","error")
    # amt = int(amt)
    if amt is None or amt<=1:
        flash('Please select an amount greater than 1$',"error")
    else:
        if request.method == "POST":
            try:                
                balance = "SELECT balance FROM IS601_Accounts WHERE 1=1"
                balance = + amt
                world_bal = "SELECT balance FROM IS601_Accounts WHERE account_number = %s","000000000000"
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

