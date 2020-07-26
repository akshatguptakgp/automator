def maxPoints(points):
        n=len(points)

        # upto two points all points will be part of the line
        if n<3:
            return n

        max_val=0

        # looping for each point

        for i in points:
            # Creating a dictionary for every new
            # point to save memory
            d = {}
            dups = 0
            cur_max = 0

            # pairing with all other points
            for j in points:
                if i!=j:
                    if j[0]==i[0]: #vertical line
                        # slope='inf'
                        continue
                    else:
                        slope=float(j[1]-i[1])/float(j[0]-i[0])

                    # Increasing the frequency of slope and
                    # updating cur_max for current point(i)
                    d[slope] = d.get(slope,0)+1
                    cur_max=max(cur_max, d[slope])
                    if d[slope] == 8:
                        print(slope)

                # if both points are equal same increase
                # duplicates count.
                # Please note that this will also increment
                # when we map it with itself.
                # we still do it because we will not have to
                # add the extra one at the end.
                else:
                    dups+=1

            # max_val=max(max_val, cur_max+dups)
            if max_val < cur_max+dups:
                max_val = cur_max+dups
                # print(d)

        return max_val

# Driver code
# points = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("saved_snips_for_cliks/timer_video.csv")
points = []
for i in range(df.shape[0]):
    points.append((df.time[i],df.frame_no[i]/55.0))
print(maxPoints(points))
