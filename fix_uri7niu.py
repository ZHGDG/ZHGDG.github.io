# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''自动批量修改因 7niu CDN 域名变更引发的图片引用失效问题
- 目前只能指定目录, 修改目录中所有 .md
- 将来看情况是否复杂到值得交互式指定目录/替换 URI 之类...

190326 for blog.zhgdg.org
'''
import os
import sys

def fixall(p2md):
    print p2md
    #print os.listdir(p2md)
    for md in os.listdir(p2md):
        _page = '%s/%s'% (p2md,md)
        _remd = ''
        for line in open(_page,'r').readlines():
            #print line

            if "http://zoomq.qiniudn.com/" in line:
                print line,"\n==>"
                _rel = line.replace('](http://zoomq.qiniudn.com/'
                                    , '](http://0.zoomquiet.top/')
                #print "{} \n==>\n {}".format(line, _rel)
                print _rel
                _remd += _rel
            else:
                _remd += line
        open(_page,'w').write(_remd)
        print "fixed -> %s "% _page

if __name__ == '__main__':
    if 2 != len(sys.argv) :
        print '''Usage:
fix_uri7niu.py /path/2/原文章目录
        '''
    else:
        startPath = sys.argv[1]
        fixall(startPath)
        print "fixall -> %s "% startPath


