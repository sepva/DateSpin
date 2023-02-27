import arcade
import random as rdm
import time
import math

def pickDate(datelist):
    dateNr = rdm.randrange(0, len(datelist))
    date = datelist[dateNr]
    return date
g
class SpinScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)


    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 800, arcade.load_texture(
            r"../DateSpin/330817011_1337881573458524_3246408094522565062_n.jpg",
            0, 0, 828, 1200))
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(250, 750, 605, 405, arcade.make_transparent_color(arcade.color.AERO_BLUE, 150))
        arcade.draw_lrtb_rectangle_filled(250, 750, 395, 195, arcade.make_transparent_color(arcade.color.AERO_BLUE, 150))
        arcade.draw_text("Spin voor een leuke korte date (weekdagen)", 500, 505, arcade.color.WHITE, 20, 0, "left", "calibri", False, False,
                         "center")
        arcade.draw_text("Spin voor een wat langere date (weekend)", 500, 295, arcade.color.WHITE, 20, 0, "left", "calibri", False, False,
                     "center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 250 < x < 750:
            if 405 < y < 605:
                weekNightDates = ['McDo-date',
                                  'MovieNight',
                                  'Seppie kok',
                                  'Spelletjesavond',
                                  'Kamp bouwen',
                                  'Welnessavond',
                                  'Dessert maken',
                                  'Pizza-maak avond',
                                  'Samen muziekplaylist maken',
                                  'Ijsdate',
                                  'Parkwandeling',
                                  'Fingerpainting',
                                  'Sterrenkijken']
                nextScreen = ResultScreen(weekNightDates)
                self.window.show_view(nextScreen)

            elif 195 < y < 395:
                uitgebreideDates = ['Drive-in movie',
                                    'Dvondje uit',
                                    'Waterpark uitje',
                                    'Projectje samen',
                                    'Zoo bezoeken',
                                    'Shoppingsdagje',
                                    'Brunchdate',
                                    'Scavenger hunt',
                                    'Krijttekeningen maken in de straten',
                                    'Pretpark',
                                    'Mock Olympics',
                                    'Picknick',
                                    'Cinema',
                                    'Eye-bombing',
                                    'Surprise surprise']
                nextScreen = ResultScreen(uitgebreideDates)
                self.window.show_view(nextScreen)

class ResultScreen(arcade.View):
    def __init__(self, datelist):
        super().__init__()
        self.datelist = datelist
        self.result = pickDate(self.datelist)
        self.spin = 0
        self.spinCount = 0
        self.result = None
        self.length = 0

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 800, arcade.load_texture(
            r"../DateSpin/330817011_1337881573458524_3246408094522565062_n.jpg",
            0, 0, 828, 1200))
        if(self.spin == 0):
            arcade.set_background_color(arcade.color.WHITE)
            arcade.draw_lrtb_rectangle_filled(250, 750, 500, 300, arcade.make_transparent_color(arcade.color.AERO_BLUE, 150))
            arcade.draw_text('Spin', 500, 400, arcade.color.WHITE, 20, 0, "left",
                             "calibri", True, False,
                             "center")
        else:
            if(self.spinCount < self.length*4):
                time.sleep(math.exp(self.spinCount/self.length)*0.01)
                arcade.draw_lrtb_rectangle_filled(250, 750, 500, 300, arcade.make_transparent_color(arcade.color.AERO_BLUE, 150))
                arcade.draw_text(self.datelist[self.spinCount % self.length], 500, 400, arcade.color.WHITE, 20, 0, "left",
                                 "calibri", False, False,
                                 "center")
                self.spinCount += 1
            else:
                arcade.draw_lrtb_rectangle_filled(250, 750, 500, 300, arcade.make_transparent_color(arcade.color.AERO_BLUE, 150))
                arcade.draw_text(self.result, 500, 400, arcade.color.WHITE, 20, 0, "left",
                                 "calibri", False, False,
                                 "center")
        arcade.draw_lrtb_rectangle_filled(0, 90, 800, 760, arcade.make_transparent_color(arcade.color.AERO_BLUE, 150))
        arcade.draw_text("Back", 10, 780, arcade.color.WHITE)


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if((250 <= x <= 750) and (300 <= y <= 500) and self.spin == 0):
            self.spin = 1
            self.result = pickDate(self.datelist)
            self.length = self.datelist.index(self.result)

        if 0 < x < 90 and 760 < y < 800:
            Main_menu = SpinScreen()
            self.window.show_view(Main_menu)

def  main():
    window = arcade.Window(1000, 800, "DateSpin")
    spinScreen = SpinScreen()
    window.show_view(spinScreen)
    arcade.run()

if __name__ == "__main__":
    main()