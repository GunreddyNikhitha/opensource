def max_consecutive_absent_days(attendance_record):
    max_consecutive_absent=0
    current_consecutive_absent=0
    for day in attendance_record:
        if day == 0:
            current_consecutive_absent += 1
        else:
            max_consecutive_absent=max(max_consecutive_absent,current_consecutive_absent)
            current_consecutive_absent=0
    max_consecutive_absent=max(max_consecutive_absent,current_consecutive_absent)
    return max_consecutive_absent
n=int(input())
attendance_record=list(map(int,input().split()))
max_absent_days=max_consecutive_absent_days(attendance_record)
print(max_absent_days)
