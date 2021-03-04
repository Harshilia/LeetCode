import collections


class Solution:
    ## Iterative approach ##

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        q = collections.deque([(sr, sc)])
        start_pixel = image[sr][sc]
        image[sr][sc] = newColor
        length, width = len(image), len(image[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if start_pixel != newColor:
            while q:
                i, j = q.popleft()
                image[i][j] = newColor

                for left, right in directions:
                    row, column = i + left, j + right
                    if 0 <= row < length and 0 <= column < width and image[row][column] == start_pixel:
                        q.append((row, column))  # q.appendleft() for stack

        return image

    ## Recursive approach ##

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        start_pixel = image[sr][sc]
        length, width = len(image), len(image[0])

        if start_pixel == newColor:
            return image

        def helper(row, column):

            if not (0 <= row < length and 0 <= column < width):
                return
            if image[row][column] == newColor or image[row][column] != start_pixel:
                return

            image[row][column] = newColor

            helper(row + 1, column)
            helper(row - 1, column)
            helper(row, column + 1)
            helper(row, column - 1)

        helper(sr, sc)

        return image
