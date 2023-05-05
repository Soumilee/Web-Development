<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Soumilee Ghosh (sg342)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 4:06:11 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/sg342" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236487216-79ca1be2-21d0-4e05-a815-2358f718cc43.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Internal Transfer page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236490153-903a91e7-7b09-4e5c-a629-e5e7b635e48a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dropdown of accounts<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236489863-ab122fd8-b6c6-4567-a2d2-b1695d871de2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing error transfer amount cannot be greater than balance<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236487530-1697d567-6114-48b8-86ac-0cdc3472f1e4.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>message stating the error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236489045-be67ff4f-0a4b-4a1c-946b-2c228b3cc0cf.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code handling the error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236489045-be67ff4f-0a4b-4a1c-946b-2c228b3cc0cf.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code handling error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236489293-da4bf1af-c31a-4282-aa13-51fcc2077c56.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cannot transfer negative balance error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236486905-22287777-c9f3-4149-aea5-3b0f961f28ca.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>transfer showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236490422-e4d5a6c7-a3de-40ec-adc7-0450d75f22d5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>transaction with id 49 50 and memo project deliverable 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236497187-55a73e9f-2e06-4a6f-8af9-6c9867586aeb.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Accounts table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <p>How are the initial balances and account numbers are fetched -<div>For fetching the<br>accounts along with their balances and account numbers, l have created an account<br>dropdown which l have been calling in every page template that requires it.<br>At first in main.py l created a global method get_accounts, in this method<br>l am importing DB from sql.db and getting the current user id from<br>the get_id() method. Then I am running a Selectall query to get all<br>the account numbers, id and balance of that particular user who is logged<br>in. After getting the result l am returning it as rows. After that<br>l have created an account_dropdown.html template file which uses form element of html<br>and also sets accs = get_account() here accs variable acts as a counter<br>and for all the rows returned by get_accounts() method a loop is run<br>for a in accs and a[&#39;account_number&#39;] a[&#39;balance&#39;] inside the option tags show the<br>values of the dropdown in the frontend and whichever value is selected that<br>account numbers a[&#39;id&#39;] is taken&nbsp;<br><div>How transaction is recorded&nbsp; and balance gets updated -</div><div>For<br>this l have created two methods in sample.py commit_transaction() and update_balance(). After all<br>the checks have been done on the arguments got from the form elements<br>in the method inttransaction, in sample.py, they are passed to the method commit_transaction<br>it takes in source account id, destination account id, change of balance, type<br>of transaction and memo. Then we are importing DB and doing select queries<br>and getting the balance from the source and destination accounts. Then we are<br>adding or subtracting/adding the difference from/to the source/destination account. Then we are inserting<br>into Transactions table the pairs of transaction with all the arguments we got<br>and in place of expected total we are putting the source and destination<br>balance which we calculated. If this insertion to DB is done and the<br>result status is true then we are moving over to update balance method<br>and passing the source and destination id into the method. In update_balance we<br>import DB and update the accounts table and set the balance by doing<br>SUM operation of the balance and amount which was updated in the transactions<br>table. This is a Boolean method which returns true or false to commit<br>_transaction method. So, if true is returned we do DB.getDB().commit() to commit all<br>the changes made up till now or if false is returned or an<br>exception occurs we do DB.getDB.rollback() so that it returns to the point of<br>the last commit and all the changes are removed.</div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/48">https://github.com/Soumilee/IS601-004/pull/48</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sg342-prod.herokuapp.com/sample/inttransaction">https://is601-sg342-prod.herokuapp.com/sample/inttransaction</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236515400-e6980aa5-6230-45b8-a9dc-99e468d6d5ee.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>can look at 19 and 17 where i have tested internal transfer function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236517265-0a8575d7-6d80-47a7-9882-84ea9dd4a97b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>dashboard or 1st page clicking on list my accounts to go to next<br>page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236517422-6b2406fc-6a59-493d-ba24-e77e847eba94.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>in the list of accounts you can click on go on the right<br>side to go to the page of transactions for that particular account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236515400-e6980aa5-6230-45b8-a9dc-99e468d6d5ee.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the page of transactions for account id 17 and there is a<br>return to profile link to return to the dashboard shown at the beginning<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236517844-47e90080-b57f-4a8e-80a0-2e58aad0476b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code for list transactions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>In the beginning we look at the dashboard -&nbsp; and then click on<br>my accounts card which has the route &#39;/list&#39; in sample.py we have defined<br>that route with the get method and it is for the method list_account()<br>method. So as soon as we click on my accounts it runs the<br>code for list_account method. In this method we get the user id of<br>the current user with the help of flask login and use this id<br>to get that user&#39;s accounts from the accounts table using a select query<br>we also ask for limit from the user and if no limit is<br>provided we give a default limit of 5 so that not more than<br>5 accounts are shown at a time. We send the response as rows<br>to list_account.html template. In the template we use th and td tags and<br>table class to generate a horizontal table format and we also url for<br>sample.list_transactions and pass the acc.id to the backend ( this ensures when we<br>click on the go button we are taken to that accounts transaction, in<br>the sample.list_transaction method we ask as arguments from the frontend the acc_id =&nbsp;<br>acc.id, **request.args statement ensures that the account id of this account gets transferred<br>to the backend. In the transactions.html we have put the url_for auth.landing_page in<br>the top so that we can return to profile dashboard from here and<br>used the table class to show the details in a horizontal table format.<br>We use a for loop on the response we get from sample.list_transactions method<br>to show all the transactions. In sample.list_transactions we get the acc_id from the<br>list_account.html page we then use that account id to run a select query<br>and get all the transactions where the source or destination id has this<br>account id and we limit it to 10 transactions.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/47">https://github.com/Soumilee/IS601-004/pull/47</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sg342-prod.herokuapp.com/sample/list_transaction?acc_id=17">https://is601-sg342-prod.herokuapp.com/sample/list_transaction?acc_id=17</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236525523-eb115d7c-a905-4587-b058-3c74741f7347.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>user profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/47">https://github.com/Soumilee/IS601-004/pull/47</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sg342-prod.herokuapp.com/profile">https://is601-sg342-prod.herokuapp.com/profile</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236552717-de880846-d3c5-487d-9108-07debd27f93a.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>page with data filled in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236552822-61c675ca-7c5d-43cf-a0f6-ca9720676cc4.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236554235-39391f74-91bc-45f2-9da8-040f1283472f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>error showing user cannot transfer more than the amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236554394-f82c4049-4ce1-486c-8628-1cdfc73f93d2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code of external transfer lines 255 to 261 shows error handling for<br>negative amount entry and amount greater than balance entry<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236554394-f82c4049-4ce1-486c-8628-1cdfc73f93d2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236554870-16f4c159-8009-4b8c-9842-344e21cfd13a.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>error showing transfer cannot be negative<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236554394-f82c4049-4ce1-486c-8628-1cdfc73f93d2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code line 233 to 254<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236556039-1ce886c6-a296-46fa-8722-2540cf0bc851.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction Table from DB can look at accounts with id 17 to 20<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/236556455-dc71f414-6cfa-4b0a-8b1b-ff3a38e31a83.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can look at account with id 19 and 20<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p>For account number lookup with the last 4 digits l learned it from<br>this website link -&nbsp;<span style="color: rgb(170, 170, 170); font-style: italic; background-color: rgb(245, 245,<br>245); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;"><a href="https://www.tutorialspoint.com/find-records-with-a-specific-last-digit-in-column-with-mysql">https://www.tutorialspoint.com/find-records-with-a-specific-last-digit-in-column-with-mysql</a></span><div>in the beginning we take the<br>last name of the user and get the id of this user and<br>then with that user id we get all the accounts which match the<br>account numbers last 4 digit on the right side so if there are<br>multiple results the combination of both will eliminate</div><div>any other possibilities because account numbers<br>are unique</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/49">https://github.com/Soumilee/IS601-004/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sg342-prod.herokuapp.com/sample/exttransaction">https://is601-sg342-prod.herokuapp.com/sample/exttransaction</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learnings -&nbsp;<div>learned to use Right(account_number,4) = for looking up DB queries whose number<br>matches the last 4 digits</div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/sg342" target="_blank">Grading</a></td></tr></table>