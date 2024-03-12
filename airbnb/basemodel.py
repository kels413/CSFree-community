from uuid import uuid4
from datetime import datetime

import time

class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        # print("from init method, created_at:", type(self.created_at))
        # print("from init method, updated_at", type(self.updated_at))

    #   __str__: should print: [<class name>] (<self.id>) <self.__dict__>

    def __str__(self):

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    # public instance method.
    def save(self):
        self.updated_at = datetime.now()

    # just a part of serilization

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        # print("from to_dict method, created_at:", type(obj_dict['created_at']))
        # print("from to_dict method, updated_at", type(obj_dict['updated_at']))
        return obj_dict



model_base = BaseModel()
# print(model_base)/
# print("dictionary representaion")
# print(model_base.to_dict())
#
# print("model base")
# print(model_base)
# print("after todict",type(model_base.created_at))
# print("after todic:",type(model_base.updated_at))

print(model_base.id)
print(model_base.created_at)
print(model_base.updated_at)
