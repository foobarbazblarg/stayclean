#!/usr/bin/python
from participantCollection import ParticipantCollection
import re
import datetime
import pyperclip

# EDIT ME!
currentMonthTotalDays = 31

currentMonthIndex = datetime.date.today().month
currentMonthPenultimateDayIndex = currentMonthTotalDays - 1
currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
nextMonthIndex = currentMonthIndex % 12 + 1
nextMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[nextMonthIndex]
currentDayOfMonthIndex = datetime.date.today().day
# TODO: testing...
# currentDayOfMonthIndex = 31
currentDayOfMonthName = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth', 16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth', 20: 'twentieth', 21: 'twenty-first', 22: 'twenty-second', 23: 'twenty-third', 24: 'twenty-fourth', 25: 'twenty-fifth', 26: 'twenty-sixth', 27: 'twenty-seventh', 28: 'twenty-eighth', 29: 'twenty-ninth', 30: 'thirtieth', 31: 'thirty-first'}[currentDayOfMonthIndex]
currentDayOfWeekName = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}[datetime.date.today().weekday()]


participants = ParticipantCollection()
numberStillIn = participants.sizeOfParticipantsWhoAreStillIn()
initialNumber = participants.size()
percentStillIn = int(round(100 * numberStillIn / initialNumber, 0))


# print "There are currently **" + str(numberStillIn) + " out of " + str(initialNumber) +"** original participants.  That's **" + str(int(round(100*numberStillIn/initialNumber,0))) + "%**  Here is the list of participants still with the challenge:\n"

def stringToPrintLegacy():
    answer = "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer = re.sub('NUMBER_STILL_IN', str(numberStillIn), answer)
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('PERCENT_STILL_IN', str(percentStillIn), answer)
    for participant in participants.participantsWhoAreStillIn():
        answer += "/u/" + participant.name
        if not participant.hasCheckedIn:
            answer += " ~"
        answer += "\n\n"
    return answer


def templateForParticipants():
    answer = ""
    for participant in participants.participantsWhoAreStillIn():
        answer += "/u/" + participant.name
        if not participant.hasCheckedIn:
            answer += " ~"
        answer += "\n\n"
    return answer


def templateForParticipantsOnFinalDay():
    answer = ""

    answer += "These participants have checked in at least once in the last 15 days:\n"
    answer += "\n"
    for participant in participants.participantsWhoAreStillInAndHaveCheckedIn():
        answer += "/u/" + participant.name + "\n"
        answer += "\n"
    answer += "These participants have not reported a relapse, so they are still in the running, but **if they do not check in by the end of today, they will be removed from the list, and will not be considered victorious**:\n"
    answer += "\n"
    for participant in participants.participantsWhoAreStillInAndHaveNotCheckedIn():
        answer += "/u/" + participant.name + " ~\n"
        answer += "\n"
    return answer


def templateFor1():
    print '1\n\n'
    answer = ""
    print "============================================================="
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  ~~We will no longer be accepting new signups.~~  Good news! We will be be accepting late signups for the next 3 days. If you forgot to sign up for the CURRENT_MONTH_NAME challenge, just leave a \"sign me up\" comment below, and I'll add you.  Best of luck to everyone here!\n"
    answer += "\n"
    answer += "Here's how this thing works:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- ~~We will not be accepting any new participants~~, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "Here are our **INITIAL_NUMBER** original participants:\n\n"
    answer += templateForParticipants()
    print "============================================================="
    return answer


