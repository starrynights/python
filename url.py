import urllib


#v1
#######################################################
#content = urllib.urlopen("http://www.baidu.com"
#print "header: ", content.info()
#print "status: ", content.getcode()
#print "url: ", content.geturl()
#print "content: "
#for line in content.readlines():
#    print line

#######################################################

#v2
#######################################################
"""download file and show process"""
def down_call(count, size, total_filesize):
    print count, size, total_filesize
    per = 100 * count * size / total_filesize
    if per > 100:
        per = 100
    print "Already download %d KB, %.2f " % (size * count / 1024, per),"%"

url = "http://www.baidu.com"
local_path = "./download"
urllib.urlretrieve(url,local_path,down_call)
#######################################################
