"""
metaclass from https://refactoring.guru/design-patterns/singleton/python/example
"""

from composite_pydantic import TreeNode


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class TreeLoader(metaclass=SingletonMeta):

    def __init__(self):
        print("Daten werden geladen")
        json_data = open("mini_questions.json").read()
        self.tree = TreeNode.model_validate_json(json_data)


if __name__ == "__main__":

    s1 = TreeLoader()
    s2 = TreeLoader()

    print(s1 is s2)
