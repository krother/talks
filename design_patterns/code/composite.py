from __future__ import annotations
from abc import ABC, abstractmethod


class TreeComponent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def get_children(self) -> list[str]:
        pass


class InternalNode(TreeComponent):
    """Internal Node in a question-answer tree"""

    def __init__(self, text: str, yes: TreeComponent, no: TreeComponent):
        super().__init__(text)
        self.yes = yes
        self.no = no

    def get_children(self) -> list[str]:
        return self.yes.get_children() + self.no.get_children()


class ChildNode(TreeComponent):

    def get_children(self) -> list[str]:
        return [self.text]


tree = InternalNode(
    text="kann es fliegen?",
    yes=ChildNode(text="Schwalbe"),
    no=InternalNode(
        text="hat es einen Rüssel?",
        yes=ChildNode(text="Elefant"),
        no=ChildNode(text="Python"),
    ),
)

print(tree.get_children())
