from __future__ import annotations
from pydantic import BaseModel


class TreeNode(BaseModel):

    text: str
    yes: TreeNode | ChildNode
    no: TreeNode | ChildNode

    def get_children(self) -> list[str]:
        return self.yes.get_children() + self.no.get_children()


class ChildNode(BaseModel):

    text: str

    def get_children(self) -> list[str]:
        return [self.text]


if __name__ == "__main__":
    json_data = open("questions.json").read()
    tree = TreeNode.model_validate_json(json_data)
    print(tree.get_children())
