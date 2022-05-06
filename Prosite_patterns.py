from Bio import SeqIO
from Bio.ExPASy import ScanProsite
import re
import requests
import time
import csv

# Read Input File
#Input fasta file
def readInputFile():
    with open('Sequence1.fasta', 'r+') as sequence_file:
        sequences = sequence_file.read()
    count=0
    sequences = sequences.split('>')[1:]
    outputCSVFile(sequences)

def writeLogFile(sequence,status):
    with open('log.txt', 'a+') as logdata:
        log =sequence+"\t"+status+"\n"
        print(log)
        logdata.write(log)


def outputCSVFile(sequences):
    #Output CSV file name
    with open("sequence_pattern_new.csv","a+",newline='') as pattern_file:
        for record in sequences[1:]:
            try:
                uniprotId = re.search(r"(?<=\|).+?(?=\|)",record)
                protId=uniprotId.group()
                print("Currently working on:"+uniprotId.group())
                newline = []
                rec = re.sub(r".*\d\n","",record)
                rec = rec.replace("\n","")
                #extract records for each sequence
                handle = ScanProsite.scan(seq=record, noprofile=1)
                res = ScanProsite.read(handle)
                print(res)
                newline.append(protId)
                newline.append(rec)
                for i in range(0,len(res)):
                    #separating signatures from the extracted records
                    sig = res[i]['signature_ac']
                    #make the url for the signature to extract the corresponding consensus patterns
                    url ='https://prosite.expasy.org/{0}.txt'.format(sig)
                    print(url)
                    response = requests.get(url)
                    try:
                        print(response)
                        content = str(response.text)
                        patterns = re.findall("(\nPA)(.*)(\.\n)?",content)
                        pattern =""
                        for i in range(len(patterns)):
                            pattern = pattern + patterns[i][1].strip()
                            pattern = pattern.replace(".","")
                        print(newline)
                        newline.append(pattern)
                    except:
                        writeLogFile(protId+"\t"+url,"ServerError")
                writer = csv.writer(pattern_file)
                writer.writerow(newline)
                writeLogFile(protId,"Successful")
                time.sleep(2)
            except:
                writeLogFile(protId,"UnSuccessful")
                time.sleep(2)
                continue


readInputFile()
