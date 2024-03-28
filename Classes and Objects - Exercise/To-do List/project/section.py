from project import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

        # option 2
        # for task in self.tasks:
        #     if task_name == task.name:
        #         task.completed = True
        #         return f"Completed task {task_name}"
        #
        # return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0

        for tk in self.tasks:
            if tk.completed:
                self.tasks.remove(tk)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n" \
               f"{result}"


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
