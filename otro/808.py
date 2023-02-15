import sounddevice as sd
import numpy as np
import soundfile as sf




# Esta función genera una señal de onda cuadrada en una frecuencia dada
def generate_square_wave(frequency, duration, volume):
  sample_rate = 44100
  t = np.linspace(0, duration, int(duration * sample_rate), False)
  square_wave = (volume * np.sign(np.sin(2 * np.pi * frequency * t)))
  return square_wave.astype(np.int16)

# Generamos una señal de onda cuadrada a una frecuencia de 808 Hz
signal = generate_square_wave(808, 1, 10000)

# Reproducimos la señal generada
sd.play(signal, 44100)

# Generamos una señal de onda cuadrada a una frecuencia de 808 Hz
signal = generate_square_wave(808, 1, 10000)

# Guardamos la señal generada en un archivo de audio
sf.write('mi_sonido.wav', signal, 44100)
