class Tasks: 
    new_list = []
    def __init__(self, *args):
        iter_args = iter(args)
        if len(args) > 0:
            self.name = next(iter_args)
            self.till_datetime = next(iter_args)
            new_task = f"{self.name} {self.till_datetime}"
            self.new_list.append(new_task)
    def add_task(self, name, till_datetime):
        new_task = f"{name} {till_datetime}"
        self.new_list.append(new_task)
    
    def remove_task(self, name, till_datetime):
        old_task = f"{name} {till_datetime}"
        self.new_list.remove(old_task)


    def display_tasks(self):
        for i in self.new_list:
            print(i)

    # implementation


tasks = Tasks()

tasks.add_task('first', '2022-05-24 12:00:00')
tasks.add_task('second', '2022-05-24 13:00:00')
tasks.add_task('third', '2022-05-24 14:00:00')


tasks.display_tasks()
print("\n")     # for readability

tasks.remove_task('second', '2022-05-24 13:00:00')

tasks.display_tasks()
print("\n")     # for readability

tasks = Tasks('meeting', '2022-05-24 15:00:00')
tasks.display_tasks()
