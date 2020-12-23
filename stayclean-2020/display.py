#!/usr/bin/env python3
from participantCollection import ParticipantCollection
import re
import datetime
import time
import pyperclip

# EDIT ME
currentMonthTotalDays = 31
year = 2020

currentMonthIndex = datetime.date.today().month
currentDayOfMonthIndex = datetime.date.today().day
currentDayOfYearIndex = time.localtime().tm_yday

# TODO: testing...
# currentMonthTotalDays = 31
# currentMonthIndex = 12
# currentDayOfMonthIndex = 31
# currentDayOfYearIndex = 366

currentMonthPenultimateDayIndex = currentMonthTotalDays - 1
currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
nextMonthIndex = currentMonthIndex % 12 + 1
nextMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[nextMonthIndex]
currentDayOfMonthName = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth', 16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth', 20: 'twentieth', 21: 'twenty-first', 22: 'twenty-second', 23: 'twenty-third', 24: 'twenty-fourth', 25: 'twenty-fifth', 26: 'twenty-sixth', 27: 'twenty-seventh', 28: 'twenty-eighth', 29: 'twenty-ninth', 30: 'thirtieth', 31: 'thirty-first'}[currentDayOfMonthIndex]
currentDayOfWeekName = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}[datetime.date.today().weekday()]

participants = ParticipantCollection()
numberStillIn = participants.sizeOfParticipantsWhoAreStillIn()
initialNumber = participants.size()
percentStillIn = int(round(100 * numberStillIn / initialNumber, 0))


def templateForParticipants() -> str:
    answer = ""
    for participant in participants.participantsWhoAreStillIn():
        answer += "/u/" + participant.name
        if not participant.hasCheckedIn:
            answer += " ~"
        answer += "\n\n"
    return answer


def templateForParticipantsOnLastDayOfMonth() -> str:
    answer = ""
    answer += "These participants have checked in at least once in CURRENT_MONTH_NAME:\n"
    answer += "\n"
    for participant in participants.participantsWhoAreStillInAndHaveCheckedIn():
        answer += "/u/" + participant.name + "\n"
        answer += "\n"
    answer += "These participants have not reported a relapse, so they are still in the running, but **if they do not check in by the end of today, they will be removed from the list**:\n"
    answer += "\n"
    for participant in participants.participantsWhoAreStillInAndHaveNotCheckedIn():
        answer += "/u/" + participant.name + " ~\n"
        answer += "\n"
    return answer


def templateForJan1() -> str:
    # first day of the challenge, and late signup grace period
    print("using templateForJan1")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is the very first day of the year-long Stay Clean YEAR challenge.  ~~We will no longer be accepting new signups.~~  Good news! We will be be accepting late signups for the next 14 days. If you forgot to sign up for the YEAR challenge, and you've been clean for all of January, just leave a \"sign me up\" comment below, and I'll add you.  Best of luck to everyone here!

Here's how this thing works:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- ~~We will not be accepting any new participants~~, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

Here are our **INITIAL_NUMBER** original participants:

