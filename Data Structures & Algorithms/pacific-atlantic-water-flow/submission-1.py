from collections import deque

class Solution:
    def getBorderCells(self, ocean: str, cells: List[List[int]]):
        num_rows = len(cells)
        num_cols = len(cells[0])
        if ocean == "pac":
            border_cells = set([(0,i) for i in range(num_cols)])
            for i in range(1, num_rows):
                border_cells.add((i, 0))
            return border_cells
        else:
            border_cells = set([(num_rows-1,i) for i in range(num_cols)])
            for i in range(0, num_rows - 1):
                border_cells.add((i, num_cols-1))
            return border_cells

    def get_neighbors(self, cell: tuple, cells: List[List[int]]):
        num_rows = len(cells)
        num_cols = len(cells[0])
        r, c = cell[0], cell[1]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        neighbors = []

        for dr, dc in dirs:
            if r + dr >= 0 and r + dr < num_rows and c + dc >= 0 and c + dc < num_cols:
                neighbors.append((r+dr, c+dc))
        return neighbors
        

    def bfs(self, start: tuple, visited: set, cells: List[List[int]]):
        visited.add(start)
        dq = deque([start])

        while dq:
            current_node = dq.popleft()
            neighbors = self.get_neighbors(current_node, cells)

            for neighbor in neighbors:
                cr, cc = current_node[0], current_node[1]
                nr, nc = neighbor[0], neighbor[1]
                
                if neighbor not in visited and cells[nr][nc] >= cells[cr][cc]:
                    visited.add(neighbor)
                    dq.append(neighbor)


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # explore border cells -> check all pacific and atlantic, find intersection
        visited_p, visited_a = set(), set()
        pac_border_cells = self.getBorderCells("pac", heights)
        atl_border_cells = self.getBorderCells("atl", heights)

        # build reachable cells for each ocean
        for pbcell in pac_border_cells:
            self.bfs(pbcell, visited_p, heights)
        for atcell in atl_border_cells:
            self.bfs(atcell, visited_a, heights)
        
        # return union of the reachable cells in both oceans
        return [coord for coord in visited_p if coord in visited_a]
        

