input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
})
basic.forever(function on_forever() {
    if (input.temperature() < 0) {
        basic.showString("brrrr")
    }
    
})
