def on_button_pressed_a():
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    if input.temperature() < 0:
        basic.show_string("brrrr")
basic.forever(on_forever)
