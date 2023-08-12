

def check_sheet(A, B, X):
    
    print("\n------------------")
    # シートAとシートBの黒いマスの位置を特定する
    black_cells_A = []
    black_cells_B = []

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '#':
                black_cells_A.append((i, j))

    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == '#':
                black_cells_B.append((i, j))

    # シートCの中でシートAとシートBの黒いマスを含む可能性のある領域を切り出す
    min_i = min(min(cell[0] for cell in black_cells_A), min(cell[0] for cell in black_cells_B))
    max_i = max(max(cell[0] for cell in black_cells_A), max(cell[0] for cell in black_cells_B))
    min_j = min(min(cell[1] for cell in black_cells_A), min(cell[1] for cell in black_cells_B))
    max_j = max(max(cell[1] for cell in black_cells_A), max(cell[1] for cell in black_cells_B))

    region = []

    for i in range(min_i, max_i + 1):
        row = ''
        for j in range(min_j, max_j + 1):
            if any(cell == (i, j) for cell in black_cells_A) or any(cell == (i, j) for cell in black_cells_B):
                row += '#'
            else:
                row += '.'

        region.append(row)
    
    for aa in region:
        print(aa)


    # 切り出された領域内の各マスを調べ、シートAとシートBの黒いマスが重なっているかを確認する
    for i in range(len(region)):
        for j in range(len(region[0])):
            if (region[i][j] == '#' and X[i][j] == '.') or (region[i][j] == '.' and X[i][j] == '#'):
                return 'No'

    return 'Yes'


Ha, Wa = map(int, input().split())
A = []
for _ in range(Ha):
    A.append(input())

Hb, Wb = map(int, input().split())
B = []
for _ in range(Hb):
    B.append(input())

Hx, Wx = map(int, input().split())
X = []
for _ in range(Hx):
    X.append(input())

print(check_sheet(A, B, X))  # 出力: Yes







