import tkinter as tk
import json
import requests
try:
    from Tkinter import Entry, Frame, Label, StringVar
    from Tkconstants import *
except ImportError:
    from tkinter import Entry, Frame, Label, StringVar
    from tkinter.constants import *


json_data = open('private.json')
private = json.load(json_data)

global hypixelapirequests
username = 0
hypixelapirequests = requests.get(f"https://api.hypixel.net/player?key={private['hypixelKey']}&name={username}")

def swstats(username):
    if hypixelapirequests.status_code == 200:
        hypixeldata = hypixelapirequests.json()

        if hypixeldata["player"] is None:
            print("profile error")

        if len(username) < 3:
            print("profile error")

        if "skywars_experience" in hypixeldata["player"]["stats"]["SkyWars"]:
            swexp = hypixeldata["player"]["stats"]["SkyWars"]["skywars_experience"]
        else:
            swexp = 0
        displayname = hypixeldata["player"]["displayname"]
        if "rank" in hypixeldata["player"] and hypixeldata["player"]["rank"] != "NORMAL":
            rank = hypixeldata["player"]["rank"]
        elif "newPackageRank" in hypixeldata["player"]:
            rank = hypixeldata["player"]["newPackageRank"]
        elif "packageRank" in hypixeldata["player"]:
            rank = hypixeldata["player"]["packageRank"]
        else:
            rank = "NON"
        if rank == "MVP_PLUS":
            rank = "MVP+"
        if rank == "VIP_PLUS":
            rank = "VIP+"

        if "kills" in hypixeldata["player"]["stats"]["SkyWars"]:
            swkills = hypixeldata["player"]["stats"]["SkyWars"]["kills"]
        else:
            swkills = 0
        if "deaths" in hypixeldata["player"]["stats"]["SkyWars"]:
            swdeaths = hypixeldata["player"]["stats"]["SkyWars"]["deaths"]
        else:
            swdeaths = 0
        if "skywars_you_re_a_star" in hypixeldata["player"]["achievements"]:
            swstar = hypixeldata["player"]["achievements"]["skywars_you_re_a_star"]
        else:
            swstar = 0
        if "wins" in hypixeldata["player"]["stats"]["SkyWars"]:
            swwins = hypixeldata["player"]["stats"]["SkyWars"]["wins"]
        else:
            swwins = 0
        if "losses" in hypixeldata["player"]["stats"]["SkyWars"]:
            swlosses = hypixeldata["player"]["stats"]["SkyWars"]["losses"]
        else:
            swlosses = 0
        if "souls" in hypixeldata["player"]["stats"]["SkyWars"]:
            swsouls = hypixeldata["player"]["stats"]["SkyWars"]["souls"]
        else:
            swsouls = 0
        if "shard" in hypixeldata["player"]["stats"]["SkyWars"]:
            swshards = hypixeldata["player"]["stats"]["SkyWars"]["shard"]
        else:
            swshards = 0
        if "coins" in hypixeldata["player"]["stats"]["SkyWars"]:
            swcoins = hypixeldata["player"]["stats"]["SkyWars"]["coins"]
        else:
            swcoins = 0
        if "angel_of_death_level" in hypixeldata["player"]["stats"]["SkyWars"]:
            angelodeath = hypixeldata["player"]["stats"]["SkyWars"]["angel_of_death_level"]
        else:
            angelodeath = 0

        coins_till_next_aodl = 0
        if angelodeath == 0:
            coins_till_next_aodl = 50000 - swcoins
        if angelodeath == 1:
            coins_till_next_aodl = 200000 - swcoins
        if angelodeath == 2:
            coins_till_next_aodl = 500000 - swcoins
        if angelodeath == 3:
            coins_till_next_aodl = 1000000 - swcoins
        if angelodeath == 4:
            coins_till_next_aodl = 2000000 - swcoins
        if angelodeath == 5:
            coins_till_next_aodl = 5000000 - swcoins
        if angelodeath == 6:
            coins_till_next_aodl = 10000000 - swcoins
        if angelodeath == 7:
            coins_till_next_aodl = 15000000 - swcoins
        if angelodeath == 8:
            coins_till_next_aodl = 20000000 - swcoins
        if angelodeath == 9:
            coins_till_next_aodl = 30000000 - swcoins
        if angelodeath == 10:
            coins_till_next_aodl = 40000000 - swcoins
        if angelodeath == 11:
            coins_till_next_aodl = 50000000 - swcoins
        if coins_till_next_aodl <= 0:
            coins_till_next_aodl = 0

        sww_l = round(swwins / swlosses, 2)
        swk_d = round(swkills / swdeaths, 2)

        kills_to_x_k_d = 0
        if swk_d <= 1:
            kills_to_x_k_d = swdeaths - swkills
            k_d_var = "1"
        if 1 <= swk_d:
            kills_to_x_k_d = swdeaths * 2 - swkills
            k_d_var = "2"
        if 2 <= swk_d:
            kills_to_x_k_d = swdeaths * 3 - swkills
            k_d_var = "3"

        wins_to_x_k_d = 0
        if sww_l <= 1:
            wins_to_x_k_d = swlosses - swwins
            w_l_var = "1"
        if 1 <= sww_l:
            wins_to_x_k_d = swlosses * 2 - swwins
            w_l_var = "2"
        if 2 <= sww_l:
            wins_to_x_k_d = swlosses * 3 - swwins
            w_l_var = "3"

        xp_next_star = 0
        if 20 >= swexp >= 0:
            xp_next_star = 20 - swexp
        if 70 >= swexp >= 20:
            xp_next_star = 70 - swexp
        if 150 >= swexp >= 70:
            xp_next_star = 150 - swexp
        if 250 >= swexp >= 150:
            xp_next_star = 250 - swexp
        if 500 >= swexp >= 250:
            xp_next_star = 500 - swexp
        if 1000 >= swexp >= 500:
            xp_next_star = 1000 - swexp
        if 2000 >= swexp >= 1000:
            xp_next_star = 2000 - swexp
        if 3500 >= swexp >= 2000:
            xp_next_star = 3500 - swexp
        if 6000 >= swexp >= 3500:
            xp_next_star = 6000 - swexp
        if 10000 >= swexp >= 6000:
            xp_next_star = 10000 - swexp
        if 15000 >= swexp >= 10000:
            xp_next_star = 15000 - swexp
        if 25000 >= swexp >= 15000:
            xp_next_star = 25000 - swexp
        if 35000 >= swexp >= 25000:
            xp_next_star = 35000 - swexp
    else:
        print("please try again")


