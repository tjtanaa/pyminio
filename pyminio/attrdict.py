"""https://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute"""
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self