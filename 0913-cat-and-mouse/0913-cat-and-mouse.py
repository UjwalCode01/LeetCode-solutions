from collections import deque

class Solution(object):
    def catMouseGame(self, graph):
        n = len(graph)
        MOUSE_WIN, CAT_WIN, DRAW = 1, 2, 0

        color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(1, n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        queue = deque()

        for c in range(1, n):
            for turn in (0, 1):
                color[0][c][turn] = MOUSE_WIN
                queue.append((0, c, turn, MOUSE_WIN))

        for m in range(1, n):
            for turn in (0, 1):
                color[m][m][turn] = CAT_WIN
                queue.append((m, m, turn, CAT_WIN))

        def get_parents(m, c, turn):
            prev_turn = 1 - turn
            if prev_turn == 0:
                for prev_m in graph[m]:
                    yield (prev_m, c, prev_turn)
            else:
                for prev_c in graph[c]:
                    if prev_c != 0:
                        yield (m, prev_c, prev_turn)

        while queue:
            m, c, turn, res = queue.popleft()
            if m == 1 and c == 2 and turn == 0:
                return res

            for pm, pc, pt in get_parents(m, c, turn):
                if color[pm][pc][pt] != DRAW:
                    continue

                if (pt == 0 and res == MOUSE_WIN) or (pt == 1 and res == CAT_WIN):
                    color[pm][pc][pt] = res
                    queue.append((pm, pc, pt, res))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        loser_res = CAT_WIN if pt == 0 else MOUSE_WIN
                        color[pm][pc][pt] = loser_res
                        queue.append((pm, pc, pt, loser_res))

        return color[1][2][0]