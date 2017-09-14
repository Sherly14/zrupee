import uuid
import hashlib
import random


def generate_password():
    generated_uuid = str(uuid.uuid4())
    salt = random.randint(111111, 999999)
    password_hash = '%s-%s' % (salt, generated_uuid)
    password = hashlib.md5(password_hash).hexdigest()

    return password
