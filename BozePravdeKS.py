from random import random
from array import array
import wave
 
SampleRate=44100
d4=293
e4=330
f4=350
fis4=370
g4=392
gis4=415
a4=440
ajs4=466
b4=494
c5=523
cis5=554
d5=587
dis5=622
e5=660

notes=[b4,a4,fis4,g4,a4,b4,c5,b4,a4,g4,fis4,e4,g4,a4,b4,d5,c5,b4,a4,g4,a4,a4,b4,a4,fis4,g4,a4,b4,c5,b4,a4,g4,fis4,

       e4,g4,a4,b4,a4,fis4,a4,g4,fis4,e4,d4,d4,d4,a4,a4,a4,c5,b4,a4,gis4,a4,d4,b4,b4,b4,d5,c5,b4,c5,b4,b4,g4,g4,b4,b4,

       c5,d5,e5,e5,d5,d5,b4,b4,b4,d5,c5,b4,c5,b4,a4,b4,b4,g4,g4,b4,b4,c5,d5,e5,e5,d5,d5,b4,b4,b4,d5,c5,b4,c5,b4,a4,g4]

duration=[1,2,2,1,2,2,1,2,2,2,2,1,1,2,2,1,1,1,2,2,1,1,
         1,2,2,1,2,2,1,2,2,2,2,1,1,2,2,1,1,2,2,2,2,1,1,
          1,1,1,1,1,1,2,2,1,1,1,1,1,2,2,2,2,1,1,
          1,1,2,2,2,2,1,1,1,1,1,2,2,2,2,1,2,2,1,1,1,
          1,1,2,2,2,2,1,1,1,1,1,2,2,2,2,1,2,2,1,1]

                                                   
nchannels,swdth,frame_rate,nframes=1,2,44100,44100
 
max_val=32767
 
def Generate(f,nsamples):
 
    N=SampleRate//f
     
    buf=[random()-0.5 for i in range(N)]
    samples=[]
 
    bufSize=len(buf)
 
    for i in range(nsamples):
        samples.append(buf[0])
        avg=0.997*0.5*(buf[0]+buf[1])
        buf.append(avg)
        buf.pop(0)
 
    tempbuf=[int(x*max_val) for x in samples]
 
    data=array('h',tempbuf).tostring()
    file.writeframes(data)
 
     
file=wave.open('BozePravdeKS.wav','wb')
file.setparams((nchannels,swdth,frame_rate,nframes,'NONE','nonecompressed'))
for i in range(len(notes)):
    Generate(notes[i],44100//duration[i])
file.close()
