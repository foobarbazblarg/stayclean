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
- http://127.0.0.1:8888/moderatechallenge.html - When this URL is reloaded in the browser, the serve-challenge-with-flask.py script uses the reddit API to retrieve all comments from the challenge reddit page.  For every new comment (i.e. every comment that has not yet been acted on by me), it displays the username of the commenter, the body of the comment, and a form with four submit buttons:

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
- **On January 1** - The first day of the month is by far the most complex day.  Every other day is simple, honest.  We have already been using (during the last week of December) the signup.py script and/or the http://127.0.0.1:8890/moderatesignups.html flask webapp to sign people up.  I.e. there are already many lines in ~/stayclean/stayclean-2016-january/participants.txt.
    - cd to the ~/stayclean/stayclean-2016-january directory.
    - execute the **display.py** script, which generates the first day's challenge page text, and copies it to the clipboard.
    - Bring up a browser on the subreddit, and click "Submit a new text post" to create the challenge post.  Give the new post a title of "STAY CLEAN: JANUARY! This thread updated daily - Check in here!"  Paste the page text into the form and hit Submit.
    - Sticky the new post.
    - Copy the 6-digit submission id code (e.g. "3v059o") from the post's URL, and paste it into the challengePageSubmissionId portion at the top of the **serve-challenge-with-flask.py** script.
    - In a long-running browser tab, open the http://127.0.0.1:8888/moderatechallenge.html flask webapp.  From now on, much of the heavy lifting of managing the monthly challenge can be done from this browser tab.
    - cd to the previous month's directory, e.g. ~/stayclean/stayclean-2015-december
    - execute the **disqualify-all-not-checked-in.py** script.
    - Edit the **display-final-after-month-is-over.py** script, and edit the nextMonthURL value at the top of the script, pasting in the URL for the new January thread.
    - execute the **display-final-after-month-is-over.py** script, which generates and automatically copies to the clipboard the final text for the (now over) previous month's challenge page, e.g. December's challenge page.
    - Edit December's challenge page, and paste in the text.
    - Un-sticky December's challenge page.
    - execute the **display-congratulations-after-month-is-over.py** script, which generates and automatically copies to the clipboard, text for the previous month's "congratulations to the victors..." post.
    - On the subreddit's page, click "Submit a new text post" to create the congratulations post.  Paste in the text and title of the post, and hit submit.
    - For each of the signup pages that we created during the last week of December, edit the pages, with text that indicates that signup is over.  Use those double-tildes to "cross out" much of the original text.
- _Workflow for the other days of the month, to be documented soon._

### Questions?
For more information, contact foobarbazblarg at gmail.  Keep fighting the good fight!