{templateForParticipants()}'''


def templateForJan2to13() -> str:
    # late signup grace period
    print("using templateForJan2to13")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  This is the CURRENT_DAY_OF_MONTH_NAME day of our 14 day late-signup grace period.  If you forgot to sign up for the YEAR challenge, and you've been clean for all of January, just leave a \"sign me up\" comment below, and I'll add you.

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- ~~We will not be accepting any new participants~~, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForJan14() -> str:
    # last day of late signup grace period
    print("using templateForJan14")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  This is the **last day** of our 14 day late-signup grace period.  If you forgot to sign up for the YEAR challenge, and you've been clean for all of January, just leave a \"sign me up\" comment below, and I'll add you.  After today, further signup requests will be silently ignored.

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- ~~We will not be accepting any new participants~~, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForJan15() -> str:
    # first day AFTER the late signup grace period
    print("using templateForJan15")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Our 14 day late-signup grace period is now over.  If you forgot to sign up, it's too late to sign up for Stay Clean YEAR, but feel free to leave comments here anyway, and join us over on the monthly challenge thread.

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForJan16to25() -> str:
    # first day AFTER the late signup grace period
    print("using templateForJan16to25")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForJan26to30() -> str:
    print("using templateForJan26to30")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

**THE COUNTDOWN: Attention everyone!** You have {str(currentMonthTotalDays - currentDayOfMonthIndex)} days to make a checkin comment (if you haven't already done so in CURRENT_MONTH_NAME) to be counted as an active participant! **Otherwise your name will be REMOVED from the list** on CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS!!

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForJan31() -> str:
    print("using templateForJan31")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

**THIS IS YOUR LAST DAY TO CHECK IN** (if you haven't already done so in CURRENT_MONTH_NAME) **BEFORE YOUR NAME IS REMOVED FROM THE LIST!**  Check in by posting a brief comment.

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.

{templateForParticipantsOnLastDayOfMonth()}'''


def templateForUltimateMinus5toPenultimateDayOfMonth() -> str:
    print("using templateForUltimateMinus5toPenultimateDayOfMonth")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

