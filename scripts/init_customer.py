# 启动django
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE","order.settings")

django.setup()



from web import models
from utils.encrypt import md5

# 创建级别
#level_object = models.Level.objects.create(title="VIP",percent=90)

models.Customer.objects.create(
    username='xinyang2',
    password=md5("xinyang2"),
    mobile="15803843063",
    level_id=1,
    creator_id=1
)

