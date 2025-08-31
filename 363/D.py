def is_palindrome(n: int) -> bool:
  """
  与えられた整数nが10進表記で回文かどうかを判定します。

  Args:
    n (int): 判定対象の整数

  Returns:
    bool: nが回文数の場合はTrue、そうでない場合はFalse
  """
  if n < 0:
    return False

  # 文字列に変換
  n_str = str(n)

  # 先頭と末尾の文字を比較
  for i in range(len(n_str) // 2):
    if n_str[i] != n_str[-(i + 1)]:
      return False

  return True

def find_nth_palindrome(n: int) -> int:
  """
  小さい方からN番目の回文数を求めます。

  Args:
    n (int): N番目の回文数を求める

  Returns:
    int: N番目の回文数
  """
  if n <= 0:
    raise ValueError("n must be a positive integer")

  # 1桁目の回文数から探索
  i = 1
  palindrome = i
  while palindrome < n:
    i += 1
    palindrome = i * i

  # 2桁目の回文数から探索
  if palindrome == n:
    return palindrome

  i = 10
  while palindrome < n:
    start = 10 * (i - 1)
    end = start + 9
    for num in range(start, end + 1):
      if is_palindrome(num):
        palindrome = num
        break

    if palindrome == n:
      return palindrome

    i += 1

# 例
n = 3
nth_palindrome = find_nth_palindrome(n)
print(f"{n}番目の回文数は {nth_palindrome} です。")