def templateFor2():
    print '2\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  This is the second day of our 3 day late-signup grace period.  If you forgot to sign up for the CURRENT_MONTH_NAME challenge, just leave a \"sign me up\" comment below, and I'll add you.\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- ~~We will not be accepting any new participants~~, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateFor3():
    print '3\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  This is the last day of our 3 day late-signup grace period.  If you forgot to sign up for the CURRENT_MONTH_NAME challenge, just leave a \"sign me up\" comment below, and I'll add you.  After today, further signup requests will be silently ignored.\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- ~~We will not be accepting any new participants~~, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateFor4():
    print '4\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  Our 3 day late-signup grace period is now over.  If you forgot to sign up, it's too late for CURRENT_MONTH_NAME, but feel free to leave comments here anyway, and we'll see you in NEXT_MONTH_NAME.\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateFor5to9():
    print '5 to 9\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  Keep fighting the good fight!\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateFor10to14():
    print '10 to 14\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  Keep fighting the good fight!\n"
    answer += "\n"
    answer += "**THE COUNTDOWN: Attention everyone!** You have " + str(15 - currentDayOfMonthIndex) + " days to make an update comment (if you haven't already) to be counted as an active participant! **Otherwise your name will be REMOVED from the list** on CURRENT_MONTH_INDEX/15!!\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateFor15():
    print '15\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  Keep fighting the good fight!\n"
    answer += "\n"
    answer += "**THIS IS YOUR LAST DAY TO CHECK IN** (if you haven't already) **BEFORE YOUR NAME IS REMOVED FROM THE LIST!**  Check in by posting a brief comment.\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads. If it is still there by CURRENT_MONTH_NAME 15th, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateFor16toPenultimate():
    print '16 to penultimate\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the CURRENT_DAY_OF_MONTH_NAME day of the Stay Clean CURRENT_MONTH_NAME challenge.  Keep fighting the good fight!\n"
    answer += "\n"
    answer += "If you think you should still be on this list but aren't, you probably got removed in the great purge of CURRENT_MONTH_NAME 15th because you never checked in. However, if you let me know you're still with it I will re-add you.\n"
    answer += "\n"
    answer += "Guidelines:\n"
    answer += "\n"
    answer += "- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.\n"
    answer += "- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!\n"
    answer += "- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.\n"
    answer += '- If you have a "~" after your name, you have yet to check in on any update threads since CURRENT_MONTH_NAME 15. If it is still there by CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.\n'
    answer += "- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  Also, stay tuned to catch the NEXT_MONTH_NAME thread!\n"
    answer += "\n"
    answer += "Good luck!\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  Here is the list of participants still with the challenge:\n\n"
    answer += templateForParticipants()
    return answer


def templateForUltimate():
    print 'Ultimate\n\n'
    answer = ""
    answer += "**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the last day of the Stay Clean CURRENT_MONTH_NAME challenge.  This is it, folks, the day we've been waiting for... the final day of the challenge.  I'll be making a congratulatory post tomorrow to honor the victors.  I'm really proud of everyone who signed up for this challenge.  Quitting porn is difficult, especially in an era where porn is always as close as a few keystrokes, and triggers are absolutely everywhere.  Everybody who gave it their best shot deserves to take a minute right now to feel good about themselves.\n"
    answer += "\n"
    answer += "For a chart of relapse data, check out [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1fnRMkDqFAJpsWHaZt8duMkZIPBCtUy0IfGFmlIfvOII/edit#gid=0).\n"
    answer += "\n"
    # TODO:  need to do the part where it lists the checked in and non-checked in participants separately.
    answer += "There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.\n\n"
    answer += templateForParticipantsOnFinalDay()
    return answer


def templateToUse():
    if currentDayOfMonthIndex == 1:
        return templateFor1()
    elif currentDayOfMonthIndex == 2:
        return templateFor2()
    elif currentDayOfMonthIndex == 3:
        return templateFor3()
    elif currentDayOfMonthIndex == 4:
        return templateFor4()
    elif 5 <= currentDayOfMonthIndex <= 9:
        return templateFor5to9()
    elif 10 <= currentDayOfMonthIndex <= 14:
        return templateFor10to14()
    if currentDayOfMonthIndex == 15:
        return templateFor15()
    elif (currentDayOfMonthIndex >= 16) and (currentDayOfMonthIndex <= currentMonthPenultimateDayIndex):
        return templateFor16toPenultimate()
    else:
        return templateForUltimate()


def stringToPrint():
    answer = templateToUse()
    answer = re.sub('NUMBER_STILL_IN', str(numberStillIn), answer)
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('PERCENT_STILL_IN', str(percentStillIn), answer)
    answer = re.sub('CURRENT_MONTH_INDEX', str(currentMonthIndex), answer)
    answer = re.sub('CURRENT_MONTH_TOTAL_DAYS', str(currentMonthTotalDays), answer)
    answer = re.sub('CURRENT_MONTH_PENULTIMATE_DAY_INDEX', str(currentMonthPenultimateDayIndex), answer)
    answer = re.sub('CURRENT_MONTH_NAME', currentMonthName, answer)
    answer = re.sub('NEXT_MONTH_INDEX', str(nextMonthIndex), answer)
    answer = re.sub('NEXT_MONTH_NAME', nextMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_INDEX', str(currentDayOfMonthIndex), answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_NAME', currentDayOfMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_WEEK_NAME', currentDayOfWeekName, answer)
    return answer


outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)


