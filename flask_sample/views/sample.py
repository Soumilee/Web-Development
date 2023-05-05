from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_required, current_user
import random
from sql.db import DB
sample = Blueprint('sample', __name__, url_prefix='/sample')


def commit_transaction(src, dest, change, type, memo):
    print(src,dest,change,type,memo)
    from sql.db import DB
    DB.getDB().autocommit = False
    if change > 0:
        change *= -1
    query1 = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s",src)
    if query1.status:
                row = query1.row
                print(row)
                src_bal = row["balance"]
    query2 = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s",dest)
    if query2.status:
                row = query2.row
                print(row)
                dest_bal = row["balance"]
    src_bal = src_bal - change
    dest_bal = dest_bal + change
    query = """INSERT INTO IS601_Transactions (account_src_id, account_dest_id , balance_change, transaction_type, memo, expected_total) VALUES (%s, %s, %s, %s, %s, %s)"""
    pairs = []
    pairs.append((src, dest, change, type, memo,src_bal))
    pairs.append((dest, src, change * -1, type,memo,dest_bal))
    try:
        result = DB.insertMany(query, pairs)
        if result.status:
            print("Recored transations pairs", src, dest, change, type, memo)
            if update_balance(src) and update_balance(dest):
                DB.getDB().commit()
                return True
    except Exception as e:
        print("Error recording point history", e)
        DB.getDB().rollback()
        return False

def update_balance(acc_id):
    from sql.db import DB 
    try:
        result = DB.update("""UPDATE IS601_Accounts set balance = (SELECT IFNULL(SUM(balance_change), 0) 
        FROM IS601_Transactions WHERE account_src_id = %(acct)s) WHERE id = %(acct)s""", {"acct":int(acc_id)})
        if result.status:
            return True
    except Exception as e:
        print("Error updating balance", e)
        DB.getDB().rollback()
    return False

@sample.route('/add', methods=['GET', 'POST'])
def create_account():
    account_type = request.form.get("type","checking")
    deposit = request.form.get("deposit", 0,int)
    user_id = current_user.get_id()  
    if account_type and deposit>=5:
        try:           
            account_no = "%0.12d" % random.randint(0,999999999999)
            result = DB.insertOne("INSERT INTO IS601_Accounts (account_number,user_id,balance,account_type) VALUES(%s,%s,%s,%s)",
                                  account_no,user_id,deposit,account_type)
            #after the new account is created an id is generated so we have to get that id and insert it into the transaction table
            if result.status:
                acc_id = DB.db.fetch_eof_status()["insert_id"]
            #we also have to get the world acc id cannot hard code it since id may change later
            query = DB.selectOne("SELECT id FROM IS601_Accounts WHERE account_number = %s","000000000000")
            if query.status:
                row = query.row
                print(row)
                world_id = row["id"]
            commit_transaction(world_id,acc_id,deposit,account_type,"account creation")           
            if result.status:
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
    args = [user_id]
    query = "SELECT id,account_number,balance,account_type,created,modified FROM IS601_Accounts WHERE user_id = %s"
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
    #user_id = current_user.get_id()
    acc_id = request.args.get("acc.id")
    args = [acc_id]
    query = """SELECT account_src_id, account_dest_id, balance_change, transaction_type, memo, expected_total, created, modified FROM IS601_Transactions WHERE account_src_id 
    or account_dest_id = %s"""
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

@sample.route('/deposit', methods=['GET','POST']) #this will perform deposit in which user will deposit money into their account from world account
def deposit():
    acc_id = request.form.get("acc_id")
    type = request.form.get("type","deposit")
    amt = request.form.get("amt",0,int)
    memo = request.form.get("memo"," ")
    print(acc_id,type,amt,memo)
    world_id_query = DB.selectOne("SELECT id FROM IS601_Accounts WHERE account_number = %s","000000000000")
    if world_id_query.status:
        row = world_id_query.row
        world_id = row["id"]
    if acc_id is None:
        flash("Please select the account for deposit","error")
    if type is None:
        flash("Please select the type of account","error")
    if amt is None or amt<=1:
        flash('Please select an amount greater than 1$',"error")
    else:
        if request.method == "POST":
            try:                
                result = commit_transaction(acc_id,world_id,amt,type,memo)
                if result:
                    flash("The deposit has been submitted","success")
            except Exception as e:
                flash(e,"danger")
    return render_template("deposit_into_acc.html")

