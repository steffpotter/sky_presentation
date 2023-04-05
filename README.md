# sky_presentation

You need flask installed to run this.  

If you get an error run the following command in the terminal of either VS Code or PyCharm: 
$ pip install -U Flask
<br/>
<br/>
<h3>Steps for creating a new feature branch and checking out the code on to your local machine:</h3>
<br/>
* Use this [github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository
) resource to create a new feature branch
* Open git bash and run "$ git clone --branch [Insert your feature branch name] https://github.com/steffpotter/sky_presentation.git"
* Open PyCharm or your code editor of choice and open the new "sky_presentation" project
<br/>

<h3>Steps for pushing local changes to your feature branch</h3>
Use [this](https://gist.github.com/whoisryosuke/36b3b41e738394170b9a7c230665e6b9) resource for instructions on how to push your changes to your feature branch

<h3>Steps for merging your feature into main</h3>
Use [this](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) resource.


<h3>Steps for updating you local code with the latest changes in the main branch:</h3>
* Run <code>git pull origin main</code>

<h3>Mock database Implementation</h3>
Given that we don't know for sure whether we will be given time/ allowance to provision a hosted db I've
added the ability to toggle between use of a mock python based db or a real MySQL db using Steff's script.

If you want to use the mock db, in routes.py, set the "useMock" parameter in the SubjectDao and CandidateDao
constructor to True. Set it to false if you want to use the real MySQL database. 
