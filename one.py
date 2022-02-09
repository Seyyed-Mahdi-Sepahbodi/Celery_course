from celery import Celery
from time import sleep

# app = Celery('one', broker='amqp://localhost')

app = Celery('one')

# app.conf.timezone = 'asia/tehran'

# app.conf.update(
#     enable_utc= True,
#     timezone= 'asia/tehran',
#     task_serializer= 'json',
#     result_serializer= 'json',
#     borker_url= 'amqp://localhost',
#     result_backend= 'rpc://',
# )

app.config_from_object('conf')

@app.task
def add(x, y):
    sleep(5)
    return x + y


# signature = add.signature((3, 4), countdown=300)
# signature = add.signature((3, 4))
# # print(signature)
# # print(signature.options)
# # print(signature.args)

# signature.delay()


# ------- 
# partial
# partial = add.signature((3, ))
# partial.delay(4)


# -------
# immutabliity
@app.task
def sub(x, y):
    return x - y

# result = add.apply_async((3, 4), link=sub.signature((5, )))
result = add.apply_async((3, 4), link=sub.signature((5, 8), immtable=True))
result = add.apply_async((3, 4), link=sub.si(5, 8))