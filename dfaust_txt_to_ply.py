import numpy as np
import os


dfolder = 'C:\\00stuff\ImgProc\projectwork\Data\\textfilesextra\shakearmstextfile'
action = 'shake_arms'

for filename in os.listdir(dfolder):
        nameparts = filename.split("_")
        newfilename = dfolder + "\\" + nameparts[0] + "_" + action + '.ply'
        print(filename)

        #read text file
        data = np.loadtxt((dfolder + "\\" + filename),delimiter=',', max_rows=240000)
        #print(data.shape)


        #write to ply file
        with open(newfilename, 'w') as plyfile:
            # First magical word
            header = ['ply']

            # Encoding format
            header.append('format ascii 1.0')
            header.append('comment width 1023')
            header.append('element vertex 240000')

            header.append('property float x')
            header.append('property float y')
            header.append('property float z')

            header.append('property uchar r')
            header.append('property uchar g')
            header.append('property uchar b')

            header.append('property uchar label')

            # End of header
            header.append('end_header')

            # Write all lines
            for line in header:
                plyfile.write("%s\n" % line)

            #write data
            linect = 0 
            for line in data:
                #insert matching rgb to label if needed here
                plyfile.write(str(data[linect, 0]) + " " + str(data[linect,1]) + " " + str(data[linect,2]) + " "
                            + str(data[linect, 3]) + " " + str(data[linect,4]) + " " + str(data[linect,5]) + " "
                            + str(data[linect, 6]) + "\n")
                linect += 1
            plyfile.close()
            
