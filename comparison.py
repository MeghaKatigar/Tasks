from datetime import datetime

task_list = []

for_loop_start_time = datetime.now()
for task_id in range(1000000):
    single_task_dict = {}
    single_task_dict["task_name"] = "This is a task"
    single_task_dict["status"] = "CR"
    single_task_dict["target_date"] = None
    single_task_dict["completed_at"] = None
    task_list.append(single_task_dict)
for_loop_end_time = datetime.now()

print(f"Total Time Taken by for loop {for_loop_end_time - for_loop_start_time}s")


task_list_=[]
list_comprehension_start_time = datetime.now()
task_list_ = [{"task_name" : " This is a task", "status":"CR", "target_date": None, "completed_at":None} for _ in range(1000000)]
list_comprehension_end_time = datetime.now()
print(f"Total time taken by list comprehension {list_comprehension_end_time -list_comprehension_start_time}s")