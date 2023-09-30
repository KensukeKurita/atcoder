# １つのポリオミノの位置は１６通り（ただし、はみ出すことは考慮してない）。回転が４通り。
# ポリオミノが３つあるので、
import itertools

class Poly:
    def __init__(self, input_str: list):
        if len(input_str) == 4:
            self.block = self._get_block(input_str)
            self.init_block = self.block
        else:
            print("Error")
    
    @staticmethod
    def _get_block(input_str: list) -> list:
        tmp_d = []
        for i, line in enumerate(input_str):
            for j in range(4):
                if line[j] == "#":
                  tmp_d.append((j, 3-i))
        return tmp_d

    def _rotate(self, ang: int):
        if ang not in [0, 90, 180, 270]:
            raise RuntimeError("rotation error")
        if len(self.block) == 0:
            raise RuntimeError("rotation Error")
        
        new_block = []
        for x, y in self.block:
            if ang == 270:
                new_block.append((3-y, x))
            elif ang == 180:
                new_block.append((3-x, 3-y))
            elif ang == 90:
                new_block.append((y, 3-x))
            elif ang == 0:
                new_block.append((x, y))

        if len(new_block) == 0:
            raise RuntimeError("rotation Error")

        self.block = new_block

    def effective_translate(self, tx, ty, ang) -> bool:
        self.block = self.init_block
        self._rotate(ang * 90)

        if abs(tx) > 3 or abs(ty) > 3:
            raise RuntimeError("translate Error")
        
        new_block = []
        for x, y in self.block:
            new_x = x + tx
            new_y = y + ty
            if (0 <= new_x <= 3) and (0 <= new_y <= 3):
                new_block.append((x+tx, y+ty))
            else:
                return False
        
        self.block = new_block
        return True



def main():

    poly1 = []
    poly1.append(input())
    poly1.append(input())
    poly1.append(input())
    poly1.append(input())
    Poly1 = Poly(input_str=poly1)

    poly2 = []
    poly2.append(input())
    poly2.append(input())
    poly2.append(input())
    poly2.append(input())
    Poly2 = Poly(input_str=poly2)

    poly3 = []
    poly3.append(input())
    poly3.append(input())
    poly3.append(input())
    poly3.append(input())
    Poly3 = Poly(input_str=poly3)

    # ブロックの数は必ず１６。そうでないものは外す。
    if (len(Poly1.block) + len(Poly2.block) + len(Poly3.block)) != 16:
        print("No")
        return

    for ang1 in range(3):
        for ang2 in range(3):
            for ang3 in range(3):

                for tx1, ty1 in itertools.product(range(-3, 4), repeat=2):
                    if not Poly1.effective_translate(tx1, ty1, ang1):
                        continue
                    for tx2, ty2 in itertools.product(range(-3, 4), repeat=2):
                        if not Poly2.effective_translate(tx2, ty2, ang2):
                            continue
                        for tx3, ty3 in itertools.product(range(-3, 4), repeat=2):
                            if not Poly3.effective_translate(tx3, ty3, ang3):
                                continue
                            
                            fla = check(Poly1, Poly2, Poly3)
                            if fla:
                                print("Yes")
                                return
    print("No")
    return



def check(p1: Poly, p2: Poly, p3: Poly) -> bool:

    result = set()
    for p in p1.block:
        if p in result:
            return False
        else:
            result.add(p)
    
    for p in p2.block:
        if p in result:
            return False
        else:
            result.add(p)


    for p in p3.block:
        if p in result:
            return False
        else:
            result.add(p)

    if len(result) == 16:
        return True

if __name__ == "__main__":
    main()
