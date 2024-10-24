from pymem import Pymem
from pymem.ptypes import RemotePointer

# OFFSETS 
decks_title_offsets = [0x148,0x178,0x1A8,0x1D8]
decks_artist_offsets = [0x150,0x180,0x1B0,0x1E0]
decks_album_offsets = [0x158,0x188,0x1B8,0x1e8]

#List of offsets
listOfOffsets = [decks_title_offsets,decks_artist_offsets,decks_album_offsets]


print("Attached to Rekordbox...\n")
pm = Pymem('rekordbox.exe')

class Decks():
    def __init__(self,title,album,artist):
        self.title = title
        self.album = album
        self.artist = artist

def main():
    listOfDecks=[]
    for i in range(4):
        #tempObject = Decks("","","")
        listOfDecks.append(Decks(i,"",""))

    baseAddress = pm.base_address #Gets the base address for Rekordbox. Equivalant of "reakordbox.exe" from cheat engine.
    
    print("Searching for Base Address...:")
    print(hex(baseAddress))
    #offset(s)

    print("\npm.process_handle =\t"+str(pm.process_handle))

    BasePointer = RemotePointer(int(pm.process_handle),baseAddress+0x05252908) #Gets the base pointer using the process handle and "reakordbox.exe" + 0x05252908 from CE.
    placeInOffset=0


    for  offset in listOfOffsets:
        #print("first for loop:" + str(offset))
        deckPosition = 0
        for element in offset:
            elementAddress = RemotePointer(int(pm.process_handle),BasePointer.value+element) #title is the address each loaded song. 
            #print("Second for Loop "+ str(element) +"\n"+ hex(elementAddress.value))

            try:
                addressValue = pm.read_string(elementAddress.value,50)
                match placeInOffset:
                    case 0: #TITLE
                        listOfDecks[deckPosition].title = str(addressValue)
                        deckPosition+=1
                    case 1: #Artist
                        listOfDecks[deckPosition].artist = str(addressValue)
                        deckPosition+=1
                    case 2: #Album 
                        listOfDecks[deckPosition].album = str(addressValue)
                        deckPosition+=1
            except Exception as e: print(e)

        placeInOffset+=1

    for decksList in listOfDecks:
        
        print(decksList.title,decksList.artist,decksList.album)

if __name__ == '__main__':
        main()