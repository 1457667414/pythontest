# Name：林
# Time： 2020/11/5 16:31
import hashlib


# 加盐加密
def password_salt(password, x='sifdzmgcxym'):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))
    h.update(x.encode('utf8'))
    return h.hexdigest()
