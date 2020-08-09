from threading import Thread
import time
import utils
import pandas as pd

class WindowInfoGetter:
    """
    Class that give the active information of the running app.
    """

    def __init__(self):
        self.stopped  = False
        self.df_info  = pd.DataFrame()
        self.csv_file = "saved_snips_for_cliks/WindowInfo.csv"

    def start(self):
        Thread(target=self.get, args=(), daemon=True).start()
        return self

    def get(self):
        while not self.stopped:
            # st_time = time.time()
            info = utils.getActiveWindow()
            active_software_name, active_window_name, active_window_bbox = info
            self.df_info = self.df_info.append(
                                                {
                                                "time":time.time(),
                                                "active_software_name": active_software_name,
                                                "active_window_name": active_window_name,
                                                "active_window_bbox": active_window_bbox
                                                },ignore_index=True)

            # print(self.df_info.shape)
            # time.sleep(0.01)

            # if len(self.info_list)%200:
                # print("grab time taken: ", time.time()-st_time)

    def stop(self):
        print("stopping")
        self.stopped = True
        print("saving")
        self.df_info.to_csv(self.csv_file, index=False)

if __name__ == "__main__":
    windowInfoGetter = WindowInfoGetter()
    windowInfoGetter.start()
    time.sleep(4)
    windowInfoGetter.stop()
