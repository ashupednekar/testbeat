from celery import shared_task


@shared_task
def test1():
    print('test1 is triggered...')


@shared_task
def test2():
    print('test2 is triggered...')
