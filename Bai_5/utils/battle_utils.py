import random

from utils.item_utils import find_player


def fight_monster(records):
    if records == []:
        print("Hệ thống chưa có dữ liệu người chơi.")
    else:
        monsters = [
        {"name": "Bug Python", "damage": 20, "reward_gold": 100},
        {"name": "Import Error", "damage": 35, "reward_gold": 150},
        {"name": "Module Not Found", "damage": 50, "reward_gold": 250}
    ]
        
        player_id = input("Nhập mã người chơi: ").strip().upper()
        player = find_player(records, player_id)

        if player is False:
            print("Không tìm thấy người chơi!")
        else:
            battle = random.choice(monsters)
            print(f">> Quái vật xuất hiện: {battle["name"]}")
            for mon in monsters:
                if battle["name"] == mon["name"]:
                    hp = player["hp"] - mon["damage"]
                    print(f">> {player["name"]} bị mất {mon["damage"]} HP.")
                
                    if hp > 0:
                        player["gold"] += mon["reward_gold"]
                        print(f">> Chiến thắng! Bạn nhận được {mon["reward_gold"]} vàng.")
                        print(f">> HP còn lại: {hp}")
                    else:
                        print("Người chơi đã gục ngã, không thể tiếp tục chiến đấu!")

        