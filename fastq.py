#! /usr/bin/env python

import sys, csv

fastq_in = open(sys.argv[1])

length_thresh = 150

fastq_list = []

line = True
while line:
    lines = []
    for i in range(4):
	line = fastq_in.readline().strip()
        if line: lines.append(line)
    if not lines: break
    fastq_dict = {}
    record = '\t'.join(lines)
    fastq_dict['seq_id'] = record.split('\t')[0]
    fastq_dict['seq'] = record.split('\t')[1]
    fastq_dict['seq_id2'] = record.split('\t')[2]
    fastq_dict['quality'] = record.split('\t')[3]
    fastq_list.append(fastq_dict)
    #print len(seq) #, quality 
    #break
    #if len(seq) < length_thresh:
    #    continue
    #else:
for i in fastq_list:
    print i.get('seq_id')
