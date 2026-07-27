import time
from locust import HttpUser, task, between
from datetime import datetime

class QuickstartUser(HttpUser):
    # wait_time = between(1, 5)
    host = "http://127.0.0.1:8000"

    @task
    def fetch_all_tasks(self):
        self.client.get("/api/tasks/")

    @task
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/api/tasks/{item_id}/", name="/api/task/id")
            time.sleep(1)

    @task
    def post_views(self):
        task_list = []

        for_loop_start_time = datetime.now()
        print(for_loop_start_time)
        for task_id in range(10000):
            single_task_dict = {}
            single_task_dict["task_name"] = "This is a task"
            single_task_dict["status"] = "CR"
            single_task_dict["target_date"] = None
            single_task_dict["completed_at"] = None
            task_list.append(single_task_dict)
        for_loop_end_time = datetime.now()
        print(for_loop_end_time)

        # list_comprehension_start_time = datetime.now()
        # task_list = [{"task_name" : " This is a task", "status":"CR", "target_date": None, "completed_at":None} for _ in range(10000)]
        # list_comprehension_end_time = datetime.now()
    
        self.client.post(f"/api/tasks/", json=task_list)
            