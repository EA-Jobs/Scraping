import csv

# Converts a selected csv to a 2-d list
def csvToList(fileName):
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list

# finds job postings on the new csv which are not on the old
# returns new jobs as a 2-d list
def updates(oldCsvName, newCsvName):
    # converts both the old csv and new csv to a list, and removes the column labels
    oldList = csvToList(oldCsvName)[1:]
    newList = csvToList(newCsvName)[1:]

    # looks through each job in the new list
    newJobs = list()
    for job in newList:
        # if the job is unique to the new list
        if job not in oldList:
            # then it adds the job to the new jobs list
            newJobs.append(job)
            
    return newJobs
