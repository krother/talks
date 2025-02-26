from __future__ import annotations

from typing import Callable

from composite_pydantic import TreeNode


class QuestionProcessor:

    def __init__(self, tree: TreeNode, action: Callable):
        self.tree = tree
        self.action = action

    def process(self):
        self.action(self.tree)


def traverse(node: TreeNode):
    print(node.get_children())


def play(node: TreeNode):
    while isinstance(node, TreeNode):
        print(node.text)
        answer = input("\nyes or no: ").lower()[0]
        node = node.yes if answer == "y" else node.no
    print("\nit is:", node.text)


if __name__ == "__main__":
    json_data = open("mini_questions.json").read()
    tree = TreeNode.model_validate_json(json_data)

    p = QuestionProcessor(tree=tree, action=traverse)
    p.process()
