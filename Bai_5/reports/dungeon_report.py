from rich.console import Console
from rich.table import Table


def player_status(hp):
    status = None
    if hp >= 100:
        status = "Sung sức"
    elif hp >= 50:
        status = "Ổn định"
    elif hp >= 1:
        status = "Nguy hiểm"
    else:
        status = "Đã gục ngã"
    return status

def display_players(records):
    if records == []:
        print("Hệ thống chưa có dữ liệu người chơi.")
    else:
        console = Console()
        table = Table(title=" --- DANH SÁCH NGƯỜI CHƠI --- ")

        columns = ["Mã", "Tên", "HP", "Mana", "Gold", "Level", "Trạng thái"]
        for column in columns:
            table.add_column(column)
        for record in records:
            status = player_status(record["hp"])

            table.add_row(
                str(record["player_id"]),
                record["name"],
                str(record["hp"]),
                str(record["mana"]),
                str(record["gold"]),
                str(record["level"]),
                status
            )
        console.print(table)


def show_leaderboard(records):
    if records == []:
        print("Hệ thống chưa có dữ liệu người chơi.")
    else:
        console2 = Console()
        table2 = Table(title=" --- BẢNG XẾP HẠNG NGƯỜI CHƠI --- ")

        column2 = ["STT", "Tên", "Level", "Gold", "HP"]

        for column in column2:
            table2.add_column(column)  

        records = sorted(records, key=lambda x:(-x["level"], -x["gold"], -x["hp"]), reverse=False)

        for index, record in enumerate(records, start=1):
            table2.add_row(
                str(index), record["name"], str(record["level"]), str(record["gold"]), str(record["hp"])
            )

        console2.print(table2)