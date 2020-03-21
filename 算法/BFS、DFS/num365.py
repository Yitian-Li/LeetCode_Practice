class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        have_tried = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                # print("succes: ", remain_x, remain_y)
                return True
            if (remain_x, remain_y) in have_tried:
                continue
            have_tried.add((remain_x, remain_y))
            stack.append((x, remain_y))
            stack.append((remain_x, y))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            # y倒向x
            stack.append((remain_x + min(x-remain_x, remain_y), remain_y - min(x-remain_x, remain_y)))
            # x倒向y
            stack.append((remain_x - min(y-remain_y, remain_x), remain_y + min(y-remain_y, remain_x)))
        return False

