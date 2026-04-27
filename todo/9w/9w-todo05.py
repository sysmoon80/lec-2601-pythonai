# 해보기9 (5) - Turtle RPG 캐릭터 전투 예제
# 요구 사항:
# 1) 캐릭터 생성(player, monster)
# 2) UI 설정(Turtle Screen)
# 3) render() 함수
# 4) attack() 함수
# 5) reset() 함수

import random
import turtle as t


# 1. 캐릭터 생성 (player, monster)
def make_character(name, max_hp, atk, color, x, y):
    return {
        "name": name,
        "max_hp": max_hp,
        "hp": max_hp,
        "atk": atk,
        "color": color,
        "x": x,
        "y": y,
    }


player = make_character("Player", 120, 28, "royalblue", -170, 20)
monster = make_character("Monster", 150, 20, "firebrick", 170, 20)


# 2. UI 설정 (Turtle Screen)
screen = t.Screen()
screen.setup(width=900, height=600)
screen.title("Turtle RPG Battle")
screen.bgcolor("white")


# 각각의 터틀 객체를 만들어 캐릭터와 UI를 그리는 데 사용
ui_pen = t.Turtle(visible=False)
ui_pen.hideturtle()
ui_pen.speed(0)
ui_pen.penup()

# 캐릭터를 그리는 터틀 객체
player_drawer = t.Turtle(visible=False)
player_drawer.hideturtle()
player_drawer.speed(0)
player_drawer.penup()

# 몬스터를 그리는 터틀 객체
monster_drawer = t.Turtle(visible=False)
monster_drawer.hideturtle()
monster_drawer.speed(0)
monster_drawer.penup()

# 게임 상태를 저장하는 딕셔너리
state = {"message": "Press SPACE to attack, R to reset"}


def draw_character(drawer, character):
    drawer.clear()
    drawer.goto(character["x"], character["y"])
    drawer.dot(90, character["color"])
    drawer.goto(character["x"], character["y"] - 65)
    drawer.color("black")
    drawer.write(character["name"], align="center", font=("Arial", 14, "bold"))


def draw_hp_bar(x, y, width, height, ratio, fill_color):
    ui_pen.goto(x, y)
    ui_pen.pendown()
    ui_pen.pensize(2)
    ui_pen.pencolor("black")
    for _ in range(2):
        ui_pen.forward(width)
        ui_pen.right(90)
        ui_pen.forward(height)
        ui_pen.right(90)
    ui_pen.penup()

    if ratio > 0:
        ui_pen.goto(x, y)
        ui_pen.fillcolor(fill_color)
        ui_pen.begin_fill()
        ui_pen.pendown()
        ui_pen.forward(width * ratio)
        ui_pen.right(90)
        ui_pen.forward(height)
        ui_pen.right(90)
        ui_pen.forward(width * ratio)
        ui_pen.right(90)
        ui_pen.forward(height)
        ui_pen.right(90)
        ui_pen.penup()
        ui_pen.end_fill()


# 3. render() 함수
def render():
    ui_pen.clear()
    draw_character(player_drawer, player)
    draw_character(monster_drawer, monster)

    player_ratio = max(player["hp"], 0) / player["max_hp"]
    monster_ratio = max(monster["hp"], 0) / monster["max_hp"]

    ui_pen.goto(-320, 220)
    ui_pen.color("black")
    ui_pen.write(
        f"{player['name']} HP: {max(player['hp'], 0)}/{player['max_hp']}",
        font=("Arial", 14, "normal"),
    )
    draw_hp_bar(-320, 200, 260, 24, player_ratio, "cornflowerblue")

    ui_pen.goto(40, 220)
    ui_pen.write(
        f"{monster['name']} HP: {max(monster['hp'], 0)}/{monster['max_hp']}",
        font=("Arial", 14, "normal"),
    )
    draw_hp_bar(40, 200, 260, 24, monster_ratio, "salmon")

    ui_pen.goto(0, -250)
    ui_pen.write(state["message"], align="center", font=("Arial", 13, "bold"))


# 4. attack() 함수
def attack():
    # 전투가 끝난 상태에서 공격을 시도하면 메시지만 업데이트하고 종료
    if player["hp"] <= 0 or monster["hp"] <= 0:
        state["message"] = "Battle is over. Press R to reset"
        render()
        return

    # 플레이어 공격
    player_damage = random.randint(player["atk"] - 5, player["atk"] + 5)
    monster["hp"] -= player_damage

    if monster["hp"] <= 0:
        monster["hp"] = 0
        state["message"] = f"{player['name']} wins! ({player_damage} damage)"
        render()
        return

    # 몬스터 공격
    monster_damage = random.randint(monster["atk"] - 4, monster["atk"] + 4)
    player["hp"] -= monster_damage

    if player["hp"] <= 0:
        player["hp"] = 0
        state["message"] = (
            f"{player['name']} attacked {player_damage}, "
            f"but {monster['name']} wins with {monster_damage} damage"
        )
    else:
        state["message"] = (
            f"{player['name']} -> {player_damage} dmg, "
            f"{monster['name']} -> {monster_damage} dmg"
        )

    render()


# 5. reset() 함수
def reset():
    player["hp"] = player["max_hp"]
    monster["hp"] = monster["max_hp"]
    state["message"] = "Battle reset. Press SPACE to attack"
    render()


screen.listen()
screen.onkey(attack, "space")
screen.onkey(reset, "r")

render()
t.done()
