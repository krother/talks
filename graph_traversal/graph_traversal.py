
from dungeon import DungeonCrawl, Player, UP, DOWN, LEFT, RIGHT
from collections import deque
import arcade


def find_path(start, exit, get_adjacent):
    """Breadth-first graph search algorithm"""
    candidates = [
        (start, [])
    ]
    visited = {start}

    while candidates:
        pos, path = candidates.pop(0)
        if pos == exit:
            return path

        for p, move in get_adjacent(pos):
            if p not in visited:
                candidates.append((p, path[:] + [move]))
                visited.add(p)
        
    raise Exception("No exit found")


class TraversalPlayer(Player):

    path = None

    def find_path(self):
        start = (self.pos, [])
        candidates = deque([start])
        visited = {self.pos}

        while candidates:
            pos, path = candidates.popleft()
            if pos == self.level.exit:
                return path

            for p, move in self.adjacent_positions(pos):
                if p not in visited:
                    candidates.append((p, path[:] + [move]))
                    visited.add(p)
            
        raise Exception("No exit found")


    def find_path(self, start, exit):
        start = (self.pos, [])
        candidates = [start]
        visited = {self.pos}

        while candidates:
            pos, path = candidates.pop(0)
            if pos == self.level.exit:
                return path

            for p, move in self.adjacent_positions(pos):
                if p not in visited:
                    candidates.append((p, path[:] + [move]))
                    visited.add(p)
            
        raise Exception("No exit found")


    def move(self):
        self.path = self.path or find_path(self.pos, self.level.exit, self.adjacent_positions)
        direction = self.path.pop(0)
        super().move(direction)



if __name__ == '__main__':
    dc = DungeonCrawl(TraversalPlayer)
    arcade.run()
