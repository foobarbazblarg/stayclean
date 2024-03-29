#!/usr/bin/env python3
from participantCollection import ParticipantCollection
import re
import datetime
import pyperclip
import editme

# EDIT ME!
# Remember, this is during signup, so current month is not January, it's December.
currentMonthTotalDays = editme.previousMonthTotalDays
year = editme.currentYear

currentMonthIndex = datetime.date.today().month
currentMonthPenultimateDayIndex = currentMonthTotalDays - 1
currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
nextMonthIndex = currentMonthIndex % 12 + 1
nextMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[nextMonthIndex]
uppercaseMonth = nextMonthName.upper()
currentDayOfMonthIndex = datetime.date.today().day
currentDayOfMonthName = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth', 16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth', 20: 'twentieth', 21: 'twenty-first', 22: 'twenty-second', 23: 'twenty-third', 24: 'twenty-fourth', 25: 'twenty-fifth', 26: 'twenty-sixth', 27: 'twenty-seventh', 28: 'twenty-eighth', 29: 'twenty-ninth', 30: 'thirtieth', 31: 'thirty-first'}[currentDayOfMonthIndex]
currentDayOfWeekName = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}[datetime.date.today().weekday()]

# TODO: testing
# currentDayOfMonthIndex = 31

participants = ParticipantCollection()
initialNumber = participants.size()


def templateForParticipants() -> str:
    answer = ""
    answer += "Here are the **INITIAL_NUMBER participants** who have already signed up:\n\n"
    for participant in participants.participants:
        answer += "/u/" + participant.name
        answer += "\n\n"
    return answer


def templateForTooEarly() -> str:
    return f"(Too early.  Come back on CURRENT_MONTH_NAME {str(currentMonthTotalDays - 6)})\n"


def templateForFirstSignupDay() -> str:
    return f'''STAY CLEAN _YEAR_ FULL-YEAR CHALLENGE!  Sign up here!  (CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX)
Our monthly Stay Clean challenges are quite popular; people seem to like them and benefit from them.  Of course we will continue those monthly challenges, but for the sixth year in a row, we will be hosting a FULL-YEAR challenge! The challenge will run for the entire year, and on December 31, _YEAR_, an elite group of victorious participants will have earned some serious bragging rights!

If you're ready to step it up a notch, sign up for this year-long challenge by leaving a brief comment to this thread.  After midnight, NEXT_MONTH_NAME 1, the sign up window will close, and the challenge will begin.

**Please note** that signing up here will NOT automatically sign you up for the Stay Clean January _YEAR_ monthly challenge, and you'll want to sign up for that too.  [To sign up for that, go here](https://www.reddit.com/r/pornfree/comments/rnfmfd/stay_clean_january_sign_up_here_december_24/)
'''


def templateForMiddleSignupDays() -> str:
    return f'''STAY CLEAN _YEAR_ FULL-YEAR CHALLENGE!  Sign up here!  (CURRENT_MONTH_NAME CURRENT_DAY_OF_MONTH_INDEX)
Hey everybody, so far **INITIAL_NUMBER participants** have signed up for our Stay Clean _YEAR_ full-year challenge.  Think you're ready to go an entire year without porn?  I know that together, we can do it, so sign up today!

If you would like to be included in this challenge, please post a brief comment to this thread (if you haven't already done so on an earlier signup thread), and I will include you.  After midnight, NEXT_MONTH_NAME 1, the sign up window will close, and the challenge will begin.

**Please note** that signing up here will NOT automatically sign you up for the Stay Clean January _YEAR_ monthly challenge, and you'll want to sign up for that too.  [To sign up for that, go here](https://www.reddit.com/r/pornfree/comments/rnfmfd/stay_clean_january_sign_up_here_december_24/)

{templateForParticipants()}'''


def templateForLastSignupDay() -> str:
    return f'''LAST CHANCE TO SIGN UP FOR STAY CLEAN _YEAR_ FULL-YEAR CHALLENGE!  Sign up here!
The Stay Clean _YEAR_ full-year challenge **begins tomorrow**!  So far, we have **INITIAL_NUMBER participants** signed up.  To paraphrase John F. Kennedy:  \"We choose to quit porn, not because it is easy, but because it is hard\".  I know that together, we are up to this challenge, so sign up today!

If you would like to be included in the challenge, please post a brief comment to this thread (if you haven't already done so on an earlier signup thread), and we will include you.  After midnight tonight, we will not be accepting any more participants.  I will create the official update post tomorrow.

**Please note** that signing up here will NOT automatically sign you up for the Stay Clean January _YEAR_ monthly challenge, and you'll want to sign up for that too.  [To sign up for that, go here](https://www.reddit.com/r/pornfree/comments/rnfmfd/stay_clean_january_sign_up_here_december_24/)

{templateForParticipants()}'''


def templateToUse() -> str:
    # TODO testing...
    # return templateForFirstSignupDay()
    # return templateForMiddleSignupDays()
    # return templateForLastSignupDay()

    if (currentMonthIndex < 12) or (currentDayOfMonthIndex <= (currentMonthTotalDays - 8)):
    # if (currentMonthIndex < 12) or (currentDayOfMonthIndex <= (currentMonthTotalDays - 7)):
        return templateForTooEarly()
    elif currentDayOfMonthIndex == (currentMonthTotalDays - 7):
    # elif currentDayOfMonthIndex == (currentMonthTotalDays - 6):
        return templateForFirstSignupDay()
    elif (currentMonthTotalDays - 6) <= currentDayOfMonthIndex <= (currentMonthTotalDays - 1):
    # elif (currentMonthTotalDays - 5) <= currentDayOfMonthIndex <= (currentMonthTotalDays - 1):
        return templateForMiddleSignupDays()
    elif currentMonthTotalDays == currentDayOfMonthIndex:
        return templateForLastSignupDay()


def stringToPrint() -> str:
    answer = templateToUse()
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('CURRENT_MONTH_INDEX', str(currentMonthIndex), answer)
    answer = re.sub('CURRENT_MONTH_TOTAL_DAYS', str(currentMonthTotalDays), answer)
    answer = re.sub('CURRENT_MONTH_PENULTIMATE_DAY_INDEX', str(currentMonthPenultimateDayIndex), answer)
    answer = re.sub('CURRENT_MONTH_NAME', currentMonthName, answer)
    answer = re.sub('NEXT_MONTH_INDEX', str(nextMonthIndex), answer)
    answer = re.sub('NEXT_MONTH_NAME', nextMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_INDEX', str(currentDayOfMonthIndex), answer)
    answer = re.sub('CURRENT_DAY_OF_MONTH_NAME', currentDayOfMonthName, answer)
    answer = re.sub('CURRENT_DAY_OF_WEEK_NAME', currentDayOfWeekName, answer)
    answer = re.sub('UPPERCASE_MONTH', uppercaseMonth, answer)
    answer = re.sub('_YEAR_', str(year), answer)
    return answer


if __name__ == "__main__":
    outputString = stringToPrint()
    print("=============================================================")
    print(outputString)
    print("=============================================================")
    pyperclip.copy(outputString)