def bwstats(username):
    if hypixelapirequests.status_code == 200:
        hypixeldata = hypixelapirequests.json()

        if hypixeldata["player"] is None:
            print("profile error")

        if len(username) < 3:
            print("profile error")

        displayname = hypixeldata["player"]["displayname"]
        if "rank" in hypixeldata["player"] and hypixeldata["player"]["rank"] != "NORMAL":
            rank = hypixeldata["player"]["rank"]
        elif "newPackageRank" in hypixeldata["player"]:
            rank = hypixeldata["player"]["newPackageRank"]
        elif "packageRank" in hypixeldata["player"]:
            rank = hypixeldata["player"]["packageRank"]
        else:
            rank = "NON"
        if rank == "MVP_PLUS":
            rank = "MVP+"
        if rank == "VIP_PLUS":
            rank = "VIP+"

        if "kills_bedwars" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwkills = hypixeldata["player"]["stats"]["Bedwars"]["kills_bedwars"]
        else:
            bwkills = 0
        if "deaths_bedwars" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwdeaths = hypixeldata["player"]["stats"]["Bedwars"]["deaths_bedwars"]
        else:
            bwdeaths = 0
        if "bedwars_level" in hypixeldata["player"]["achievements"]:
            bwlevel = hypixeldata["player"]["achievements"]["bedwars_level"]
        else:
            bwlevel = 0
        if "wins_bedwars" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwwins = hypixeldata["player"]["stats"]["Bedwars"]["wins_bedwars"]
        else:
            bwwins = 0
        if "losses_bedwars" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwlosses = hypixeldata["player"]["stats"]["Bedwars"]["losses_bedwars"]
        else:
            bwlosses = 0
        if "final_kills_bedwars" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwfk = hypixeldata["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
        else:
            bwfk = 0
        if "final_deaths_bedwars" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwfd = hypixeldata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
        else:
            bwfd = 0
        if "coins" in hypixeldata["player"]["stats"]["Bedwars"]:
            bwcoins = hypixeldata["player"]["stats"]["Bedwars"]["coins"]
        else:
            bwcoins = 0

        bwfkdr = round(bwfk / bwfd, 2)
        bww_l = round(bwwins / bwlosses, 2)
        bwk_d = round(bwkills / bwdeaths, 2)

        finals_to_x_fkdr = 0
        if 0 <= bwfkdr:
            finals_to_x_fkdr = bwfd - bwfk
            fkdr_var = "1"
        if 1 <= bwfkdr:
            finals_to_x_fkdr = bwfd * 2 - bwfk
            fkdr_var = "2"
        if 2 <= bwfkdr:
            finals_to_x_fkdr = bwfd * 3 - bwfk
            fkdr_var = "3"
        if 3 <= bwfkdr:
            finals_to_x_fkdr = bwfd * 4 - bwfk
            fkdr_var = "4"
        if 4 <= bwfkdr:
            finals_to_x_fkdr = bwfd * 5 - bwfk
            fkdr_var = "5"
        if 5 <= bwfkdr:
            finals_to_x_fkdr = bwfd * 6 - bwfk
            fkdr_var = "6"
        if 6 <= bwfkdr:
            finals_to_x_fkdr = bwfd * 7 - bwfk
            fkdr_var = "7"

        bwkills_to_x_k_d = 0
        if 0 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths - bwkills
            k_d_var = "1"
        if 1 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths * 2 - bwkills
            k_d_var = "2"
        if 2 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths * 3 - bwkills
            k_d_var = "3"
        if 3 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths * 4 - bwkills
            k_d_var = "4"
        if 4 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths * 5 - bwkills
            k_d_var = "5"
        if 5 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths * 6 - bwkills
            k_d_var = "6"
        if 6 <= bwk_d:
            bwkills_to_x_k_d = bwdeaths * 7 - bwkills
            k_d_var = "7"

        bwwins_to_x_w_l = 0
        if 0 <= bww_l:
            bwwins_to_x_w_l = bwlosses - bwwins
            w_l_var = "1"
        if 1 <= bww_l:
            bwwins_to_x_w_l = bwlosses * 2 - bwwins
            w_l_var = "2"
        if 2 <= bww_l:
            bwwins_to_x_w_l = bwlosses * 3 - bwwins
            w_l_var = "3"
        if 3 <= bww_l:
            bwwins_to_x_w_l = bwlosses * 4 - bwwins
            w_l_var = "4"
        if 4 <= bww_l:
            bwwins_to_x_w_l = bwlosses * 5 - bwwins
            w_l_var = "5"
        if 5 <= bww_l:
            bwwins_to_x_w_l = bwlosses * 6 - bwwins
            w_l_var = "6"
        if 6 <= bww_l:
            bwwins_to_x_w_l = bwlosses * 7 - bwwins
            w_l_var = "7"
    else:
        print("please try again")


def duelsstats(username):
    if hypixelapirequests.status_code == 200:
        hypixeldata = hypixelapirequests.json()

        if hypixeldata["player"] is None:
            print("profile error")

        if len(username) < 3:
            print("profile error")

        displayname = hypixeldata["player"]["displayname"]
        if "rank" in hypixeldata["player"] and hypixeldata["player"]["rank"] != "NORMAL":
            rank = hypixeldata["player"]["rank"]
        elif "newPackageRank" in hypixeldata["player"]:
            rank = hypixeldata["player"]["newPackageRank"]
        elif "packageRank" in hypixeldata["player"]:
            rank = hypixeldata["player"]["packageRank"]
        else:
            rank = "NON"
        if rank == "MVP_PLUS":
            rank = "MVP+"
        if rank == "VIP_PLUS":
            rank = "VIP+"

        if "kills" in hypixeldata["player"]["stats"]["Duels"]:
            duelskills = hypixeldata["player"]["stats"]["Duels"]["kills"]
        else:
            duelskills = 0
        if "deaths" in hypixeldata["player"]["stats"]["Duels"]:
            duelsdeaths = hypixeldata["player"]["stats"]["Duels"]["deaths"]
        else:
            duelsdeaths = 0
        if "wins" in hypixeldata["player"]["stats"]["Duels"]:
            duelswins = hypixeldata["player"]["stats"]["Duels"]["wins"]
        else:
            duelswins = 0
        if "losses" in hypixeldata["player"]["stats"]["Duels"]:
            duelslosses = hypixeldata["player"]["stats"]["Duels"]["losses"]
        else:
            duelslosses = 0
        if "coins" in hypixeldata["player"]["stats"]["Duels"]:
            duelscoins = hypixeldata["player"]["stats"]["Duels"]["coins"]
        else:
            duelscoins = 0
        if "duels_duels_division" in hypixeldata["player"]["achievements"]:
            duelsdivision = hypixeldata["player"]["achievements"]["duels_duels_division"]
            if duelsdivision == 1:
                duelsdivisionname = "Rookie"
            if duelsdivision == 2:
                duelsdivisionname = "Iron"
            if duelsdivision == 3:
                duelsdivisionname = "Gold"
            if duelsdivision == 4:
                duelsdivisionname = "Diamond"
            if duelsdivision == 5:
                duelsdivisionname = "Master"
            if duelsdivision == 6:
                duelsdivisionname = "Legend"
            if duelsdivision == 7:
                duelsdivisionname = "Grandmaster"
            if duelsdivision == 8:
                duelsdivisionname = "Godlike"
        else:
            duelsdivision = "N/A"

        duelsw_l = round(duelswins / duelslosses, 2)
        duelsk_d = round(duelskills / duelslosses, 2)

        duelskills_to_x_k_d = 0
        if duelsk_d <= 1:
            duelskills_to_x_k_d = duelsdeaths - duelskills
            k_d_var = "1"
        if 1 <= duelsk_d:
            duelskills_to_x_k_d = duelsdeaths * 2 - duelskills
            k_d_var = "2"
        if 2 <= duelsk_d:
            duelskills_to_x_k_d = duelsdeaths * 3 - duelskills
            k_d_var = "3"
        if 3 <= duelsk_d:
            duelskills_to_x_k_d = duelsdeaths * 4 - duelskills
            k_d_var = "4"
        if 4 <= duelsk_d:
            duelskills_to_x_k_d = duelsdeaths * 5 - duelskills
            k_d_var = "5"
        if 5 <= duelsk_d:
            duelskills_to_x_k_d = duelsdeaths * 6 - duelskills
            k_d_var = "6"
        if 6 <= duelsk_d:
            duelskills_to_x_k_d = duelsdeaths * 7 - duelskills
            k_d_var = "7"

        duelswins_to_x_k_d = 0
        if duelsw_l <= 1:
            duelswins_to_x_k_d = duelslosses - duelswins
            w_l_var = "1"
        if 1 <= duelsw_l:
            duelswins_to_x_k_d = duelslosses * 2 - duelswins
            w_l_var = "2"
        if 2 <= duelsw_l:
            duelswins_to_x_k_d = duelslosses * 3 - duelswins
            w_l_var = "3"
        if 3 <= duelsw_l:
            duelswins_to_x_k_d = duelslosses * 4 - duelswins
            w_l_var = "4"
        if 4 <= duelsw_l:
            duelswins_to_x_k_d = duelslosses * 5 - duelswins
            w_l_var = "5"
        if 5 <= duelsw_l:
            duelswins_to_x_k_d = duelslosses * 6 - duelswins
            w_l_var = "6"
        if 6 <= duelsw_l:
            duelswins_to_x_k_d = duelslosses * 7 - duelswins
            w_l_var = "7"

        duelswins_to_x_division = 0
        if duelsdivision == 1:
            duelswins_to_x_division = 200 - duelswins
            div_var = "Iron"
        if duelsdivision == 2:
            duelswins_to_x_division = 500 - duelswins
            div_var = "Gold"
        if duelsdivision == 3:
            duelswins_to_x_division = 1000 - duelswins
            div_var = "Diamond"
        if duelsdivision == 4:
            duelswins_to_x_division = 2000 - duelswins
            div_var = "Master"
        if duelsdivision == 5:
            duelswins_to_x_division = 4000 - duelswins
            div_var = "Legend"
        if duelsdivision == 6:
            duelswins_to_x_division = 10000 - duelswins
            div_var = "Grandmaster"
        if duelsdivision == 7:
            duelswins_to_x_division = 20000 - duelswins
            div_var = "Godlike"


root = tk.Tk()


def hex2rgb(str_rgb):
    try:
        rgb = str_rgb[1:]

        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError("Invalid value %r provided for rgb color." % str_rgb)

    return tuple(int(v, 16) for v in (r, g, b))


class Placeholder_State(object):
    __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'contains_placeholder'


def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color = normal_color
    state.normal_font = normal_font
    state.placeholder_color = color
    state.placeholder_font = font
    state.placeholder_text = placeholder
    state.contains_placeholder = True

    def on_focusin(event, entry=entry, state=state):
        if state.contains_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font = state.normal_font)

            state.contains_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font = state.placeholder_font)

            state.contains_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font = font)

    entry.bind('<FocusIn>', on_focusin, add = "+")
    entry.bind('<FocusOut>', on_focusout, add = "+")

    entry.placeholder_state = state

    return state


