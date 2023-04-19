from celery import Celery

from src.configs.environment import settings


celery_app = Celery("tasks", broker=settings.CELERY_BROKER_URL)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        10.0,
        update_all_products_info.s("IVAN!"),
        name="print every 10 secs"
    )


@celery_app.task
def update_all_products_info(name):
    print("=========================")
    print(f"IM A PERIODIC TASK BOY! {name}")
    print("=========================")
