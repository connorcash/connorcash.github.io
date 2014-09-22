#!/usr/bin/env python

class Connor(object):
    def __init__(self, lastname, interests):
        self.lastname = lastname
        self.interests = interests

    def __repr__(self):
        rep = "Hi, I'm {} {}.\n".format(self.__class__.__name__,
                                        self.lastname)
        rep += "I enjoy " + ", ".join(self.interests) + "."
        return rep


if __name__ == "__main__":
    i = Connor("Cash", interests=["Python", "DotA 2"])
    print(i)
