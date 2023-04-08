import sqlite3
import random

conn = sqlite3.connect("games_base.db")
cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE fav_games (
#         id INT,
#         title TEXT,
#         genre TEXT,
#         year INT,
#         studio_name TEXT
#     );
# ''')
# cursor.execute('''
#     INSERT INTO fav_games(id,title,genre,year,studio_name) VALUES
#         (1, "Call of Duty 4: Modern Warfare", "FPS", 2007, "Infinity Ward, Treyarch, Aspyr Media, N-Space"),
#         (2, "Far Cry 3", "FPS", 2012, "Massive Entertainment, Ubisoft Montreal"),
#         (3, "Grand Theft Auto: San Andreas", "Action-adventure", 2004, "Rockstar North"),
#         (4, "Red Dead Redemption 2", "Action-adventure", 2018, "Rockstar Games"),
#         (5, "Half-Life", "FPS", 1998, "Valve, Crowbar Collective, Gearbox Software"),
#         (6, "Mafia III", "Action-adventure", 2016, "Hangar 13"),
#         (7, "Counter-Strike: Global Offensive", "MMOFPS", 2012, "Valve, Hidden Path Entertainment"),
#         (8, "Uncharted: Drake`s Fortune", "Action-adventure", 2007, "Naughty Dog"),
#         (9, "S.T.A.L.K.E.R.: Shadow of Chernobyl", "FPS", 2007, "GSC Game World"),
#         (10, "Hitman 3", "Stealth", 2021, "IO Interactive");
# ''')
num_id = random.randint(1,10)
res = cursor.execute('''
    SELECT * FROM fav_games WHERE id = (?);
''', [num_id])
for i in res.fetchall():
    print(f"Я вам посоветую такую игру, как: \n Название: {i[1]} \n Жанр: {i[2]} \n Год выпуска: {i[3]} \n Название студии(-й) разработчиков: {i[4]}")
conn.commit()