#!/usr/bin/python
# TODO: issues with new oauth2 stuff.  Keep using older version of Python for now.
# #!/usr/bin/env python

from participantCollection import ParticipantCollection
import string
import re
import datetime
import pyperclip

# Edit Me!
# Remember, this is during signup, so current month is not March, it's February.
currentMonthTotalDays = 31
currentMonthURL = "https://www.reddit.com/r/pornfree/comments/6km7me/stay_clean_july_this_thread_updated_daily_check/"

currentMonthIndex = datetime.date.today().month
currentMonthPenultimateDayIndex = currentMonthTotalDays - 1
currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
nextMonthIndex = currentMonthIndex % 12 + 1
nextMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[nextMonthIndex]
uppercaseMonth = string.upper(nextMonthName)
currentDayOfMonthIndex = datetime.date.today().day
currentDayOfMonthName = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth', 16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth', 20: 'twentieth', 21: 'twenty-first', 22: 'twenty-second', 23: 'twenty-third', 24: 'twenty-fourth', 25: 'twenty-fifth', 26: 'twenty-sixth', 27: 'twenty-seventh', 28: 'twenty-eighth', 29: 'twenty-ninth', 30: 'thirtieth', 31: 'thirty-first'}[currentDayOfMonthIndex]
currentDayOfWeekName = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}[datetime.date.today().weekday()]

# TODO: testing
# currentDayOfMonthIndex = 28

participants = ParticipantCollection()
initialNumber = participants.size()


def templateForParticipants():
    answer = ""
    answer += "Here are the **INITIAL_NUMBER participants** who have already signed up:\n\n"
    for participant in participants.participants:
        answer += "/u/" + participant.name
        answer += "\n\n"
    return answer


def templateForTooEarly():
    answer = ""
    answer += "(Too early.  Come back on CURRENT_MONTH_NAME " + str(currentMonthTotalDays - 6) + ")\n"
    return answer


def templateForFirstSignupDay():
    answer = ""
    answer += "STAY CLEAN UPPERCASE_MONTH!  Sign up here!  (CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX)\n"
    answer += "Hey everybody, we had a great turnout for [Stay Clean CURRENT_MONTH_NAME](CURRENT_MONTH_URL) - let's see if we can knock it out of the park for NEXT_MONTH_NAME.  Have you been clean for the month of CURRENT_MONTH_NAME?  Great!  Join us here, and let's keep our streak going.  Did you slip in CURRENT_MONTH_NAME?  Then NEXT_MONTH_NAME is your month to shine, and we will gladly fight the good fight along with you.  Did you miss out on the CURRENT_MONTH_NAME challenge?  Well then here is your opportunity to join us.\n"
    answer += "\n"
    answer += "If you would like to be included in this challenge, please post a brief comment to this thread, and I will include you.  After midnight, NEXT_MONTH_NAME 1, the sign up window will close, and the challenge will begin."
    return answer


def templateForMiddleSignupDays():
    answer = ""
    answer += "STAY CLEAN UPPERCASE_MONTH!  Sign up here!  (CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX)\n"
    answer += "Hey everybody, so far **INITIAL_NUMBER participants** have signed up.  Have you been clean for **[the month of CURRENT_MONTH_NAME](CURRENT_MONTH_URL)**?  Great!  Join us here, and let's keep our streak going.  Did you slip in CURRENT_MONTH_NAME?  Then NEXT_MONTH_NAME is your month to shine, and we will gladly fight the good fight along with you.  Did you miss out on the CURRENT_MONTH_NAME challenge?  Well then here is your opportunity to join us.\n"
    answer += "\n"
    answer += "If you would like to be included in this challenge, please post a brief comment to this thread (if you haven't already done so on an earlier signup thread), and I will include you.  After midnight, NEXT_MONTH_NAME 1, the sign up window will close, and the challenge will begin.\n"
    answer += "\n"
    answer += templateForParticipants()
    return answer


def templateForLastSignupDay():
    answer = ""
    answer += "LAST CHANCE TO SIGN UP FOR STAY CLEAN UPPERCASE_MONTH!  Sign up here!\n"
    answer += "The Stay Clean NEXT_MONTH_NAME challenge **begins tomorrow**!  So far, we have **INITIAL_NUMBER participants** signed up.  If you would like to be included in the challenge, please post a brief comment to this thread (if you haven't already done so on an earlier signup thread), and we will include you.  After midnight tonight, we will not be accepting any more participants.  I will create the official update post tomorrow.\n"
    answer += "\n"
    answer += templateForParticipants()
    return answer


def templateToUse():
    if currentDayOfMonthIndex <= (currentMonthTotalDays - 7):
        return templateForTooEarly()
    elif currentDayOfMonthIndex == (currentMonthTotalDays - 6):
        return templateForFirstSignupDay()
    elif (currentMonthTotalDays - 5) <= currentDayOfMonthIndex <= (currentMonthTotalDays - 1):
        return templateForMiddleSignupDays()
    elif currentMonthTotalDays == currentDayOfMonthIndex:
        return templateForLastSignupDay()


def stringToPrint():
    answer = templateToUse()
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('CURRENT_MONTH_INDEX', str(currentMonthIndex), answer)
    answer = re.sub('CURRENT_MONTH_TOTAL_DAYS', str(currentMonthTotalDays), answer)
    answer = re.sub('CURRENT_MONTH_PENULTIMATE_DAY_INDEX', str(currentMonthPenultimateDayIndex), answer)
    answer = re.sub('CURRENT_MONTH_NAME', currentMonthName, answer)
    answer = re.sub('CURRENT_MONTH_URL', currentMonthURL, answer)
    answer = re.sub('NEXT_MONTH_INDEX', str(nextMonthIndex), answer)
    answer = re.sub('NEXT_MONTH_NAME', nextMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_INDEX', str(currentDayOfMonthIndex), answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_NAME', currentDayOfMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_WEEK_NAME', currentDayOfWeekName, answer)
    answer = re.sub('UPPERCASE_MONTH', uppercaseMonth, answer)
    return answer


outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)
