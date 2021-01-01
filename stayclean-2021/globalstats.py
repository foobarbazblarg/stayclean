#!/usr/bin/env python3

from glob import glob
from os import path
from participant import Participant

'''

- For the monthly challenges
    - Number of signups (not unique users):
    - Number of successful attempts (clean all month):
    - Number of unique reddit users that have participated:
    - Average success rate (percentage of participants that have made it through the month porn-free):
    - Counting only those who made it all the way through the challenges, the total number of days clean: .  That's  years.
- For the year-long challenges
    - Number of signups (not unique users):
    - Number of successful attempts (clean all year):
    - Number of unique reddit users that have participated:
    - Average success rate (percentage of participants that have made it through the month porn-free):
    - Counting only those who made it all the way through the challenges, the total number of days clean: .  That's  years.


'''

if __name__ == '__main__':
    monthly_directories = glob("../stayclean-????-*")
    year_long_directories = glob("../stayclean-????")
    monthly_directories.remove("../stayclean-2021-january")
    year_long_directories.remove("../stayclean-2021")

    is_monthly = True
    for directories in [monthly_directories, year_long_directories]:
        participants_file_names = [f"{d}/participants.txt" for d in directories]
        # print(participants_file_names)
        # print()
        for file_name in participants_file_names:
            if not path.exists(file_name):
                print(f"WARNING: {file_name} does not exist.")
        all_participants = []
        for file_name in participants_file_names:
            with open(file_name, "r") as file:
                for line in file.readlines():
                    participant = Participant()
                    participant.setFromLine(line)
                    all_participants.append(participant)
        all_participant_names = [part.name for part in all_participants]
        unique_participant_names = set(all_participant_names)
        # TODO - I think some of the older ones did not record a relapse date, so new code may not have accurate hasRelapsed() - need to investigate.
        # successful_participants = [part for part in all_participants if not part.hasRelapsed]
        successful_participants = [part for part in all_participants if part.isStillIn]
        successful_days = len(successful_participants) * 30 if is_monthly else len(successful_participants) * 365
        print(f'    - Number of signups (not unique users): {len(all_participants)}')
        print(f'    - Number of successful attempts (clean all {"month" if is_monthly else "year"}): {len(successful_participants)}')
        print(f'    - Average success rate (percentage of participants that were clean all {"month" if is_monthly else "year"}): {int(len(successful_participants) / len(all_participants) * 100)}')
        print(f'    - Number of unique reddit users that have participated: {len(unique_participant_names)}')
        print(f'    - Counting only those who made it all the way through the challenges, the total number of days clean: {successful_days}.  That is {successful_days / 365} years.')
        print()
        is_monthly = False
