import extractor
from matrix_generator import *
import random
from midiutil.MidiFile import MIDIFile
import pygame

def finalMatrix():
    choice=["150","30","18","109"]
    return extractor.matrixGenerator(generateMatrix("000000000010000000000", 150, transition_dict[random.choice(choice)]), 12, 4)
       
notes=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
keyOfC={'C','D','E','F','G','A','B'}
keyOfDm={'D', 'E', 'F', 'A', 'A#', 'C'}
pitchNumber={'C':60,'C#':61,'D':62,'D#':63,'E':64,'F':65,'F#':66,'G':67,'G#':68,'A':69,'A#':70,'B':71}

def extractNotes(finalMatrix):
    extractedNotes=[]
    noteGroup=[]
    for i in range(0,4):
        for j in range(0,12):
            if finalMatrix[i][j] == 1:
                noteGroup.append(notes[j])
        extractedNotes.append(noteGroup)
        noteGroup=[]
    return extractedNotes

def cleanNoteKey(key, extractedNotes):
    cleanKeys=[]
    for i in range(0,len(extractedNotes)):
        s=set(extractedNotes[i])
        cleanKeys.append(list(s&key))
    return cleanKeys

def reduceNoteGroup(cleanKeys):
    reducedKeys=[]
    for i in range(0,len(cleanKeys)):
        noteGroup=cleanKeys[i]
        newNoteGroup=[]
        r=random.randint(1,4)
        for j in range(0, len(noteGroup)):
            noteValue=noteGroup[j]
            if(len(newNoteGroup)<r):
                if(random.randint(0,2)==1):
                    newNoteGroup.append(noteValue)
        reducedKeys.append(newNoteGroup)
    return reducedKeys

def keysToMidi(reducedKeys):
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, random.randint(80,250))

    # add some notes
    channel = 0
    volume = 100
    duration = [0.25,0.5 ,1,2]
    
    for i in range(0,len(reducedKeys)):
        if not len(reducedKeys[i]) == 0:
            for j in range(0,len(reducedKeys[i])):
                offset=[0,12,-12,-24]
                note=reducedKeys[i][j]
                pitch=pitchNumber[note]+random.choice(offset)
                mf.addNote(track, channel, pitch, time, random.choice(duration), volume)
            time=time+1

    with open("output.mid", 'wb') as outf:
        
        mf.writeFile(outf)
    
midiKeys=reduceNoteGroup(cleanNoteKey(keyOfC, extractNotes(finalMatrix())))

for i in range(0,10):
    reducedKeys=reduceNoteGroup(cleanNoteKey(keyOfC, extractNotes(finalMatrix())))
    #reducedKeys=reduceNoteGroup(extractNotes(finalMatrix()))
    if random.randint(0,2)==1:
        midiKeys=midiKeys+reducedKeys
    else:
        midiKeys=midiKeys+midiKeys

print("Sheet")
print(midiKeys)

keysToMidi(midiKeys)

pygame.init()
pygame.mixer.music.load("output.mid")
pygame.mixer.music.play()


