import flet as ft

def main(page: ft.Page):
    page.title = "Music Player 🎵"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    songs = [
        {"title": "God's Plan", "artist": "Drake", "album": "Scorpion", "file": "Audio/Drake - God's Plan.mp3"},
        {"title": "The One That Got Away", "artist": "Katy Perry", "album": "Teenage Dream", "file": "Audio/Katy Perry - The One That Got Away.mp3"},
        {"title": "Billie Jean", "artist": "Michael Jackson", "album": "Thriller", "file": "Audio/Michael Jackson - Billie Jean.mp3"},
        {"title": "Smooth Criminal", "artist": "Michael Jackson", "album": "Bad", "file": "Audio/Michael Jackson - Smooth Criminal.mp3"},
        {"title": "Riptide", "artist": "Vance Joy", "album": "Dream Your Life Away", "file": "Audio/Vance Joy - Riptide.mp3"},
    ]

    i = 0
    is_playing = False

    audio = ft.Audio(src=songs[i]["file"])
    page.overlay.append(audio)

    title = ft.Text(songs[i]["title"], size=20)
    artist = ft.Text(songs[i]["artist"])
    album = ft.Text(songs[i]["album"])
    volume_text = ft.Text("Volume: 100%")

    def update():
        audio.src = songs[i]["file"]
        audio.play()
        title.value = songs[i]["title"]
        artist.value = songs[i]["artist"]
        album.value = songs[i]["album"]
        page.update()

    def play_pause(e):
        nonlocal is_playing
        if is_playing:
            audio.pause()
        else:
            audio.play()
        is_playing = not is_playing

    def next_song(e):
        nonlocal i
        i = (i + 1) % len(songs)
        update()

    def prev_song(e):
        nonlocal i
        i = (i - 1) % len(songs)
        update()

    def change_volume(e):
        audio.volume = slider.value / 100
        volume_text.value = f"Volume: {int(slider.value)}%"
        page.update()

    slider = ft.Slider(min=0, max=100, value=100, on_change=change_volume)

    page.add(
        ft.Column([
            ft.Text("🎶 Music Player", size=30),
            title,
            artist,
            album,
            ft.Row([
                ft.ElevatedButton("⏮ Previous", on_click=prev_song),
                ft.ElevatedButton("▶️ Play/Pause", on_click=play_pause),
                ft.ElevatedButton("⏭ Next", on_click=next_song),
            ]),
            ft.Text("🔊 Volume"),
            slider,
            volume_text
        ], alignment="center")
    )

# 🔥 IMPORTANTE: esto fuerza a abrir en navegador
ft.app(target=main, view=ft.AppView.WEB_BROWSER)