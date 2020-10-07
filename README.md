# nicematrix
My solution to problem 1442B in codeforces (nice matrix)

link: https://codeforces.com/problemset/problem/1422/B

1. I took points which had to match 3 other corresponding points and sorted them in an array.
2. I then took the median of these points and summed the diffrences of the three other points, which added to my count
3. I then solved for the middle horizontal and vertical lines (if exist). These points only have one corresponding point, so I just took the diffrence between the points and added it to my count
4. print count, which is the answer
