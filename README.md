# StayClean

Scripts used to manage the StayClean monthly challenges for https://www.reddit.com/r/pornfree

Here's a rundown of these files, and how I use each one to manage the StayClean monthly challenges:

### Miscellaneous files

 - **participants.txt** This is the list of people who have signed up for the challenge.  It's just a space-delimited file, one record per line, with the following fields for each record:  1) The username of the user,  2) A boolean indicating whether the user has checked in at least once,  3) A boolean indicating whether the user has been disqualified for the month (i.e. has reported a relapse some time during the month)  4) (optional) the date that the user reported a relapse.  Most of the Python scripts either read from or write to this file.  This file must be present to allow the scripts to run - when you create a new month, create an empty participants.txt file by executing "touch participants.txt".

 - **participant.py, participantCollection.py** - classes used by various scripts.

### Scripts to use during the signup period (usually the week before the month starts, when people sign up for the challenge)

 - **signup.py** - Use this script to sign up one or more new users.  This script is typically used before the beginning of the month, during the signup period, or during a "late signup grace period", which I sometimes offer for the first few days of the month.  Follow the script name by a list of usernames for users to sign up.

 - **display-during-signup.py** - Generate and automatically copy to the clipboard, text for the daily signup post.

### Frequently used scripts to use during the challenge

 - **checkin.py** - Use this script to "check in" one or more users.  Follow the script name with a list of usernames for users to check in.

 - **signup-and-checkin.sh** - This is a convenience script, typically used during the "late signup grace period", to automatically sign up and check in one or more users.  Follow the script name with a list of usernames.

 - **relapse.py** - Use this script to disqualify one or more users who have reported a relapse.  Follow the script name with a list of usernames for users to disqualify.

 - **display.py** - Use this script once per morning to generate and automatically copy to the clipboard, text for the main "stickied" challenge post.

### Infrequently used scripts

 - **reinstate.py** - This infrequently used script can be used to "un-disqualify" a user.  It is sometimes used when a user simply forgot to checkin in time, and wants to be re-added to the challenge.

 - **disqualify-all-not-checked-in.py** - Use this on the 16th of the month, and after the last day of the month, to disqualify all participants who have not checked in.

 - **mark-all-as-not-checked-in.py** - On the 16th, use this to mark all participants who checked in during the first half of the month, as not checked in again.

 - **on-the-sixteenth.sh** - This is a convenience script, to be run on the 16th of the month.  It executes the three scripts that need to be run on that day, in the proper order.

### Flask scripts
Flask is great, and saves me a ton of manual copying / pasting!  Flask is a Python framework for creating simple web apps.  By leaving a couple of our daemon scripts running at all times (serve-signups-with-flask.py and serve-challenge-with-flask.py), you can process incoming signup, checkin, and relapse comments from participants, simply by clicking form submit buttons, rather than manually copying and pasting usernames from the reddit pages to our command line python scripts.

