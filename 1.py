import re
import jieba
import matplotlib.pyplot as plt
import wordcloud
import imageio
from scipy.misc import imread
f = open('/Users/Administrator/Desktop/萝北(1832333945).txt' , 'r', encoding = 'utf-8')
f1 = f.readlines()
del f1[:8]
f1= f1[1::3]
strf = ''.join(f1)
list1 = re.findall(r'/.{2,3}', strf)
list2 = re.findall(r'\[.+?\]', strf)
set1 = set(list1)
set2 = set(list2)
for item in set1:
    strf = strf.replace(item, '')
for item in set2:
    strf = strf.replace(item, '')
strf = strf.replace('请使用最新版本手机QQ查看', '')
strf = strf.replace('请使用最新版手机QQ体验新功能', '')
strf = strf.replace('哈哈', '')
strf = strf.replace('fork', '')
strf = strf.replace('哈哈哈', '')
word_list = jieba.cut(strf, cut_all=True)
word = ' '.join(word_list)
pic = imageio.imread('/Users/Administrator/Desktop/xin.jpg')
wc = wordcloud.WordCloud(mask=pic, font_path='/Users/Administrator/Desktop/msyhttc_downcc/msyh.ttc', width=1000, height=500, background_color='white',).generate(word)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
wc.to_file('result.jpg')