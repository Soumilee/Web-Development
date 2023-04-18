<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Soumilee Ghosh (sg342)</td></tr>
<tr><td> <em>Generated: </em> 4/12/2023 2:26:15 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/sg342" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231252076-d5ed945e-4135-4280-9ed2-57ef19e50bca.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-mt85 is updated to DIAR-sg342 (in nav.html)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231253645-fb8566fc-afd8-4aad-9cc1-c5dd4b60f07f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>company search add and edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231253805-c3054b77-4043-4aff-9f95-3d5ff7aaae01.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee search add and edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231253968-fa71bee5-dcac-4e6b-98f4-a194ccd77e16.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin import csv<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231256674-c0b5f2f5-bc3b-4d24-b67c-b3786ab6924e.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP3_Company table populated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231256903-225d5cc1-d5b5-4602-be8b-1c0bb57b5580.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP3_Employee table populated<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231269750-98896b65-cab2-4730-8a02-350d320ff4cf.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>code checking .csv file and rejecting with flash ; file is being read<br>from the provided stream as dict ; data is only being considered if<br>all fields are present <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231270222-3fa062e7-89c5-4ee6-81d4-5bae73b28dfb.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>proper flash message present after every operation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231270481-8fe223b9-778f-4e90-bc66-983a75e34617.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Csv file checked and uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231270600-74cd14f3-0411-4a78-9f4e-99fd34c76447.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>file missing error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231271352-f03f89a4-2d82-420f-8aa0-e24162addb39.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee Table after importing CSV<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231271500-df92fefd-ca9b-4a84-953e-d553a0562061.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Table after importing CSV<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231517854-c6d83a05-b17a-4f19-9da4-72a2f84f0352.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee.add() method in VS code with ucid and date visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231518620-9b544c91-e600-48da-91f4-e875332f9406.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231518778-6b1fd555-892f-4c35-a18f-61e334618193.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last name required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231519006-0a275126-fb0d-4d3e-80ba-7c14e33c47e9.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231519228-8281220d-7736-4ea3-a7d7-8f2d50419ce2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message of employee added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231519775-37701c46-caa7-4959-93ac-d28b83687fc2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows all the employee data previously used for filling also shows that its<br>checking valid email or not in the terminal<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231526915-8fbcf14c-2278-4dd2-82ea-a0d3dd0b7ec7.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code for Employee search method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231540959-eda0922a-f22d-4fd3-9ab7-6cfca74e37dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>website for search employee <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231533005-3c747707-9047-490a-abe5-413a8ca40d28.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee.edit() method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231540959-eda0922a-f22d-4fd3-9ab7-6cfca74e37dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee webpage<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231516502-070112a5-37cc-4654-a632-96e7720aef4d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code for company.add() method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231513785-7abde8bc-983c-4635-b19a-e9cb996f203b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data on company add website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231514012-15893a77-d813-4dae-9722-0717b7d4ea67.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message on adding company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231516978-380e0d79-9e8b-462e-ac57-145e327e439f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB record of the new added company with ucid in top left corner<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231534200-6292831c-13aa-4269-b07a-a23c7e923e26.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company_search() method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231534753-88d3f653-0267-4716-a055-33a329095cfd.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>website for company search<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231538008-1004882a-ba18-42b7-a467-c05e979f766d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code of company edit method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231534753-88d3f653-0267-4716-a055-33a329095cfd.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website for company editing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231538581-6f7be696-0c67-4cb8-a201-07a33d03b42e.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code for employee delete method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231538910-7ee5051f-3d6c-4c33-94fb-e2f1c676cb27.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>VS code for company delete method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231545363-9fb57e7d-0b44-4cc9-8d39-ea9f818a7a35.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing upload csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231545512-f561bc86-5dd0-4ef1-8350-1cea796dc55e.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing search employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231545620-9b9e632b-1857-40b7-b968-5effc69242de.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing search company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231545738-b942190f-0ffc-4d54-b666-c988bd52dda7.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing edit employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231545900-ce9acd55-5bda-44e1-9b21-636d984f1e42.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing edit company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231546007-f7fa6c3c-4209-40fc-bbd2-54b56dd81f3c.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing add company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/231546097-5b77c063-4643-4757-aa3e-3445ae8e3844.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>testing add employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>Things I learned while doing this assignment -<div>1. web development is hard, you<br>have to do everything yourself, frontend, backend and database everything. Just making sure<br>that the data flows in proper direction is so hard.&nbsp;</div><div>2. I learned how<br>to write the code for the backend of a website following GET POST<br>methods and how to check if the arguments are in proper format or<br>not.</div><div>3. I still need to learn the frontend part I had some issues<br>while doing the html template pages with horizontal format for employee directory I<br>could not do that I hope in the next project I will learn<br>more about the frontend part. Also how to add action buttons for edit<br>and delete I couldn&#39;t do that as well.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/sg342" target="_blank">Grading</a></td></tr></table>