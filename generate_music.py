from music21 import stream, note
import random

# Notes used for music generation
notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]

# Create music stream
music = stream.Stream()

# Generate 50 random notes
for i in range(50):
    n = note.Note(random.choice(notes))
    n.quarterLength = 1
    music.append(n)

# Save as MIDI
music.write('midi', fp='generated_music.mid')

print("Music generated successfully!")
