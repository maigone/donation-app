# Problem A: Neko Finds Grapes

https://codeforces.com/contest/1152/problem/A

## Task

```text
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
On a random day, Neko found 𝑛 treasure chests and 𝑚 keys. The 𝑖-th chest has an integer 𝑎𝑖 written on it and the 𝑗-th key has an integer 𝑏𝑗 on it. Neko knows those chests contain the powerful mysterious green Grapes, thus Neko wants to open as many treasure chests as possible.

The 𝑗-th key can be used to unlock the 𝑖-th chest if and only if the sum of the key number and the chest number is an odd number. Formally, 𝑎𝑖+𝑏𝑗≡1(mod2). One key can be used to open at most one chest, and one chest can be opened at most once.

Find the maximum number of chests Neko can open.

Input
The first line contains integers 𝑛 and 𝑚 (1≤𝑛,𝑚≤105) — the number of chests and the number of keys.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤109) — the numbers written on the treasure chests.

The third line contains 𝑚 integers 𝑏1,𝑏2,…,𝑏𝑚 (1≤𝑏𝑖≤109) — the numbers written on the keys.

Output
Print the maximum number of chests you can open.

Examples
inputCopy
5 4
9 14 6 2 11
8 4 7 20
outputCopy
3
inputCopy
5 1
2 4 6 8 10
5
outputCopy
1
inputCopy
1 4
10
20 30 40 50
outputCopy
0
Note
In the first example, one possible way to unlock 3 chests is as follows:

Use first key to unlock the fifth chest,
Use third key to unlock the second chest,
Use fourth key to unlock the first chest.
In the second example, you can use the only key to unlock any single chest (note that one key can't be used twice).

In the third example, no key can unlock the given chest.
```

## Solution

Blah....Blah ...

### Python

Reference: [Code](/Problem-A/floor.py)

### C++
