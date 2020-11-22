#!/usr/bin/python3

class CsvReader():
	def __init__(self, filename=None, sep=',', header=True, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
	
	def __enter__(self):
		self.f = open(self.filename)
		if (self.f is None):
			return None
		self.lines = self.f.readlines()
		self.data = []
		start = self.skip_top
		if self.header is True:
			self.header = self.lines[0].split(self.sep)
			start += 1
		end = len(self.lines) - self.skip_bottom
		maxlen = len(self.lines[0].split(self.sep))
		for i in range(start, end):
			self.data.append(self.lines[i].split(self.sep))
			for elems in self.lines[i].split(self.sep):
				if len(elems) < maxlen:
					return None
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		self.f.close()
	
	def getdata(self):
		return self.data

	def getheader(self):
		return self.header