@sample.route('/withdraw', methods=['GET','POST']) #this will perform withdraw in which user will withdraw money from their account
def withdraw():
    acc_id = request.form.get("acc_id")
    type = request.form.get("type","withdraw")
    amt = request.form.get("amt",0,int)
    memo = request.form.get("memo"," ")
    print(acc_id,type,amt,memo)
    get_world_id = DB.selectOne("SELECT id FROM IS601_Accounts WHERE account_number = %s","000000000000")
    if get_world_id.status:
        row = get_world_id.row
        world_id = row["id"]
    if acc_id is None:
        flash("Please select the account for deposit","error") 
    else:
        get_balance = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s",acc_id)
        print(get_balance)
        if get_balance.status:
            row = get_balance.row
            bal = row["balance"]       
    if type is None:
        flash("Please select the type of transaction","error")
    if amt<=1 or amt > bal:
        flash('Please select an amount greater than 1$ and less than your total balance',"error")
    else:
        if request.method == "POST":
            try:
                result = commit_transaction(world_id,acc_id,amt,type,memo)
                if result:
                    flash("The money has been withdrawn","success")
            except Exception as e:
                flash(e,"danger")
    return render_template("withdraw_from_acc.html")

@sample.route('inttransaction',methods = ['GET','POST'])
def internal_transaction():
    src_acc_id = request.form.get("src_acc_id")
    dest_acc_id = request.form.get("dest_acc_id")
    amt = request.form.get('amt',0,int)
    memo = request.form.get('memo'," ")
    type = request.form.get('type','internal transaction')
    print(src_acc_id,dest_acc_id,amt,memo,type)
    if request.method == "POST":
        try:
            if src_acc_id is None:
                flash("Please enter the source account","error")
            else:
                get_balance = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s",src_acc_id)
            if get_balance.status:
                row = get_balance.row
                bal = row['balance']
            if dest_acc_id is None:
                flash('Please enter destination account','error')
            if amt < 0:
                flash('The transfer amount cannot be negative','error')
            if src_acc_id == dest_acc_id:
                flash('Cannot transfer to same account','error')
            if amt > bal:
                flash('The transfer amount cannot be greater than balance','error')
            else:
                result = commit_transaction(src_acc_id,dest_acc_id,amt,type,memo)
                if result:
                    flash("The money has been submitted","info")
        except Exception as e:
            flash(e,'danger')
    return render_template('internal_transactions.html')

@sample.route('exttransaction',methods = ['GET','POST'])
def external_transaction():
    src_acc_id = request.form.get("src_acc_id")
    dest_acc_no = request.form.get("dest_acc_no")
    last_name = request.form.get("last_name")
    amt = request.form.get("amt",0,int)
    type = request.form.get("type","external transaction")
    memo = request.form.get("memo")
    if request.method == "POST":
        try:
            if src_acc_id is None:
                flash("Please enter the source account","error")  
            if last_name is None:
                flash("Please enter the last name","error")
            else:
                query = DB.selectOne("SELECT id FROM IS601_Users WHERE last_name = %s",last_name)
                if query.status:
                    row = query.row
                    user_id = row['id']   
                else:
                    flash('This user does not exist','error') 
            if dest_acc_no is None:
                flash('Please enter destination account','error')

            else: # learned this query from https://www.tutorialspoint.com/find-records-with-a-specific-last-digit-in-column-with-mysql
                print(user_id)
                query1 = DB.selectOne("SELECT id FROM IS601_Accounts WHERE RIGHT(account_number,4)=%s AND user_id = %s",dest_acc_no,user_id)
                print(query1.row)
                if query1.status: 
                    row = query1.row
                    dest_acc_id = row['id']
                else:
                    flash('This account does not exist','error')
                get_balance = DB.selectOne("SELECT balance FROM IS601_Accounts WHERE id = %s",src_acc_id)
                if get_balance.status:
                    row = get_balance.row
                    balance = row['balance']
            if amt < 0:
                flash('The transfer cannot be negative','error')
            if amt>balance:
                flash('The transfer amount cannot be greater than balance','error')
            else:
                result = commit_transaction(src_acc_id,dest_acc_id,amt,type,memo)
                if result:
                    flash("The money has been submitted","info")
        except Exception as e:
            flash(e,'danger')
            print(Exception,e)
    return render_template('external_transactions.html')