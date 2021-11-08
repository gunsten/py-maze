import random
from linkedlist import LinkedList as LinkedList


class Maze:
    def __init__(self, w, h, paths):
        self.maze = [
            [0 for x in range(0, w)] for y in range(0, h)]
        for ((i, j), (i_, j_)) in paths:
            if j == j_:
                self.maze[j][i] ^= 1
            elif i == i_:
                self.maze[j][i] ^= 2
        self.w = w
        self.h = h

    def get_walls(self, coord):
        (i, j) = coord
        return self.maze[j][i]

    def reachable(self, coord):
        maze, (i, j) = self.maze, coord
        reachable = list()
        if self.get_walls(coord) % 2 == 1:
            reachable.append((i + 1, j))
        if self.get_walls(coord) >= 2:
            reachable.append((i, j + 1))
        if i > 0 and self.get_walls((i - 1, j)) % 2 == 1:
            reachable.append((i - 1, j))
        if j > 0 and self.get_walls((i, j - 1)) >= 2:
            reachable.append((i, j - 1))
        return reachable

    def as_string(self):
        maze, w, h = self.maze, self.w, self.h
        lines = ["#" * (2 * w + 1)]
        for i in range(0, h):
            upper = "#" + "".join(["  " if maze[i][j] % 2 == 1 else " #" for j in range(0, w)])
            lower = "#" + "".join([" #" if maze[i][j] > 1 else "##" for j in range(0, w)])
            lines.append(upper)
            lines.append(lower)

        return "\n".join(lines)

    def __repr__(self):
        return self.as_string()

    @staticmethod
    def generate(w, h):
        candidates = [(n % w, n // h) for n in range(0, w * h)]
        c_groups, g_cells, paths = dict(), dict(), list()

        # Group all cells. Keep both cell -> group and group -> cells in memory
        for (i, j) in candidates:
            c_groups[(i, j)] = j * h + i
            g_cells[j * h + i] = {(i, j)}

        while len(g_cells) > 1:
            index = random.randint(0, len(candidates) - 1)
            (i, j) = c = candidates[index]
            group = c_groups[(i, j)]
            # list possible path from cell (i, j)
            choices = list()
            if i - 1 >= 0 and c_groups[(i - 1, j)] != group:
                choices.append((i - 1, j))
            if i + 1 < w and c_groups[(i + 1, j)] != group:
                choices.append((i + 1, j))
            if j - 1 >= 0 and c_groups[(i, j - 1)] != group:
                choices.append((i, j - 1))
            if j + 1 < h and c_groups[(i, j + 1)] != group:
                choices.append((i, j + 1))

            if len(choices) == 0:
                candidates.pop(index)
                continue

            c_ = random.choice(choices)

            # remember chosen path and merge groups
            if c > c_:
                paths.append((c_, c))
            else:
                paths.append((c, c_))
            old_group = c_groups[c_]
            for cell in g_cells[old_group]:
                c_groups[cell] = group
            g_cells[group].update(g_cells[old_group])
            g_cells.pop(old_group)

        return Maze(w, h, paths)


class Solver:
    @staticmethod
    def solve(maze, start, end):
        print(maze)
        paths = [LinkedList(start)]
        while True:
            current = paths.pop(0)
            visited = None
            if current.has_tail:
                visited = current.tail.head

            reachable = maze.reachable(current.head)
            if reachable:
                for step in maze.reachable(current.head):
                    if step == end:
                        res = LinkedList.cons(step, current).to_list()
                        res.reverse()
                        return res
                    if step == visited:
                        continue
                    paths.append(LinkedList.cons(step, current))
