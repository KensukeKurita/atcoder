# ABC226

## B
重複しないベクトルの数え上げの問題。\
文字列なら、set([str1, str2, str3.])のようにすればよい。\
しかし、set([list1, list2, list3,])はできない。
```python
>>> set([[1,2], [1,2], [2,1]])
raceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
となる。つまり、「unhashableな何か」は、setには入れられないということ。\
辞書のキーにも、unhashbleな何かを使うことはできない。\

書き換えられないもの(immutable)は、hashableなので、setに使える。\
immutableでベクトルっぽいもの？　→　tuple !!!

```python
>>> set([tuple([1,2]), tuple([2,1]), tuple([1,2])])
set([(1, 2), (2, 1)])
```

基本的に、ベクトルを書き換えないなら、タプルを使ったほうがいいかも？