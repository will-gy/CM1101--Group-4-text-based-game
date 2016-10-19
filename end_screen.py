import time
def victory():
    victory_message =  \
    """
     __     __           ______                              _ _
     \ \   / /          |  ____|                            | | |
      \ \_/ /__  _   _  | |__   ___  ___ __ _ _ __   ___  __| | |
       \   / _ \| | | | |  __| / __|/ __/ _` | '_ \ / _ \/ _` | |
        | | (_) | |_| | | |____\__ \ (_| (_| | |_) |  __/ (_| |_|
        |_|\___/ \__,_| |______|___/\___\__,_| .__/ \___|\__,_(_)
                                             | |
                                             |_|
        """

    name_list = ["Charly Whitlow", "William Yelverton", "Peter Ghawi", "Karan Juj", "Charlie Read", "Caleb Stride", "Markuss Baumgarts", "Sara Aldossary"]

    v_split = victory_message.split('\n')
    for x in v_split:
        print(x)
        time.sleep(0.3)
    print("Prison break was developed by:")
    for name in name_list:
        print()
        print(name)
        time.sleep(1)

    time.sleep(2)
    print()
    print("Thanks for playing!")
    exit()