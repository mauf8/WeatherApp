import PySimpleGUI as psg
import weatherAppBackend
import requests


def main():


    psg.theme()  # Add a touch of color

    # pad=((left, right), (top, bottom))
    padding_for_text_and_inputField = ((0, 0), (30, 0))
    padding_for_image_and_text = ((0, 0), (60, 0))

    weather_info_group = [
        [psg.Push(), psg.Image(key="-IMAGE-", size=(400, 400)), psg.Push()],
        [psg.Push(), psg.Text(key="-WEATHER-"), psg.Push()],
        [psg.Push(), psg.Text(key="-DESCRIPTION-"), psg.Push()]
    ]

    weather_text_input_button_group = [
        [psg.Push(), psg.Text('Enter City Name:'), psg.Push()],
        [psg.Push(), psg.Input(key="-CITY-", size=(15, 1)), psg.Push()],
        [psg.Push(), psg.Button('OK'), psg.Button('Exit', button_color="orange"), psg.Push()]]

    layout = [
        [psg.Push(), psg.Frame("Weather Info", layout=weather_info_group, pad=padding_for_image_and_text, size=(400, 150)),psg.Push()],
        [psg.Push(), psg.Column(layout=weather_text_input_button_group, pad=padding_for_text_and_inputField), psg.Push()]

    ]
    # Create the Window
    window = psg.Window('Weather App', layout, size=(800, 400))
    # Event Loop to process "events" and get the "values" of the inputs

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == 'Exit':  # if the user closes the window or clicks cancel
            break

        if event == "OK":
            entered_city = values["-CITY-"]
            weather_info = weatherAppBackend.get_weather_Temp(entered_city)
            weather_image_url = weatherAppBackend.get_weather_icon(entered_city)
            weather_description = weatherAppBackend.get_weather_description(entered_city)
            window["-DESCRIPTION-"].update(weather_description)
            window["-WEATHER-"].update(weather_info)

            try:
                # Fetch the image from the URL
                image_data = requests.get(weather_image_url).content
                # Update the Image element with the loaded image directly from the URL
                window["-IMAGE-"].update(data=image_data)

            except Exception as e:
                print(f"Error updating the image: {e}")

    window.close()

