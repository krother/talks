from abc import ABC, abstractmethod

from composite_pydantic import TreeNode


class TreeAction(ABC):

    dummy: str

    @abstractmethod
    def execute(self, node: TreeNode):
        pass


class QuestionProcessor:

    def __init__(self, tree: TreeNode, action: TreeAction):
        self.tree = tree
        self.action = action

    def process(self):
        self.action.execute(self.tree)


class Traversal(TreeAction):

    def execute(self, node: TreeNode):
        print(node.get_children())


if __name__ == "__main__":
    json_data = open("mini_questions.json").read()
    tree = TreeNode.model_validate_json(json_data)

    p = QuestionProcessor(tree=tree, action=Traversal())
    p.process()
