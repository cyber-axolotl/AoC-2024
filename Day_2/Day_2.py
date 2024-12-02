# AoC - Day 2
# Federico Pevere - 2024

def calculate_level_diffs(report):
    """
    Calculate level differences of a report. Return the list of differences.
    """
    return [(report[idx+1]-level) for idx,level in enumerate(report[:-1])]


def is_safe(report):
    """
    Check if the difference between levels in a report are all between -3 and -1 or
    all between 1 and 3.
    Input: levels as a list of levels of the report
    Returns True or False
    """
    level_diffs = calculate_level_diffs(report)
    return ((all(a >= 1 and a <= 3 for a in level_diffs)) or 
            (all(a <= -1 and a >= -3 for a in level_diffs)))

# ---- Part One ----
print('----- Day 2 Part One -----')

# Open the puzzle input file for reading
with open("input.txt", "r") as file:
    # Initialize the lists of reports
    reports = []
    for line in file:
        # Each line is a report containing a list of levels
        reports.append([int(i) for i in line.split()])

# DEBUG
#print('Reports: ', reports)

safe_reports = reports.__len__()*[False]
n_safe_reports = 0
for idx, report in enumerate(reports):
    if is_safe(report):
        n_safe_reports += 1
        safe_reports[idx] = True

#print('Safe reports: ', safe_reports)

# count number of safe reports
n_safe_reports = sum(1 for x in safe_reports if x)
print('Number of safe reports: ', n_safe_reports)

# ---- Part Two ----
print('----- Day 2 Part Two -----')

for report in reports:
    # if the report was not safe check if it can become safe
    # by fixing one failure by problem dampener
    if not is_safe(report):
        for idx in range(report.__len__()):
            if is_safe(report[0:idx]+report[idx+1:]):
                print(f'Report {report} is now safe by removing level n. {idx+1}')
                n_safe_reports += 1
                safe_reports[idx] = True
                break

print('Number of safe reports w problem dampener: ', n_safe_reports)