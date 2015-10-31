# StayClean

Scripts used to manage the StayClean monthly challenges for https://www.reddit.com/r/pornfree

Here's a rundown of these files, and how I use each one to manage the StayClean monthly challenges:

### Miscellaneous files

 - **participants.txt** This is the list of people who have signed up for the challenge.  It's just a space-delimited file, one record per line, with the following fields for each record:  1) The username of the user,  2) A boolean indicating whether the user has checked in at least once,  3) A boolean indicating whether the user has been disqualified for the month (i.e. has reported a relapse some time during the month)  4) (optional) the date that the user reported a relapse.  Most of the Python scripts either read from or write to this file.  This file must be present to allow the scripts to run - when you create a new month, create an empty participants.txt file by executing "touch participants.txt".

 - **participant.py, participantCollection.py** - classes used by various scripts.

### Scripts to use during the signup period (usually the week before the month starts, when people sign up for the challenge)

 - **signup.py** Use this script to sign up one or more new users.  This script is typically used before the beginning of the month, during the signup period, or during a "late signup grace period", which I sometimes offer for the first few days of the month.  Follow the script name by a list of usernames for users to sign up.

 - **display-during-signup.py** Generate and automatically copy to the clipboard, text for the daily signup post.

### Frequently used scripts to use during the challenge

 - **checkin.py** Use this script to "check in" one or more users.  Follow the script name with a list of usernames for users to check in.

 - **signup-and-checkin.sh** This is a convenience script, typically used during the "late signup grace period", to automatically sign up and check in one or more users.  Follow the script name with a list of usernames.

 - **relapse.py** Use this script to disqualify one or more users who have reported a relapse.  Follow the script name with a list of usernames for users to disqualify.

 - **display.py** Use this script once per morning to generate and automatically copy to the clipboard, text for the main "stickied" challenge post.

### Infrequently used scripts

 - **reinstate.py** This infrequently used script can be used to "un-disqualify" a user.  It is sometimes used when a user simply forgot to checkin in time, and wants to be re-added to the challenge.

 - **disqualify-all-not-checked-in.py** Use this on the 16th of the month, and after the last day of the month, to disqualify all participants who have not checked in.

 - **mark-all-as-not-checked-in.py** On the 16th, use this to mark all participants who checked in during the first half of the month, as not checked in again.

 - **on-the-sixteenth.sh** This is a convenience script, to be run on the 16th of the month.  It executes the three scripts that need to be run on that day, in the proper order.


For more information, contact foobarbazblarg at gmail.  Keep fighting the good fight!
