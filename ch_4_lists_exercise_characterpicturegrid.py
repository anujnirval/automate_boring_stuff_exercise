grid = [['.','.','.','.','.','.'],['.','o','o','.','.','.'],['o','o','o','o','.','.'],['o','o','o','o','o','.'],['.','o','o','o','o','o'],['o','o','o','o','o','.'],['o','o','o','o','.','.'],['.','o','o','.','.','.'],['.','.','.','.','.','.']]

for i in range(6):
    for l in range(len(grid)):
        print(grid[l][i],end='')
    print('\n')
