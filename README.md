# Converting Ancient Indian Classical Music Manuscripts to Audio

## Overview

Indian Classical Music is passed down orally from generation to generation, so many of the traditions from centuries have been lost forever, or changed drastically. Luckily, we have few available manuscripts to understand the music from times past -- most notably, the Sangeetha Sampradaya Pradarshini from 1904 (outlining the songs of Muttuswami Dikshitar) and the Walajapet Manuscripts from the early 1800's (notating the songs of Thyagaraja). These manuscripts give us enough detail to reconstruct the music of those times. But if we do so by hand, we risk inserting our own interpretations while converting them to audio. 

This Python project aims to remove that bias. It aims to read such complex manuscripts exactly as they are written, removing the risk of misinterpretation when humans are doing the reading. Precisely, it will have a library of oscillations (gamakas), along with a corresponding list of audio files; when the program finds an oscillation in the manuscript, it will produce the corresponding audio output. The final audio will need some adjusting to ensure the notes transition smoothly between notes, but it will be an invaluable resource in understanding exactly what these notations say.

## Step 1: Using Neural Networks to Convert Manuscripts to Text 

We will then use Optical Character Recognition (OCR) neural networks to convert the manuscripts into a text format the program can use. These networks will need to be tailor-made for this use because existing networks do not meet the needs of the project. For one, the notations are arranged in an unconventional table format that existing OCR technologies cannot read. Further, the notations also use extensive symbols unique to Indian Classical Music, so we need to train the network to recognize them.

## Step 2: Creating a Dictionary of Oscillations (Gamakas)

Much of the difficulty in reading these manuscripts lies in interpreting the complex oscillations they describe. The first step, therefore, is to create a 'dictionary of oscillations' -- that is, a dictionary of all the gamakas listed in the Sangeetha Sampradaya Pradarshini and the Walajapet Manuscripts -- and convert them to audio files (in .wav format) for all possible scales. This will give us an audio file for each oscillation and each note; we will then to join these notes together to reconstruct the entire song. 

## Latest Progress

So far, I've made functions that handle basic glides and oscillations in a minor scale (Thodi Ragam): the code for that is in `FunWithScales.py`.  If you run it, it'll produce an audio file (`gamakamthodi.wav`) that plays the basic oscillations of the scale. This needs to be majorly upscaled to reconstruct all the manuscripts, but it's a sign that a computer can even be programmed to sing Indian Classical Music in the first place -- quite a miracle, if you ask me!

## Sources

To interpret the oscillations in these manuscripts, I am referring to:

1. <u>The Ph.D. Thesis of Dr. RS Jayalakshmi</u>: "Subbarama Dikshitarin Sangita Sampradaya Pradarsiniyil Gamakangal". It contains detailed descriptions of how to sing the oscillations of the Sangeetha Sampradaya Pradarshini -- with audio demonstrations. (Link here: http://musicresearchlibrary.net/omeka/items/show/2483)
2. <u>Jnanarnava</u>: An initiative by musicians TM Krishna, RK Sriramkumar, K Arunprakash, and Dr. RS Jayalakshmi to record the Sangeetha Sampradaya Pradarshini as written. I am using these recordings as further exemplars to learn how to interpret the notations. (Link here:http://jnanarnava.org/)
3. <u>The Lost Melodies</u>: This channel is spearheaded by Aravindhan Ranganathan to create audio versions of select songs from the Walajapet manuscripts. I am using them as exemplars to learn how to interpret the notations. (Link here: https://www.youtube.com/playlist?list=PLewxNWNgoxAqvPfh4bpkBzhOyHUVwBqJd)