**THE COUNTDOWN: Attention everyone!** You have " + str(currentMonthTotalDays - currentDayOfMonthIndex) + " days to make a checkin comment (if you haven't already done so in CURRENT_MONTH_NAME) to be counted as an active participant! **Otherwise your name will be REMOVED from the list** on CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS!!

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForUltimateDayOfMonth() -> str:
    print("using templateForUltimateDayOfMonth")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

**THIS IS YOUR LAST DAY TO CHECK IN** (if you haven't already done so in CURRENT_MONTH_NAME) **BEFORE YOUR NAME IS REMOVED FROM THE LIST!**  Check in by posting a brief comment.

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipantsOnLastDayOfMonth()}'''


def templateForUltimateMinus5toPenultimateDayOfYear() -> str:
    print("using templateForUltimateMinus5toPenultimateDayOfYear")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

**THE COUNTDOWN: Attention everyone!** You have {str(currentMonthTotalDays - currentDayOfMonthIndex)} days to make a checkin comment (if you haven't already done so in CURRENT_MONTH_NAME) to be counted as an active participant! **Otherwise your name will be REMOVED from the list** on CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS!!

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateForUltimateDayOfYear() -> str:
    print("using templateForUltimateDayOfYear")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, the very last day of the Stay Clean YEAR challenge.  This is it, folks, the day we've been waiting for... the final day of the challenge.  I'll be making a congratulatory post tomorrow to honor the victors.

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

{templateForParticipantsOnLastDayOfMonth()}'''


def templateForNormalDay() -> str:
    print("using templateForNormalDay")
    print("=============================================================")
    return f'''**Daily news:**  This is CURRENT_DAY_OF_WEEK_NAME, CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX, and today is **day CURRENT_DAY_OF_YEAR_INDEX** of the year-long Stay Clean YEAR challenge.  Keep fighting the good fight!

If you think you should still be on this list but aren't, you probably got removed for not checking in at least once per month. However, if you let me know you're still with it I'll re-add you.

Guidelines:

- At the end of this post is a list of people who have signed up for the challenge, and who are still in the running.  That means that they have not needed to reset because of a relapse or slip.
- Please check in with the group in the comments as often as you want! Feel free to share thoughts, feelings, experiences, progress, wisdom, encouragement and whatever else!
- **IMPORTANT: if you relapse, please post a comment to that effect here** and I will remove your name from the list.  We will not judge you or shame you, we have all been there.
- Participants are required to check in once per month.  If you have a "~" after your name, you have yet to check in during CURRENT_MONTH_NAME. If it is still there at the end of CURRENT_MONTH_NAME CURRENT_MONTH_TOTAL_DAYS, you will be removed from the list, in order to keep the numbers as realistic as possible.
- We will not be accepting any new participants, but even if you're not on the list, please feel free to check in in the update threads anyway!  And be sure to join us for the Stay Clean monthly thread!

Good luck!

There are currently **NUMBER_STILL_IN out of INITIAL_NUMBER** original participants.  That's **PERCENT_STILL_IN%**.  These NUMBER_STILL_IN participants represent **CUMULATIVE_DAYS_BY_THOSE_STILL_IN pornfree days** in YEAR!  That's more than **CUMULATIVE_YEARS_BY_THOSE_STILL_IN years**.

Here is the list of participants still with the challenge:

{templateForParticipants()}'''


def templateToUse() -> str:
    # TODO - testing
    # return templateForJan1()
    # return templateForJan2to13()
    # return templateForJan14()
    # return templateForJan15()
    # return templateForJan16to25()
    # return templateForJan26to30()
    # return templateForJan31()
    # return templateForUltimateMinus5toPenultimateDayOfYear()
    # return templateForUltimateDayOfYear()
    # return templateForNormalDay()

    # if currentDayOfMonthIndex == 1:
    #     return templateFor1()
    # elif currentDayOfMonthIndex == 2:
    #     return templateFor2()
    # elif currentDayOfMonthIndex == 3:
    #     return templateFor3()
    # elif currentDayOfMonthIndex == 4:
    #     return templateFor4()
    # elif 5 <= currentDayOfMonthIndex <= 9:
    #     return templateFor5to9()
    # elif 10 <= currentDayOfMonthIndex <= 14:
    #     return templateFor10to14()
    # if currentDayOfMonthIndex == 15:
    #     return templateFor15()
    # elif (currentDayOfMonthIndex >= 16) and (currentDayOfMonthIndex <= currentMonthPenultimateDayIndex):
    #     return templateFor16toPenultimate()
    # else:
    #     return templateForUltimate()
    if currentDayOfYearIndex == 1:
        return templateForJan1()
    elif 2 <= currentDayOfYearIndex <= 13:
        return templateForJan2to13()
    elif currentDayOfYearIndex == 14:
        return templateForJan14()
    elif currentDayOfYearIndex == 15:
        return templateForJan15()
    elif 16 <= currentDayOfYearIndex <= 25:
        return templateForJan16to25()
    elif 26 <= currentDayOfYearIndex <= 30:
        return templateForJan26to30()
    elif currentDayOfYearIndex == 31:
        return templateForJan31()
    elif currentMonthName == "December" and (26 <= currentDayOfMonthIndex <= 30):
        return templateForUltimateMinus5toPenultimateDayOfYear()
    elif currentMonthName == "December" and currentDayOfMonthIndex == 31:
        return templateForUltimateDayOfYear()
    # elif (currentDayOfMonthIndex >= 16) and (currentDayOfMonthIndex <= currentMonthPenultimateDayIndex):
    elif (currentMonthPenultimateDayIndex - 4) <= currentDayOfMonthIndex <= currentMonthPenultimateDayIndex:
        return templateForUltimateMinus5toPenultimateDayOfMonth()
    elif currentDayOfMonthIndex == currentMonthTotalDays:
        return templateForUltimateDayOfMonth()
    else:
        return templateForNormalDay()


def stringToPrint() -> str:
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
    answer = re.sub('CURRENT_DAY_OF_YEAR_INDEX', str(currentDayOfYearIndex), answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_NAME', currentDayOfMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_WEEK_NAME', currentDayOfWeekName, answer)
    answer = re.sub('CUMULATIVE_DAYS_BY_THOSE_STILL_IN', str(currentDayOfYearIndex * numberStillIn), answer)
    answer = re.sub('CUMULATIVE_YEARS_BY_THOSE_STILL_IN', str(int(currentDayOfYearIndex * numberStillIn / 365)), answer)
    answer = re.sub('YEAR', str(year), answer)
    return answer


if __name__ == "__main__":
    outputString = stringToPrint()
    print("=============================================================")
    print(outputString)
    print("=============================================================")
    pyperclip.copy(outputString)