### Flask URLs
Once you start the two flask scripts in a month's directory, as described above, you will have two very handy URLs that you can open in browser tabs to help manage that month's signups and checkin / relapse comments:
- **http://127.0.0.1:8888/moderatechallenge.html** - When this URL is reloaded in the browser, the serve-challenge-with-flask.py script uses the reddit API to retrieve all comments from the challenge reddit page.  For every new comment (i.e. every comment that has not yet been acted on by me), it displays the username of the commenter, the body of the comment, and a form with four submit buttons:

    - **Checkin** - Checkin the commenter (invoke the checkin.py script with the commenter's username), and then use the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.
    - **Signup and Checkin** - Signup and checkin the commeter (invoke the signup-and-checkin.py script with the commenter's username), and then use the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.  This script is very useful during the 3-day late-signup grace period.
    - **Relapse** - Disqualify the commenter (invoke the relapse.py script with the commenter's username), and then use the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.
    - **Reinstate** - Reinstate the commenter (invoke the reinstate.py script with the commenter's username), and then use the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.
    - **Skip comment** - Don't do anything besides using the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.  This is appropriate for comments that are neither checkins nor relapses.
    - **Skip comment and don't upvote** - Don't do anything at all with the comment.

- **http://127.0.0.1:8890/moderatesignups.html** - When this URL is reloaded in the browser, the serve-signups-with-flask.py script uses the reddit API to retrieve all comments from the signup reddit pages.  E.g. on the last week of December, we post a signup message every day, to remind people to sign up for January's challenge.  This script runs in the January directory, and checks all of the signup posts posted so far.  For every new comment (i.e. every comment that has not yet been acted on by me), it displays the username of the commenter, the body of the comment, and a form with three submit buttons:

    - **Signup** - Signup the commenter (invoke signup.py with the commenter's username), and then use the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.
    - **Skip comment** - Don't do anything besides using the reddit API to upvote the comment, for easy identification of the comment as already being taken care of.  This is appropriate for comments that are not actually signup requests.
    - **Skip comment and don't upvote** - Don't do anything at all with the comment.

### My workflow for managing the StayClean monthly challenges
Let's go through an example.  For our example, we will manage the monthly challenge for January 2016.
- **On the morning of January 1** - The first day of the month is by far the most complex day.  Every other day is simple, honest.  We have already been using (during the last week of December) the signup.py script and/or the http://127.0.0.1:8890/moderatesignups.html flask webapp to sign people up (see the _On the mornings of January 25-January 31_ section below for more on that).  I.e. there are already many lines in ~/stayclean/stayclean-2016-january/participants.txt.
    - cd to the _~/stayclean/stayclean-2016-january_ directory.
    - In a terminal, execute the **display.py** script, which generates the first day's challenge page text, and copies it to the clipboard.
    - Bring up a browser on the subreddit, and click "Submit a new text post" to create the challenge post.  Give the new post a title of "STAY CLEAN: JANUARY! This thread updated daily - Check in here!"  Paste the page text into the form and hit Submit.
    - Sticky the new post.
    - Copy the 6-digit submission id code (e.g. "3v059o") from the post's URL, and paste it into the _challengePageSubmissionId_ portion at the top of the **serve-challenge-with-flask.py** script.
    - In a long-running browser tab, open the _http://127.0.0.1:8888/moderatechallenge.html_ flask webapp.  From now on, much of the heavy lifting of managing the monthly challenge can be done from this browser tab.
    - cd to the previous month's directory, e.g. _~/stayclean/stayclean-2015-december_
    - In a terminal, execute the **disqualify-all-not-checked-in.py** script.
    - Edit the **display-final-after-month-is-over.py** script, and edit the _nextMonthURL_ value at the top of the script, pasting in the URL for the new January thread.
    - In a terminal, execute the **display-final-after-month-is-over.py** script, which generates and automatically copies to the clipboard the final text for the (now over) previous month's challenge page, e.g. December's challenge page.
    - Edit December's challenge page, and paste in the text.
    - Un-sticky December's challenge page.
    - In a terminal, execute the **display-congratulations-after-month-is-over.py** script, which generates and automatically copies to the clipboard, text for the previous month's "congratulations to the victors..." post.
    - On the subreddit's page, click _Submit a new text post_ to create the congratulations post.  Paste in the text and title of the post, and hit submit.
    - For each of the signup pages that we created during the last week of December, edit the pages, with text that indicates that signup is over.  Use those double-tildes to "cross out" much of the original text.
- **On the mornings of January 2-3** - These are the second and third days of our late-signup grace period.
    - Refresh the browser tab that is open to http://127.0.0.1:8888/moderatechallenge.html , and use the submit buttons to _Checkin_, _Signup and Checkin_, and _Relapse_ the users who have posted comments throughout the day.
    - You can do this as many times as you wish throughout the day.
    - Because we are within our 3-day late-signup grace period, feel free to simply use the signup and checkin button, instead of the checkin button.
    - Click the _Copy display.py stdout to clipboard_ button.
    - Log into the challenge page on Reddit, edit the post, and paste in the clipboard text.
    - If you wish to customize the "Daily News" paragraph, do it now.
    - Click Save
- **On the mornings of January 4-15** - This is the first half of the month, not within the three day late-signup grace period.
    - Follow the directions of the "January 2-3" section, but do not use the signup and checkin button, only use the _Checkin_ button and _Relapse_ button.
- **On the morning of January 16** - This is the first day of the second half of the month, and those who have not checked in will be disqualified.
    - Make sure you have caught up completely on checking in and relapsing commenting users.
    - In a terminal, execute the **on-the-sixteenth.sh** script, which disqualifies everyone not yet checked in, then marks everyone else as not checked in (restoring the tilde next to their name), and copies the day's post to the clipboard.
    - Log into the challenge page on Reddit, edit the post, paste in the clipboard text, and click Save.
- **On the mornings of January 17-January 24** - These are normal days, prior to posting the signup threads for February.  If the month had 30 days instead of 31, we would follow these directions through January 23, not 24.
    - Just follow the "January 4-15" directions.
- **On any day before January 25** - We need to prepare the stayclean subdirectory for February.
    - In a terminal, cd to the stayclean directory, and then use _cp -a stayclean-2016-january stayclean-2016-february_ to recursively copy january's directory to a new directory for february.
    - _cd stayclean-2016-february_
    - Make a new participants.txt file by rm'ing the existing one and then executing _touch participants.txt_
    - Immediately sign yourself in by executing _./signup.py foobarbazblarg_
    - Several of the python scripts have variables that need to be edited for the new month.  Do a text search for _"Edit Me"_, and edit the variables, which should hopefully be self-explanatory or commented.
        - Please note that for the _challengePageSubmissionId_ variable in **serve-challenge-with-flask.py**, you will not yet know the submission ID for the February challenge page.  Just leave it as the empty string or something for now - we will fill it in on Febrary 1.
    - In preparation for the one-week signup window, start up in a terminal tab, the script that serves with Flask the signup webapp:  _cd ~/stayclean/stayclean-2016-february ; ./serve-signups-with-flask.py_
- **On the mornings of January 25-January 31** - In addition to managing the January challenge as usual, we post daily February challenge signup posts.
    - Follow the "January 4-15" directions as usual, to manage the January challenge.
    - When you created and initialized the stayclean-2016-february directory (detailed above), you should have started the signup webapp by executing _cd ~/stayclean/stayclean-2016-february ; ./serve-signups-with-flask.py_.  If not, do that now, and leave it running.
    - Bring up the signup webapp by opening _http://127.0.0.1:8890/moderatesignups.html_ in a web browser tab.  Process any signup requests that may have come in, by clicking the _Signup_ buttons.
    - Click the _Copy display-during-signup.py stdout to clipboard_ button.
    - On the subreddit's page, click _Submit a new text post_ to create a new signup post.  Paste in the text and title of the post, cut the first line (the title) and paste it into the Title field, and then hit submit.
    - Copy the 6-digit submission id code (e.g. "3v059o") from the post's URL, and add it to the _signupPageSubmissionIds_ array at the top of the **serve-signups-with-flask.py** script.

### Questions?
For more information, contact foobarbazblarg at gmail.  Keep fighting the good fight!
