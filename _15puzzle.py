import sys
import time as t
from A_star import A_star
from DFS import DFS
from BFS import BFS
from Puzzle import Puzzle

#python main.py bfs ludr plik.txt out1.txt out2.txt
inf = open(sys.argv[3])
input_lines = inf.readlines()
inf.close()

puzzlemap = []

for line in input_lines:
    tmp = []
    for n in line.split():
        tmp.append(int(n))
    puzzlemap.append(tmp)

print(puzzlemap)

szer, wys = puzzlemap.pop(0)


if sys.argv[1] == "dfs":
    puzzle = Puzzle(szer, wys, puzzlemap)
    dfs = DFS(puzzle, sys.argv[2])
    wynik, gl_rek, stany_odw, stany_przet, czas = dfs.solve()
elif sys.argv[1] == "bfs":
    queue = []
    puzzle = Puzzle(4, 4, puzzlemap)
    queue.append(puzzle.grid)
    bfs = BFS(puzzle, sys.argv[2])
    czas, stany_przet, stany_odw, wynik, gl_rek = bfs.solve(queue, puzzlemap)
else:
    puzzle = Puzzle(szer, wys, puzzlemap)
    astar = A_star(puzzle, sys.argv[2])
    start = t.time()
    wynik, gl_rek, stany_odw, stany_przet, czas = astar.solve()


dl_rozw_str = "-1"
fout1 = open(sys.argv[4],'w+')
if wynik != -1:
    dl_rozw = len(wynik)
    dl_rozw_str = str(dl_rozw)
    fout1.write(dl_rozw_str + '\n')
fout1.write(str(wynik))
fout1.close()

stany_odw_str = str(stany_odw)
stany_przet_str = str(stany_przet)
gl_rek_str = str(gl_rek)

fout2 = open(sys.argv[5], 'w+')
fout2.write(dl_rozw_str + '\n')
fout2.write(stany_odw_str + '\n')
fout2.write(stany_przet_str + '\n')
fout2.write(gl_rek_str + '\n')
fout2.write('%.3f' % czas + '\n')
fout2.close()