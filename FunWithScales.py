# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 07:38:56 2020

@author: mythkc
"""
import numpy as np
from scipy.io.wavfile import write

# always use this fixed sample rate (sps stands for "samples per second")
sps = 44100 




################# MAIN FUNCTION TO PLAY NOTES ################################


def hold_note (frequency, stdtime):
    # stdtime (standard time) is the time we *wish* each note took if it weren't for the clicking noise
    
    period = 1/frequency
    # To avoid clicks, the peak of the first sine wave ending must align with the peak of the second sine wave starting
    # We allow each frequency to run for the number (n) of period-multiples whose total time IS JUST ABOUT TO EXCEED the stdtime

    # initializing n
    n = 1
    
    # n = smallest number of period-multiples EXCEEDING the stdtime 
    
    while n*period < stdtime:     
        n = n + 1 
            
    time = n*period
    
    each_sample_number = np.arange(time * sps)
    waveform = np.sin(2 * np.pi * each_sample_number * frequency / sps)
    waveform_quiet = waveform * 0.3
    waveform_integers = np.int16(waveform_quiet * 32767)
    
    return (waveform_integers)



def hold_note_clicks (frequency, time):
    
    
    
    each_sample_number = np.arange(time * sps)
    waveform = np.sin(2 * np.pi * each_sample_number * frequency / sps)
    waveform_quiet = waveform * 0.3
    waveform_integers = np.int16(waveform_quiet * 32767)
    
    return (waveform_integers)



################# TESTING THE FUNCTION ######################################
    
# How to ADD two sine waves
output_add = hold_note(138.59, 5) + hold_note(277.18, 5)

# How to CONCATENATE two sine waves
output_concat = np.concatenate((hold_note(138.59, 5), hold_note(277.18, 5)))
write('LowSAHighSA.wav', sps, output_concat)

output_concat = np.concatenate((hold_note_clicks(138.59, 5), hold_note_clicks(277.18, 5)))
write('LowSAHighSA_clicks.wav', sps, output_concat)



################# PLAYING SCALES: in the key C-sharp #################

swara_dictionary = {
    "p": 103.83,
    "d1": 110.00,
    "d2": 116.54,
    "d3": 123.47,
    "n1": 116.54,
    "n2": 123.47,
    "n3": 130.81,
    "S1": 138.59,
    "R1": 146.83,
    "R2": 155.56,
    "R3": 164.81,
    "G1": 155.56,
    "G2": 164.81,
    "G3": 174.61,
    "M1": 185.00,
    "M2": 196.00,
    "P": 207.65,
    "D1": 220.00,
    "D2": 233.08,
    "D3": 246.94,
    "N1": 233.08,
    "N2": 246.94,
    "N3": 261.63,
    "S2": 277.18,
    "rr1": 293.66,
    "rr2": 311.13,
    "rr3": 329.63,
    "gg1": 311.13,
    "gg2": 329.63,
    "gg3": 349.23,
    "mm1": 369.99,
    "mm2": 392.00,
    "pp": 415.30
}



shankarabharanam = np.concatenate((hold_note(swara_dictionary["S1"], 1), 
                                hold_note(swara_dictionary["R2"], 1),
                                hold_note(swara_dictionary["G3"], 1),
                                hold_note(swara_dictionary["M1"], 1),
                                hold_note(swara_dictionary["P"], 1),
                                hold_note(swara_dictionary["D2"], 1),
                                hold_note(swara_dictionary["N3"], 1),
                                hold_note(swara_dictionary["S2"], 1)))

write('shankarabharanam.wav', sps, shankarabharanam)

thodi = np.concatenate((hold_note(swara_dictionary["S1"], 1), 
                                hold_note(swara_dictionary["R1"], 1),
                                hold_note(swara_dictionary["G2"], 1),
                                hold_note(swara_dictionary["M1"], 1),
                                hold_note(swara_dictionary["P"], 1),
                                hold_note(swara_dictionary["D1"], 1),
                                hold_note(swara_dictionary["N2"], 1),
                                hold_note(swara_dictionary["S2"], 1)))

write('thodi.wav', sps, thodi)

rasikapriya = np.concatenate((hold_note(swara_dictionary["S1"], 1), 
                                hold_note(swara_dictionary["R3"], 1),
                                hold_note(swara_dictionary["G3"], 1),
                                hold_note(swara_dictionary["M2"], 1),
                                hold_note(swara_dictionary["P"], 1),
                                hold_note(swara_dictionary["D3"], 1),
                                hold_note(swara_dictionary["N3"], 1),
                                hold_note(swara_dictionary["S2"], 1)))

write('rasikapriya.wav', sps, rasikapriya)






#################################### JAARU with CLICKS #######################




frequencies = np.linspace (swara_dictionary["S1"], swara_dictionary["S2"], num=40)


# output is the array that will contain the frequencies of the full jaaru 

output = np.int16([])

# stdtime (standard time) is the time we *wish* each note took if it weren't for the clicking noise

time = 0.08

for i in range (0, len(frequencies)):
    freq = frequencies [i]
    

    output = np.concatenate((output, hold_note_clicks(freq, time)))

       
write('jaaru_clicks.wav', sps, output)






#################################### JAARU no CLICKS ###################################




# list of all frequencies between start and end note

frequencies = np.linspace (swara_dictionary["S1"], swara_dictionary["S2"], num=40)
 

# output is the array that will contain the frequencies of the full jaaru 

output = np.int16([])

# stdtime (standard time) is the time we *wish* each note took if it weren't for the clicking noise

stdtime = 0.08

# To avoid clicks, the peak of the first sine wave ending must align with the peak of the second sine wave starting
# We allow each frequency to run for the number of period-multiples whose total time IS JUST ABOUT TO EXCEED the stdtime

for i in range (0, len(frequencies)):
    freq = frequencies [i]
    period = 1/freq
    
    # initializing n
    n = 1
    
    # n = smallest number of period-multiples EXCEEDING the stdtime 
    
    while n*period < stdtime:     
        n = n + 1 
         
    if (i%2)==1:
        n = n-1  
           
    time = n*period
    output = np.concatenate((output, hold_note(freq, time)))
    
       
write('jaaru.wav', sps, output)




################################## JAARU FUNCTION ###############################

    
def jaaru (startfrequency, endfrequency, time, intermediatenotes):
    frequencies = np.linspace (startfrequency, endfrequency, num=intermediatenotes)

    # output is the array that will contain the frequencies of the full jaaru 
    output = np.int16([])
    
    
    stdtime = time/len(frequencies)
    
    for i in range (0, len(frequencies)):
        freq = frequencies [i]
        output = np.concatenate((output, hold_note(freq, stdtime)))
           
    return output


output = jaaru(swara_dictionary["S1"], swara_dictionary["S2"],10,50)
    
write('jaarufunction.wav', sps, output)




#################################### GAMAKAM FROM JAARUS ##########################

n = 1
        
while n*(1/swara_dictionary["R1"]) < 1:     
    n = n + 1 
            
output = np.concatenate((hold_note(swara_dictionary["R1"], n/swara_dictionary["R1"]),
                         jaaru(swara_dictionary["R1"], swara_dictionary["M1"],0.3,10),
                         jaaru(swara_dictionary["M1"], swara_dictionary["R2"],0.3,10),
                         jaaru(swara_dictionary["R2"], swara_dictionary["M1"],0.3,10),
                         jaaru(swara_dictionary["M1"], swara_dictionary["R2"],0.3,10),
                         jaaru(swara_dictionary["R2"], swara_dictionary["M1"],0.3,10),
                         jaaru(swara_dictionary["M1"], swara_dictionary["R2"],0.3,10),
                         jaaru(swara_dictionary["M1"], swara_dictionary["R2"],0.3,10),
                         jaaru(swara_dictionary["R2"], swara_dictionary["M1"],0.3,10),
                         hold_note(swara_dictionary["M1"], 1)                       
                         ))

write('gamakam.wav', sps, output)  # thodi Gandharam






###################################### THODI SRGMP ##################################
    
output = np.concatenate((
    
    hold_note(swara_dictionary["S1"], 1), 
    hold_note(swara_dictionary["R1"], 0.125),
    hold_note(swara_dictionary["S1"], 0.5-0.125),
    hold_note(swara_dictionary["R1"], 0.5),
    hold_note(swara_dictionary["G2"], 0.125),
    hold_note(swara_dictionary["R1"], 0.5-0.125),
    jaaru(swara_dictionary["R1"], swara_dictionary["M1"],0.25,10),
    jaaru(swara_dictionary["M1"], swara_dictionary["R2"],0.25,10),
    jaaru(swara_dictionary["M1"], swara_dictionary["R2"],0.25,10),
    jaaru(swara_dictionary["R2"], swara_dictionary["M1"],0.25,10),
    hold_note(swara_dictionary["M1"], 0.5),
    hold_note(swara_dictionary["P"], 2)
    
    ))

write('gamakamthodi.wav', sps, output)



############################### RAGA DICTIONARIES #################################













