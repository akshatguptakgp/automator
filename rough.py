import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_csv("saved_snips_for_cliks/timer_video.csv")

plt.plot(df.time,df.frame_no)
plt.show()

"""
#find slopes for 5 sec
slope_arr=[]
for i in range(5):
    initial_frame = i*0.2*df.shape[0]
    final_frame = (i+1)*0.2*df.shape[0]
    average_val=0
    for j in range(int(initial_frame),int(final_frame),1):
        average_val += df["time"][j]/(df["frame_no"][j]+1)
    slope_arr.append(average_val/int(final_frame)-int(initial_frame))


print(slope_arr)
print(numpy.median(slope_arr))
"""
