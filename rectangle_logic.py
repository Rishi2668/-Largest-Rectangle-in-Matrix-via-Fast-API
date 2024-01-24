from typing import List

def largest_rectangle(matrix: List[List[int]]) -> tuple:
    # if not matrix[0]:
        # return 0, 0

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    result_number = None

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != -1:  
                number = matrix[row][col]
                length, breadth = 0, 0

                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()

                    if 0 <= r < rows and 0 <= c < cols and matrix[r][c] == number: 
                        matrix[r][c] = -1
                        length += 1

                        # Check if a rectangle can be formed
                        breadth = 1
                        while c + breadth < cols and matrix[r][c + breadth] == number:
                            matrix[r][c + breadth] = -9
                            breadth += 1

                        area = length * breadth

                        if area > max_area and length != breadth:
                            max_area = area
                            result_number = number

                        # Add the next row for the current length
                        stack.append((r + 1, c))  

                # Check if a rectangle can be formed in the next column
                breadth = 1
                while col + breadth < cols and matrix[row][col + breadth] == number:
                    matrix[row][col + breadth] = -9
                    breadth += 1

                area = length * breadth
                #checking the codintion length!= breadth 
                
                if area > max_area and length != breadth:
                    max_area = area
                    result_number = number
                
    return result_number, max_area






# # Example Usage
# matrix = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]

# output is (1,20)

