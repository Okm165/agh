from math import sqrt

def dist(pt1:tuple, pt2:tuple)->float:
    return sqrt(
        (pt1[0]-pt2[0])**2 +
        (pt1[1]-pt2[1])**2 +
        (pt1[2]-pt2[2])**2
    )

def upd_avg(old_avg: float, cnt:int, elem:float)->float:
    if not cnt: return elem
    elif not elem: return old_avg
    return old_avg + ((old_avg+elem)*cnt - old_avg*(cnt+1)) / (cnt*(cnt+1))

def search(table:list, r:float, cnt:int=0, r_cnt:int=0,
        x_avg:float=0, y_avg:float=0, z_avg:float=0)->bool:

    if r_cnt < 3: return False
    elif dist((0,0,0), (x_avg,y_avg,z_avg)) < r: return True
    elif cnt >= len(table): return False

    return (
        search(table, r, cnt+1, r_cnt, x_avg, y_avg, z_avg) or
        search(table, r, cnt+1, r_cnt+1,
            upd_avg(x_avg,cnt,table[cnt][0]),
            upd_avg(y_avg,cnt,table[cnt][1]),
            upd_avg(z_avg,cnt,table[cnt][2])
        )
    )