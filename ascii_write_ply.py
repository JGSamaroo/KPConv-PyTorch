import numpy as np
import os


#dfolder = 'C:\\00stuff\ImgProc\projectwork\Data\JumpingJacks\\50027_shake_arms'
#action = 'shake_arms'
def write_ply_kernel(filename, kernel_points, xyz):
    linect = kernel_points.shape[0]
    print(kernel_points.shape)
    if not filename.endswith('.ply'):
        filename += '.ply'

        #read text file
        data = np.loadtxt(filename ,delimiter=',', max_rows=240000)
        #print(data.shape)

        #write to ply file
    with open(filename, 'a') as plyfile:
        # First magical word
        header = ['ply']

            # Encoding format
        header.append('format ascii 1.0')
        header.append('comment width 1023')
        header.append(f'element vertex {linect}')

        header.append('property float x')
        header.append('property float y')
        header.append('property float z')

        # End of header
        header.append('end_header')

        # Write all lines
        for line in header:
            plyfile.write("%s\n" % line)

        data = np.empty((linect, 3))
        for lines in range(0, linect):
            data[lines, 0] = kernel_points[lines, 0]
            data[lines, 1] = kernel_points[lines, 1]
            data[lines, 2] = kernel_points[lines, 2]

            #print(data)
            nextline = "{} {} {}\n"
            nextline = nextline.format(data[lines, 0], data[lines, 1],data[lines, 2],)
            plyfile.write(nextline)
    plyfile.close()



def write_ply(filename, sub_points, sub_colors, sub_labels, field_names):
    #for filename in os.listdir(dfolder):
    #print(filename)
    
    linect = sub_labels.shape[0]
    

            # Add extension if not there
    if not filename.endswith('.ply'):
        filename += '.ply'

        #read text file
        data = np.loadtxt(filename ,delimiter=',', max_rows=240000)
        #print(data.shape)


        #write to ply file
    with open(filename, 'a') as plyfile:
        # First magical word
        header = ['ply']

            # Encoding format
        header.append('format ascii 1.0')
        header.append('comment width 1023')
        header.append(f'element vertex {linect}')

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

        data = np.empty((linect, 8))
        for lines in range(0, linect):
            data[lines, 0] = sub_points[lines, 0]
            data[lines, 1] = sub_points[lines, 1]
            data[lines, 2] = sub_points[lines, 2]
            data[lines, 3] = sub_colors[lines, 0]
            data[lines, 4] = sub_colors[lines, 1]
            data[lines, 5] = sub_colors[lines, 2]
            data[lines, 6] = sub_labels[lines]
            #print(data)
            nextline = "{} {} {} {} {} {} {}\n"
            nextline = nextline.format(data[lines, 0], data[lines, 1],
                          data[lines, 2], data[lines, 3], data[lines, 4], data[lines, 5], data[lines, 6])
            plyfile.write(nextline)
    plyfile.close()
    return
            
