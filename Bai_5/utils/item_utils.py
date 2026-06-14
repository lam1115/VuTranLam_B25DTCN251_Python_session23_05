import random

from colorama import Fore, Style, init

init(autoreset=True)


def find_player(records, player_id):
    for player in records:
        if player_id == player["player_id"]:
            return player
    return False

def open_treasure_chest(records):
    if records == []:
        print("Hệ thống chưa có dữ liệu người chơi.")
    else:
        rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]

        player_id = input("Nhập mã người chơi: ").strip().upper()

        player = find_player(records, player_id)

        if player is False:
            print("Không tìm thấy người chơi!")
        else:
            item = random.choice(rewards)
            print(f">> Người chơi {player["name"]} đã mở rương!")
            if item == "100 Gold":
                player["gold"] += 100
                print("+ 100 Gold")
            else:
                player["inventory"].append(item)
                print(f">> Phần thưởng nhận được: {item}"
                    f"\n>> Đã thêm {item} vào túi đồ"
                    )
                

def buy_item(records):
    if records == []:
        print("Hệ thống chưa có dữ liệu người chơi.")
    else:
        shop_items = {
        "Potion": 50,
        "Iron Sword": 200,
        "Magic Book": 300,
        "Mana Stone": 150
    }
        player_id = input("Nhập mã người chơi: ").strip().upper()
        player = find_player(records, player_id)

        if player is False:
            print("Không tìm thấy người chơi!")
        else:
            print(f"Danh sách sản phẩm:"
                f"\n{shop_items}"
                )
            
            item_name = input("Nhập tên vật phẩm muốn mua: ").title()

            for item, price in shop_items.items():
                if item_name == item:
                    if player["gold"] < price:
                        print(f"{Fore.RED}Không đủ vàng để mua vật phẩm này!")
                    else:
                        remaining_amount = player["gold"] - price
                        player["inventory"].append(item_name)
                        print(f">> Mua thành công {item_name}!"
                            f"\n>> Số vàng còn lại: {remaining_amount}"
                            )
                    return
                    
            else:
                print("Vật phẩm không tồn tại trong cửa hàng!")
                return
            