class SearchBox(Frame):
    def __init__(self, master, entry_width=30, entry_font=None, entry_background="white", entry_highlightthickness=1,
                 button_text="Search", button_ipadx=10, button_background="#009688", button_foreground="white",
                 button_font=None, opacity=0.8, placeholder=None, placeholder_font=None, placeholder_color="grey",
                 spacing=3, command=None):
        Frame.__init__(self, master)

        self._command = command

        self.entry = Entry(self, width = entry_width, background = entry_background, highlightcolor = button_background,
                           highlightthickness = entry_highlightthickness)
        self.entry.pack(side = LEFT, fill = BOTH, ipady = 1, padx = (0, spacing))

        if entry_font:
            self.entry.configure(font = entry_font)

        if placeholder:
            add_placeholder_to(self.entry, placeholder, color = placeholder_color, font = placeholder_font)

        self.entry.bind("<Escape>", lambda event: self.entry.nametowidget(".").focus())
        self.entry.bind("<Return>", self._on_execute_command)

        opacity = float(opacity)

        if button_background.startswith("#"):
            r, g, b = hex2rgb(button_background)
        else:
            # Color name
            r, g, b = master.winfo_rgb(button_background)

        r = int(opacity * r)
        g = int(opacity * g)
        b = int(opacity * b)

        if r <= 255 and g <= 255 and b <= 255:
            self._button_activebackground = '#%02x%02x%02x' % (r, g, b)
        else:
            self._button_activebackground = '#%04x%04x%04x' % (r, g, b)

        self._button_background = button_background

        self.button_label = Label(self, text = button_text, background = button_background,
                                  foreground = button_foreground, font = button_font)
        if entry_font:
            self.button_label.configure(font = button_font)

        self.button_label.pack(side = LEFT, fill = Y, ipadx = button_ipadx)

        self.button_label.bind("<Enter>", self._state_active)
        self.button_label.bind("<Leave>", self._state_normal)

        self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)

    def get_text(self):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            if entry.placeholder_state.contains_placeholder:
                return ""
            else:
                return entry.get()
        else:
            return entry.get()

    def set_text(self, text):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            entry.placeholder_state.contains_placeholder = False

        entry.delete(0, END)
        entry.insert(0, text)

    def clear(self):
        self.entry_var.set("")

    def focus(self):
        self.entry.focus()

    def _on_execute_command(self, event):
        text = self.get_text()
        self._command(text)

    def _state_normal(self, event):
        self.button_label.configure(background = self._button_background)

    def _state_active(self, event):
        self.button_label.configure(background = self._button_activebackground)


if __name__ == "__main__":
    try:
        from Tkinter import Tk
        from tkMessageBox import showinfo
    except ImportError:
        from tkinter import Tk
        from tkinter.messagebox import showinfo


    def command(text):
        showinfo("search command", "searching:%s" % text)


    root = Tk()
    SearchBox(root, command = command, placeholder = "Type and press enter", entry_highlightthickness = 0).pack(
        pady = 6, padx = 3)

    root.mainloop()


json_data.close()