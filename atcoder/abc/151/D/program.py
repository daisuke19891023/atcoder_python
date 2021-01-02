import queue
# import sys
# input = sys.stdin.readline

vx = [0,1,0,-1];
vy = [1,0,-1,0];
q = queue.Queue()
 
h, w = map(int, input().split())
# print(hw)
# h = int(hw[0]);
# w = int(hw[1]);
s_s = [h-1, 0]
sy = int(s_s[0]);
sx = int(s_s[1]);
s_g = [0, w-1]
gy = int(s_g[0]);
gx = int(s_g[1]);
s = [ [0]*w for i in range(h)];
for i in range(h) :
	si = input();
	for j in range(w) :
		s[i][j] = si[j];
 
cont = 1;
q_a = [0]*2;
q_a[0] = sy;
q_a[1] = sx;
q.put(q_a);
s[sy][sx] = 0;
while not q.empty() :
	q_a = q.get();
	for i in range(4):
		ny = q_a[0] + x[i];
		nx = q_a[1] + vx[i];
		if s[ny][nx] == '.' :
			s[ny][nx] = s[q_a[0]][q_a[1]] + 1;
			q_b = [0]*2;
			q_b[0] = ny;
			q_b[1] = nx;
			q.put(q_b);
 
print(s[gy][gx]);