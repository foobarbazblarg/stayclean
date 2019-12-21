#!/usr/bin/python
# TODO: issues with new oauth2 stuff.  Keep using older version of Python for now.
# #!/usr/bin/env python
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import datetime
from participantCollection import ParticipantCollection

# Edit Me!
participantFileNames = ['../stayclean-2014-november/participants.txt',
                        '../stayclean-2014-december/participants.txt',
                        '../stayclean-2015-january/participants.txt',
                        '../stayclean-2015-february/participants.txt',
                        '../stayclean-2015-march/participants.txt',
                        '../stayclean-2015-april/participants.txt',
                        '../stayclean-2015-may/participants.txt',
                        '../stayclean-2015-june/participants.txt',
                        '../stayclean-2015-july/participants.txt',
                        '../stayclean-2015-august/participants.txt',
                        '../stayclean-2015-september/participants.txt',
                        '../stayclean-2015-october/participants.txt',
                        '../stayclean-2015-november/participants.txt',
                        '../stayclean-2015-december/participants.txt',
                        '../stayclean-2016-january/participants.txt',
                        '../stayclean-2016-february/participants.txt',
                        '../stayclean-2016-march/participants.txt',
                        '../stayclean-2016-april/participants.txt',
                        '../stayclean-2016-may/participants.txt',
                        '../stayclean-2016-june/participants.txt',
                        '../stayclean-2016-july/participants.txt',
                        '../stayclean-2016-august/participants.txt',
                        '../stayclean-2016-september/participants.txt',
                        '../stayclean-2016-october/participants.txt',
                        '../stayclean-2016-november/participants.txt',
                        '../stayclean-2016-december/participants.txt',
                        '../stayclean-2017-january/participants.txt',
                        '../stayclean-2017-february/participants.txt',
                        '../stayclean-2017-march/participants.txt',
                        '../stayclean-2017-april/participants.txt',
                        '../stayclean-2017-may/participants.txt',
                        '../stayclean-2017-june/participants.txt',
                        '../stayclean-2017-july/participants.txt',
                        '../stayclean-2017-august/participants.txt',
                        '../stayclean-2017-september/participants.txt',
                        '../stayclean-2017-october/participants.txt',
                        '../stayclean-2017-november/participants.txt',
                        '../stayclean-2017-december/participants.txt',
                        '../stayclean-2018-january/participants.txt',
                        '../stayclean-2018-february/participants.txt',
                        '../stayclean-2018-march/participants.txt',
                        '../stayclean-2018-april/participants.txt',
                        '../stayclean-2018-may/participants.txt',
                        '../stayclean-2018-june/participants.txt',
                        '../stayclean-2018-july/participants.txt',
                        '../stayclean-2018-august/participants.txt',
                        '../stayclean-2018-september/participants.txt',
                        '../stayclean-2018-october/participants.txt',
                        '../stayclean-2018-november/participants.txt',
                        '../stayclean-2018-december/participants.txt',
                        '../stayclean-2019-january/participants.txt',
                        '../stayclean-2019-february/participants.txt',
                        '../stayclean-2019-march/participants.txt',
                        '../stayclean-2019-april/participants.txt',
                        '../stayclean-2019-may/participants.txt',
                        '../stayclean-2019-june/participants.txt',
                        '../stayclean-2019-july/participants.txt',
                        '../stayclean-2019-august/participants.txt',
                        '../stayclean-2019-september/participants.txt',
                        './participants.txt']

sortedRelapseDates = []
for participantFileName in participantFileNames:
    participants = ParticipantCollection(fileNameString=participantFileName)
    sortedRelapseDates = sortedRelapseDates + participants.allRelapseDates()
sortedRelapseDates.sort()
earliestReportDate = sortedRelapseDates[0]
latestReportDate = sortedRelapseDates[-1]
reportDates = []
numberOfRelapsesPerDate = []
reportDatesAndNumberOfRelapses = {}
dayOfWeekIndexesAndNumberOfInstances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

reportDate = earliestReportDate
while reportDate <= latestReportDate:
    reportDatesAndNumberOfRelapses[reportDate] = 0
    # dayOfWeekIndexesAndNumberOfInstances[reportDate.weekday()] = dayOfWeekIndexesAndNumberOfInstances[reportDate.weekday()] + 1
    dayOfWeekIndexesAndNumberOfInstances[reportDate.weekday()] += 1
    reportDate += datetime.timedelta(days=1)
for relapseDate in sortedRelapseDates:
    # reportDatesAndNumberOfRelapses[relapseDate] = reportDatesAndNumberOfRelapses[relapseDate] + 1
    reportDatesAndNumberOfRelapses[relapseDate] += 1
dayOfWeekIndexesAndTotalNumberOfRelapses = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for participantFileName in participantFileNames:
    participants = ParticipantCollection(fileNameString=participantFileName)
    # print participants.relapseDayOfWeekIndexesAndParticipants()
    for index, parts in participants.relapseDayOfWeekIndexesAndParticipants().iteritems():
        # dayOfWeekIndexesAndTotalNumberOfRelapses[index] = dayOfWeekIndexesAndTotalNumberOfRelapses[index] + len(parts)
        dayOfWeekIndexesAndTotalNumberOfRelapses[index] += len(parts)
dayOfWeekIndexesAndAverageNumberOfRelapses = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for index, instances in dayOfWeekIndexesAndNumberOfInstances.iteritems():
    # dayOfWeekIndexesAndAverageNumberOfRelapses[index] = int(round(float(dayOfWeekIndexesAndTotalNumberOfRelapses[index]) / float(instances)))
    dayOfWeekIndexesAndAverageNumberOfRelapses[index] = float(dayOfWeekIndexesAndTotalNumberOfRelapses[index]) / float(instances)


spreadsheetTitle = "StayClean monthly challenge relapse data"
# spreadsheetTitle = "Test spreadsheet"
json_key = json.load(open('../google-oauth-credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
spreadSheet = None
try:
    spreadSheet = gc.open(spreadsheetTitle)
except gspread.exceptions.SpreadsheetNotFound:
    print "No spreadsheet with title " + spreadsheetTitle
    exit(1)
workSheet = spreadSheet.get_worksheet(0)
columnACells = workSheet.range("A2:A" + str(len(reportDatesAndNumberOfRelapses) + 1))
columnBCells = workSheet.range("B2:B" + str(len(reportDatesAndNumberOfRelapses) + 1))
columnCCells = workSheet.range("C2:C8")
columnDCells = workSheet.range("D2:D8")

reportDate = earliestReportDate
rowIndex = 0
while reportDate <= latestReportDate:
    columnACells[rowIndex].value = str(reportDate)
    columnBCells[rowIndex].value = str(reportDatesAndNumberOfRelapses[reportDate])
    rowIndex += 1
    reportDate += datetime.timedelta(days=1)
for weekdayIndex in range(0, 7):
    weekdayName = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekdayIndex]
    # spreadsheetClient.UpdateCell(weekdayIndex + 2,3,weekdayName,spreadsheetId)
    # spreadsheetClient.UpdateCell(weekdayIndex + 2,4,str(dayOfWeekIndexesAndAverageNumberOfRelapses[weekdayIndex]),spreadsheetId)
    columnCCells[weekdayIndex].value = weekdayName
    columnDCells[weekdayIndex].value = str(dayOfWeekIndexesAndAverageNumberOfRelapses[weekdayIndex])
allCells = columnACells + columnBCells + columnCCells + columnDCells
workSheet.update_cells(allCells)

exit(0)

