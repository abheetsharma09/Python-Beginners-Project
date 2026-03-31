# Project 01: Server Log Error Counter
# Goal: Scan a log file and summarize the number of critical errors.

error_count = 0

# 1. Reading the source data
with open("server_logs.txt", "r") as log_file:
    lines = log_file.readlines()
    for line in lines:
        # We look for "ERROR," to ensure we match the status code specifically
        if "ERROR," in line:
            error_count += 1

# 2. Writing the analysis report
with open("log_result.txt", "w") as report_file:
    report_file.write(f"ANALYSIS REPORT\n")
    report_file.write(f"----------------\n")
    report_file.write(f"Total ERROR status codes found: {error_count}\n")

print(f"Analysis Complete. {error_count} errors logged in log_result.txt")
