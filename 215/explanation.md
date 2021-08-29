# 215 Beginner Contest

## B
```math
2^k \le N
```
となる最大の整数kを求める。

自分の回答
```python
import numpy as np
N = int(input())
k = int(np.log2(N))
```
だが、これはWAとなった。
特に$N=2^59-1$で精度不足となるなるようだ。