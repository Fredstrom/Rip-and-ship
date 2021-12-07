from abc import ABC


class Result(list):
    def first(self):
        return self[0] if len(self) > 0 else None

    def last(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, **data):
        super().__init__()

        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def save(self):
        if not self._id:
            del self.__dict__['_id']
            self.collection.insert_one(self.__dict__)
        else:
            self.collection.replace_one({'_id': self._id}, self.__dict__)

    @classmethod
    def get_all(cls):
        return [cls(**item) for item in cls.collection.find()]

    @classmethod
    def find(cls, **kwargs):
        return Result(cls(**item) for item in cls.collection.find(kwargs))

