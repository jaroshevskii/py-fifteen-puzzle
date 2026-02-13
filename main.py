import random
from pyray import *


class Card:
    def __init__(self, text: str, rectangle: Rectangle):
        self.text = text
        self.rectangle = rectangle

    def draw(self):
        draw_rectangle_rec(self.rectangle, BLACK)
        body = Rectangle(self.rectangle.x + 2, self.rectangle.y + 2, self.rectangle.width - 4,
                         self.rectangle.height - 4)
        font_size = 50
        position_y = int(self.rectangle.y + (self.rectangle.height - font_size) / 2)
        if self.text != "":
            draw_rectangle_rec(body, ORANGE)
        else:
            draw_rectangle_rec(body, DARKPURPLE)
        position_x = int(self.rectangle.x + (self.rectangle.width - measure_text(self.text, font_size)) / 2)
        draw_text(self.text, position_x, position_y, font_size, BLACK)


def check_consecutive(cards):
    for i in range(len(cards) - 2):
        if cards[i].text.isdigit() and cards[i + 1].text.isdigit() and cards[i + 2].text.isdigit():
            if int(cards[i].text) + 1 == int(cards[i + 1].text) and int(cards[i + 1].text) + 1 == int(
                    cards[i + 2].text):
                return True

    return False


def shuffle_card_text(cards):
    card_texts = [card.text for card in cards]
    random.shuffle(card_texts)
    for i in range(len(cards)):
        cards[i].text = card_texts[i]
    if check_consecutive(cards):
        cards.reverse()


def get_empty_card_index(cards):
    for i, card in enumerate(cards):
        if card.text == "":
            return i
    return None


def is_sorted(cards):
    expected_text = [str(i) for i in range(1, 16)]
    if cards[-1].text != "":
        return False
    return [card.text for card in cards[:-1]] == expected_text


card_size = 94
cards_per_row = 4
cards_per_column = 4
ident = 16
cards = []
for row in range(cards_per_column):
    for col in range(cards_per_row):
        x = col * card_size
        y = row * card_size
        if row == 4 - 1 and col == cards_per_row - 1:
            card = Card("", Rectangle(x, y, card_size, card_size))
        else:
            card_number = str(row * cards_per_row + col + 1)
            rect = Rectangle(x, y, card_size, card_size)
            card = Card(card_number, rect)
        cards.append(card)

shuffle_card_text(cards)

is_end_of_geme = False

set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)
init_window(card_size * 4, card_size * 4, "Find Pair")

while not window_should_close():
    if is_key_pressed(KeyboardKey.KEY_S):
        shuffle_card_text(cards)
    if is_sorted(cards):
        is_end_of_geme = True
    if is_end_of_geme:
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            is_end_of_geme = False
            shuffle_card_text(cards)
    else:
        for i in range(0, len(cards)):
            empty_card_index = get_empty_card_index(cards)
            if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT) and check_collision_point_rec(
                    get_mouse_position(), cards[i].rectangle):
                if i == empty_card_index - 1 or i == empty_card_index + 1 or i == empty_card_index - cards_per_row or i == empty_card_index + cards_per_row:
                    cards[empty_card_index].text = cards[i].text
                    cards[i].text = ""

    begin_drawing()
    clear_background(DARKPURPLE)

    for card in cards:
        card.draw()

    if is_end_of_geme:
        text = "Victory!"
        draw_rectangle(0, 0, get_screen_width(), get_screen_height(), Color(0, 0, 0, 192))
        font_size = 60
        position_x = int((get_screen_width() - measure_text(text, font_size)) / 2)
        position_y = int((get_screen_height() - font_size) / 2 - ident * 2)
        draw_text(text, position_x, position_y, font_size, WHITE)

        desctiption = "Click to continue."
        desctiption_position_x = int((get_screen_width() - measure_text(desctiption, 20)) / 2)
        desctiption_position_y = position_y + font_size + ident
        draw_text(desctiption, desctiption_position_x, desctiption_position_y, 20, WHITE)

    end_drawing()

close_window()