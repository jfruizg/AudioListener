import speech_recognition as sr
from pydub import AudioSegment
from os import remove



def print_hi():
    arr = []
    r = sr.Recognizer()
    num_inicial = 1
    num_audios = 21
    for i in range(num_inicial, num_audios + 1):
        if i != 0:
            try:
                audio = 'Audio' + str(i) + '.ogg'
                wav_filename = r"Audio" + str(i) + ".wav"
                track = AudioSegment.from_file(audio, format='ogg')
                file_handle = track.export(wav_filename, format='wav')
                audio_file = sr.AudioFile(file_handle)
                with audio_file as source:
                    audio_analizar = r.record(source)
                texto1 = r.recognize_google(audio_analizar, language='es-ES')
                arr.append(texto1)
            except Exception:
                arr.append("Error de archivo"+wav_filename)
    return arr


if __name__ == '__main__':

    arr = print_hi()
    cont = 1
    for i in arr:
        print(str(cont) + i + '\n')
        cont = cont + 1


