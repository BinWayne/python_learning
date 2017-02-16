import urllib2
class HtmlDownloader(object):
	
	
	
	def download(self,url):
		print 'start download'
		if url is None:
			return None
		response = urllib2.urlopen(url)
		print response.getcode()
		if response.getcode() != 200:
			return None
		return response.read()