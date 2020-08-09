import pandas as pd
import numpy as np
from utils import *

def add_windoInfo_and_save_image_from_timer_csv():
    windowInfo_timePreviousSec = 0.05
    commands_csv_file = "saved_snips_for_cliks/commands.csv"
    window_info_file = "saved_snips_for_cliks/WindowInfo.csv"
    df_info = pd.read_csv(window_info_file)
    df_commands = pd.read_csv(commands_csv_file)
    info_list = np.array([ [row.time, (row.active_software_name,row.active_window_name,row.active_window_bbox)]  for index, row in df_info.iterrows()])
    arr_active_software_name,arr_active_window_bbox,arr_active_window_name = [],[],[],[]
    for index, row in df_commands.iterrows():
        print(index)
        active_software_name, active_window_name, active_window_bbox = info
        arr_active_software_name.append(active_software_name)
        arr_active_window_name.append(active_window_name)
        arr_active_window_bbox.append(active_window_bbox)

    # df_commands["img_path"] = arr_img_path
    df_commands["active_software_name"] = arr_active_software_name
    df_commands["active_window_name"] = arr_active_window_name
    df_commands["active_window_bbox"] = arr_active_window_bbox
    df_commands.to_csv("saved_snips_for_cliks/combined_commands.csv")

if __name__ == "__main__":
    add_windoInfo_and_save_image_from_timer_csv()
