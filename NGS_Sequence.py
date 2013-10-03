
class NGSSequence:
	def __init__(self,id_string,sequence,quality):
		self.id_string=id_string
		self.sequence=list(sequence)
		self.quality=list(quality)
	'''trim function will trim sequence based on the length of sequence
	   and a quality threshold
	'''
	def trim(self,win_width,threshold):
		if win_width==1:
			self.check_1(threshold)
		#no time to finish this part 
		else:
			self.check_1(threshold)
	def window_width(self):
		if len(self.sequence)<=10: return 1
		else: return 1+len(self.sequence)/10
	'''check_1 funciton will check each base one by one and replace
	   the base which is under threshold
	'''
	def check_1(self,threshold):
		i=0
		while i < len(self.sequence):
			if ord(self.quality[i])-64<threshold:
				self.sequence[i]=' '
			i+=1
	#no time to finish this part
	def check_2(self):
		pass
