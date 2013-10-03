class FASTQ:
    
    def __init__(self, fastq_filename):
        fastq_list = []
        self.parse_file(fastq_filename)
  
    def parse_file(self, file_name):
        try:
            print "Opening ",file_name
            fastq_in = open(file_name)
            line=True
            while line:
                lines = []
                for i in range(4):
                    line = fastq_in.readline().strip()
                    print "Read line ",line
                    if line: lines.append(line)
                if not lines: break
                fastq_dict={}	
                record = '\t'.join(lines)
                fastq_dict['seq_id'] = record.split('\t')[0]
                fastq_dict['seq'] = record.split('\t')[1]
                fastq_dict['seq_id2'] = record.split('\t')[2]
                fastq_dict['quality'] = record.split('\t')[3]
                fastq_list.append(fastq_dict)
                print "After append ",fastq_list
                #fastq_in.close()
                print "After close dict is ",fastq_dict
        except:
            print "Exception caught"
    
    def print_oneline(self):
        print "print_oneline"
       
    def print_fourline(self):
        print "print_fourline"
       
