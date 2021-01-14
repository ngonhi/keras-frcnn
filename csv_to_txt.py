'''
Convert csv file to txt file
csv format: filename, width, class, height, xmin, ymin, xmax, ymax, area
txt format: filename,x1,y1,x2,y2,class
'''

from optparse import OptionParser
parser = OptionParser()

parser.add_option('-c', '--csv', dest='csv_path')
parser.add_option('-t', '--txt', dest='txt_path')

(options, args) = parser.parse_args()

output = open(options.txt_path, 'w')
print('Start converting')
with open(options.csv_path, "rt", encoding='ascii') as f:
    next(f)
    for row in f:
        row = row.split(',')
        line = ','.join([row[0], row[4], row[5], row[6], row[7], row[3]])
        output.write(line)
        output.write('\n')
output.close()
print('Finish converting')