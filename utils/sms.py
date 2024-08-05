from unisdk.sms import UniSMS
from unisdk.exception import UniException

# 初始化
client = UniSMS("kmvMRKwAoquQ84EtDHcadcKKeNCAfV2fBiJZ6m8JktvpN9hXM") # 若使用简易验签模式仅传入第一个参数即可

try:
  # 发送短信
  res = client.send({
    "to": "18523820295",
    "signature": "UniSMS",
    "templateId": "pub_verif_short",
    "templateData": {
      "code": 7777
    }
  })
  print(res.data)
except UniException as e:
  print(e)