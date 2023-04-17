<table><tr><td> <em>Assignment: </em> Sample Flask App and Readings</td></tr>
<tr><td> <em>Student: </em> Soumilee Ghosh (sg342)</td></tr>
<tr><td> <em>Generated: </em> 3/6/2023 2:32:43 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/sample-flask-app-and-readings/grade/sg342" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>&nbsp;Follow the slides from class.&nbsp;</li><li>&nbsp;Get the sample app deployed to Heroku dev</li><li>&nbsp;Once finished with the slides create a pull request from the lesson branch to dev (don't close it yet)&nbsp;</li><li>&nbsp;Create an m6_submission.md file in the same directory as the flask sample app&nbsp;</li><li>&nbsp;Fill in the deliverables below&nbsp;</li><li>&nbsp;Generate the markdown and paste the content into the new md file&nbsp;</li><li>&nbsp;git add/commit/push&nbsp;</li><li>&nbsp;Complete the pull request&nbsp;</li><li>&nbsp;Create a pull request from dev to prod&nbsp;</li><li>&nbsp;Complete the merge&nbsp;</li><li>&nbsp;Locally checkout dev&nbsp;</li><li>&nbsp;git pull the latest dev changes&nbsp;</li><li>&nbsp;On GitHub navigate to the location of the m6_submission.md file from the prod branch&nbsp;</li><li>&nbsp;Grab that direct link and submit it to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Proof App has been deployed </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the output of the app (including the url) showing it's running from Heroku dev</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/101204363/223211397-8577b930-3eb2-4b8d-9a46-7fef133fa641.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of Heroku dev app is601-sg342-dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a direct link to the app here (prod url)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sg342-prod.herokuapp.com/">https://is601-sg342-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a link to the pull request from Flask-Sample-HW to Dev</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Soumilee/IS601-004/pull/16">https://github.com/Soumilee/IS601-004/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Did you have any issues during setup and if so how did you resolve them, otherwise what did you learn?</td></tr>
<tr><td> <em>Response:</em> <p>I had several issues while setting up -<div>1. VS code is not able<br>to reference files unless they are added to workspace and i did not<br>know that so i had a problem with it which was solved when<br>i added the flask_sample folder to workspace in VS code.</div><div>2. I had 2<br>failure while building the app in github and i realised they were because<br>i was missing 2 of the requirements which i completed and then i<br>build it again and it showed green tick but when deployed in heroku<br>the is-601-dev gave an error i.e on the webpage there was an application<br>error not on github - when i showed it to professor he said<br>i was missing the gunicorn requirement, so i installed it froze the requirements<br>file.</div><div>3. Then i was doing the sql part and in it eventhough i<br>had all the requirements and i had installed mysql-connector-python and dotenv there was<br>error in db.py file wherever there was an import statement referencing to these<br>modules claiming VS code cannot find these files - so i ran the<br>sql file from the powershell by doing python path-of-db.py and it ran and<br>gave the correct output. Then i did git status, add, commit and then<br>push and pull and merge and i went to actions in github to<br>check and it took some time to build but it worked and in<br>heroku the app was deployed and showing the output.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Readings </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> What can you tell me about docker? Describe the various steps needed to get an app ran inside a docker container in your own words</td></tr>
<tr><td> <em>Response:</em> <p>Docker -&nbsp; it is an open platform for developing, shipping and running applications.<br>It helps<span style="font-family: Roboto, sans-serif;">&nbsp;to segregate our applications from our infrastructure so we<br>can deliver software quickly. We can manage our infrastructure in the same ways<br>we manage our applications. By taking advantage of Docker’s methodologies for shipping, testing,<br>and deploying code quickly, you can significantly reduce the delay between writing code<br>and running it in production. We can do several things with Docker -<br>we can</span><span style="font-family: Roboto, sans-serif;">&nbsp;write code locally and share with our colleagues using<br>Docker containers. We can</span><span style="font-family: Roboto, sans-serif;">&nbsp;use Docker to push our applications into<br>a test environment and execute automated and manual tests. We can&nbsp;</span><span style="font-family: Roboto,<br>sans-serif;">find bugs, fix them in the dev environment and make test cases and<br>when they all have passed we can deploy them to the prod.</span><div>Link -&nbsp;<a href="https://docs.docker.com/get-started/overview/">https://docs.docker.com/get-started/overview/</a>&nbsp;<br>l have gone over this website and referenced the various articles written for<br>a better understanding of Docker.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> What is Heroku? Why do you feel it was chosen for this class?</td></tr>
<tr><td> <em>Response:</em> <p>Heroku - is a paas platform as a service which provides a cloud<br>platform for everyone to deploy their applications. It runs on AWS but is<br>more user friendly than AWS. There are many languages on which we can<br>code in Heroku. It can be connected with Salesforce so if we want<br>to make an enterprise based application it is easy to convince people to<br>use Salesforce connector. There are many powerful add ons which can be used<br>as and when required.<div>I think it was chosen for this class because it<br>is flexible and easy to use platform which makes it easy for students<br>to learn how to deploy web based applications.&nbsp;</div><div>Link -&nbsp;<a href="https://trifinlabs.com/what-is-heroku/">https://trifinlabs.com/what-is-heroku/</a></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What is flask? List a few things you learned about it</td></tr>
<tr><td> <em>Response:</em> <p>It is a web framework which helps us to build web applications easily.<br>It has a collection of modules and libraries which lets the programmer to<br>write applications without having to think about protocols, thread management and so on.<br>WSGI is The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has<br>been used as a standard for Python web application development. WSGI is the<br>specification of a common interface between web servers and web applications. Werkzeug is<br>a WSGI toolkit that implements requests, response objects, and utility functions. This enables<br>a web frame to be built on it. The Flask framework uses Werkzeg<br>as one of its bases. jinja2 is a popular template engine for Python.A<br>web template system combines a template with a specific data source to render<br>a dynamic web page. It is also known as microframework instead of an<br>abstraction layer for database support it just adds an extension.<div>Link -&nbsp;<a href="https://pythonbasics.org/what-is-flask-python/">https://pythonbasics.org/what-is-flask-python/</a>&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> What is the difference between a Dockerfile and a Github Action .yml file?</td></tr>
<tr><td> <em>Response:</em> <div>The three primary differences between the Docker file and docker-compose are:<br></div><div>1. The Docker<br>file is used to build images while the docker-compose.yaml file is used to<br>run images.<br></div><div>2. The Docker file uses the docker build command, while the docker-compose.yaml<br>file uses the docker-compose up command.</div><div>3. A docker-compose.yaml file can reference a Docker<br>file, but a Dockerfile can’t reference a docker-compose file.</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/sample-flask-app-and-readings/grade/sg342" target="_blank">Grading</a></td></tr></table>