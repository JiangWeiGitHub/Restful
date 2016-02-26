from celery import task,platforms

platforms.C_FORCE_ROOT = True

@task()
def justtry():
    print 111111111111111111111111111111111111111
    return 9