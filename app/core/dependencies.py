from app.repositories.tasks import TaskRepository


def get_tasks_repository():
    return TaskRepository()
