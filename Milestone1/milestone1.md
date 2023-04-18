<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Soumilee Ghosh (sg342)</td></tr>
<tr><td> <em>Generated: </em> 4/17/2023 10:58:12 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/sg342" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641163-ad434e62-897f-4d10-b7f5-76012a435fd5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641261-780e6e92-d56d-42c0-a23c-b0e89c834c5d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641332-a866e90f-07f8-46ba-b6e8-6e3703b15834.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords must match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641446-dac1083b-5276-477d-a0c3-7922aad45f61.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641551-a543fe7e-67f4-43cf-bb70-5ec214dba0df.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641604-e0c4cd1e-5efd-489d-ac6d-5d38a36a9d52.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>form with data filled before registering<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641685-7c7c5d2b-720a-4dcf-aaa8-199e192843cf.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users table with data filled from previous task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><span style="white-space: pre-wrap;">We install and use these packages for authentication - </span></div><div><span style="white-space:<br>pre-wrap;">flask-WTF - wrapper for WTForm (pythonic form generation and validation), </span><span style="white-space: pre-wrap;">email_validator<br>- needed for Email field validation for WTForms, </span><span style="white-space: pre-wrap;">flask_login - utilities<br>to work with a user session and manage the user session, </span><span style="white-space:<br>pre-wrap;">flask-bcrypt - The bcrypt hashing algorithm for password hashing. </span><span style="white-space: pre-wrap;">In our<br>main.py we use LoginManager, this handles our user session and provides helpful utilities<br>as we’re using an app factory we defined a variable for login_manager outside<br>of the factory then inside the factory we have used its init_app() method<br>to associate the app,</span><span style="white-space: pre-wrap;"> inside of the app factory we have<br>used the user_loader decorator. </span><span style="white-space: pre-wrap;">This runs a process to lookup a<br>user by id. Then</span><span style="white-space: pre-wrap;"> db.py will do a basic SELECT query.</span><span<br>style="white-space: pre-wrap;"> define a User model (class) which will be explained later, but<br>this function will generate a User object upon successful lookup of a user<br>otherwise it’ll return None. </span><span style="white-space: pre-wrap;">Lastly, there is a request teardown decorator.<br>This is used to close our DB connections at the end of requests.<br></span><span style="white-space: pre-wrap;">In _formhelpers.html we describe a</span><span style="white-space: pre-wrap;"> macro which is basically<br>a template function that allows parameters/arguments to be passed into a partial template<br>and the result returned. Then </span><span style="white-space: pre-wrap;">render_field is defined that’ll wrap a<br>form field with a bootstrap form-group class, provide the form-label class on the<br>label part of the form, and apply the form-control class on the field<br>part of the form. </span><span style="white-space: pre-wrap;">It’ll also loop through any errors applied<br>by wtforms validators which are handled automatically.</span></div><div><span style="white-space: pre-wrap;">This can then be imported<br>into any template and used as a function.</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641785-9882b422-2770-460a-82fe-a3e2e9a5b108.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641861-82993038-57e4-4979-a781-531efea4d5df.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232642043-e7217070-d570-411e-8b50-de352fcd47c8.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful login of user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The functions were defined below to validate the password logic -&nbsp;</div><div>1. register() -<br>handles presenting the registration form and receiving/validating the data to create a new<br>user</div><div>2. login() - handles presenting the login form and receiving/validating the data to<br>login a user via login_user() from flask_login</div><div>3. landing_page() - a sample login-protected route</div><div>Upon<br>invalid access, it’ll route the user to a built-in access denied page that<br>we’ll override later&nbsp;</div><div>4. logout() - destroys the user session via logout_user() from flask_login<br>and redirects to login</div><div>Both register and login will create a form object of<br>their respective form. They’ll use validate_on_submit() which runs the validator rules of the<br>form when the form submission is received by the server (again these are<br>client-side and server-side so you shouldn’t need to do extra validations). We have<br>fetched the data of the form via form.field.data. Next, we have hashed the<br>password. For this, bcrypt is used mainly since it always generates 60 character<br>hashes and it has a built in salt value. The generated hash will<br>be stored in the DB along with the desired email address. Upon login,<br>we have fetched the user by email address (and SELECT the password as<br>well). Then we have used bcrypt to compare the existing hash with the<br>raw login password. If this process returns true, we generate a User object<br>and pass it to login_user() from flask_login which does the session work.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232642138-dc52ebaa-cb85-483a-b256-2efa59893737.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>user logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232655131-e1d71bde-195b-456e-a46a-bb4bfd3c382d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tried to access profile page after logging out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>logout() - destroys the user session via logout_user() from flask_login and redirects to<br>login</div><div>Both register and login will create a form object of their respective form.<br>They’ll use validate_on_submit() which runs the validator rules of the form when the<br>form submission is received by the server (again these are client-side and server-side<br>so you shouldn’t need to do extra validations). We have fetched the data<br>of the form via form.field.data. Next, we have hashed the password. For this,<br>bcrypt is used mainly since it always generates 60 character hashes and it<br>has a built in salt value. The generated hash will be stored in<br>the DB along with the desired email address. Upon login, we have fetched<br>the user by email address (and SELECT the password as well). Then we<br>have used bcrypt to compare the existing hash with the raw login password.<br>If this process returns true, we generate a User object and pass it<br>to login_user() from flask_login which does the session work.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232655131-e1d71bde-195b-456e-a46a-bb4bfd3c382d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tried accessing profile page after logging out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232648036-bc044489-4707-46f8-ac8f-d0d5745690dd.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>permission denied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232642493-3ad343ae-032a-486b-af91-93480f16782c.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>We have loaded the user from the session since each request would needlessly<br>hit our DB to lookup the user. The jsons package is used to<br>try to restore a string representation of the user back into a User<br>object and returns it. We have kept our DB lookup as a fallback<br>if the session isn’t available. Note if this scenario does happen we’ll not<br>have our roles/permissions carry through. Flask principal requires an identity_loaded decorator that will<br>associate the user to principal’s identity object via user id and if the<br>user has roles it’ll convert the roles to RoleNeed() objects.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>The roles.py file contains our blueprint/route info, and lastly we have used a<br>permissions.py file to define what permissions our app will use so we don’t<br>need to keep redeclaring them. We have created a new class called Role<br>that’ll extend JsonSerializable our basic class just holds name, description, and is_active</div><div>Mostly name<br>is important for the user lifecycle. The other fields are used for create/edit<br>and loading. Is_active will be a flag to globally enable/disable a role</div><div>JsonSerializable is<br>a utility class that’ll give access to a few overridden methods that’ll attempt<br>to convert the object into json for easier printing for debugging info and<br>serialization for transmitting objects or passing them through sessions.&nbsp; __str__, __repr__, toJson(), toJSON(),<br>basically all do the same thing and are mostly aliases which uses the<br>jsons package to attempt to serialize nested objects.&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232657967-88307409-ad13-49f3-86ef-058ed7d7e4ea.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of UI<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641163-ad434e62-897f-4d10-b7f5-76012a435fd5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641261-780e6e92-d56d-42c0-a23c-b0e89c834c5d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641332-a866e90f-07f8-46ba-b6e8-6e3703b15834.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>password must match<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>By using flash messages I have made the errors user friendly also colorful.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232650245-017085b6-3eff-4258-9070-2f276cb7e22f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>User profile for soumilee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div><span style="white-space: pre-wrap;">We install and use these packages for authentication - </span></div><div><span style="white-space:<br>pre-wrap;">flask-WTF - wrapper for WTForm (pythonic form generation and validation), </span><span style="white-space: pre-wrap;">email_validator<br>- needed for Email field validation for WTForms, </span><span style="white-space: pre-wrap;">flask_login - utilities<br>to work with a user session and manage the user session, </span><span style="white-space:<br>pre-wrap;">flask-bcrypt - The bcrypt hashing algorithm for password hashing. </span><span style="white-space: pre-wrap;">In our<br>main.py we use LoginManager, this handles our user session and provides helpful utilities<br>as we’re using an app factory we defined a variable for login_manager outside<br>of the factory then inside the factory we have used its init_app() method<br>to associate the app,</span><span style="white-space: pre-wrap;"> inside of the app factory we have<br>used the user_loader decorator. </span><span style="white-space: pre-wrap;">This runs a process to lookup a<br>user by id. Then</span><span style="white-space: pre-wrap;"> db.py will do a basic SELECT query.</span><span<br>style="white-space: pre-wrap;"> define a User model (class) which will be explained later, but<br>this function will generate a User object upon successful lookup of a user<br>otherwise it’ll return None. </span><span style="white-space: pre-wrap;">Lastly, there is a request teardown decorator.<br>This is used to close our DB connections at the end of requests.<br></span><span style="white-space: pre-wrap;">In _formhelpers.html we describe a</span><span style="white-space: pre-wrap;"> macro which is basically<br>a template function that allows parameters/arguments to be passed into a partial template<br>and the result returned. Then </span><span style="white-space: pre-wrap;">render_field is defined that’ll wrap a<br>form field with a bootstrap form-group class, provide the form-label class on the<br>label part of the form, and apply the form-control class on the field<br>part of the form. </span><span style="white-space: pre-wrap;">It’ll also loop through any errors applied<br>by wtforms validators which are handled automatically.</span></div><div><span style="white-space: pre-wrap;">This can then be imported<br>into any template and used as a function.</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232651177-a03d133b-12b1-4ffb-b62e-cf127ff28377.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid username format for updating profile<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232651865-7eac53c9-2dc7-4a24-a080-a0f354d82782.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated profile successfully<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232651491-e37b6077-10da-48e8-97a8-f8a1ae5778b8.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB after updating profile for Soumilee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/232641685-7c7c5d2b-720a-4dcf-aaa8-199e192843cf.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB before updating profile for Soumilee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/37">https://github.com/Soumilee/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div><span style="white-space: pre-wrap;">We install and use these packages for authentication - </span></div><div><span style="white-space:<br>pre-wrap;">flask-WTF - wrapper for WTForm (pythonic form generation and validation), </span><span style="white-space: pre-wrap;">email_validator<br>- needed for Email field validation for WTForms, </span><span style="white-space: pre-wrap;">flask_login - utilities<br>to work with a user session and manage the user session, </span><span style="white-space:<br>pre-wrap;">flask-bcrypt - The bcrypt hashing algorithm for password hashing. </span><span style="white-space: pre-wrap;">In our<br>main.py we use LoginManager, this handles our user session and provides helpful utilities<br>as we’re using an app factory we defined a variable for login_manager outside<br>of the factory then inside the factory we have used its init_app() method<br>to associate the app,</span><span style="white-space: pre-wrap;"> inside of the app factory we have<br>used the user_loader decorator. </span><span style="white-space: pre-wrap;">This runs a process to lookup a<br>user by id. Then</span><span style="white-space: pre-wrap;"> db.py will do a basic SELECT query.</span><span<br>style="white-space: pre-wrap;"> define a User model (class) which will be explained later, but<br>this function will generate a User object upon successful lookup of a user<br>otherwise it’ll return None. </span><span style="white-space: pre-wrap;">Lastly, there is a request teardown decorator.<br>This is used to close our DB connections at the end of requests.<br></span><span style="white-space: pre-wrap;">In _formhelpers.html we describe a</span><span style="white-space: pre-wrap;"> macro which is basically<br>a template function that allows parameters/arguments to be passed into a partial template<br>and the result returned. Then </span><span style="white-space: pre-wrap;">render_field is defined that’ll wrap a<br>form field with a bootstrap form-group class, provide the form-label class on the<br>label part of the form, and apply the form-control class on the field<br>part of the form. </span><span style="white-space: pre-wrap;">It’ll also loop through any errors applied<br>by wtforms validators which are handled automatically.</span></div><div><span style="white-space: pre-wrap;">This can then be imported<br>into any template and used as a function.</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learned about -<div>1. authenticating a form</div><div>2. taking data in from the form and<br>putting in db</div><div>3. withdrawing data from db and displaying on frontend</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sg342-prod.herokuapp.com/login">https://is601-sg342-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/sg342" target="_blank">Grading</a></td></tr></table>