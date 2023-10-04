# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 16:36
# @Author  : 4v1d
# @File    : dzdp-spider.py
# @Software: PyCharm
import re
import requests
import hashlib
import fontTools
from  fontTools.ttLib import TTFont

class Spider():
    def __init__(self):
        self.headers = {
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": "^\\^",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        cookies = {
            "_lxsdk_cuid": "1833a4550c0c8-018b8851c1a86f-977173c-144000-1833a4550c1c8",
            "_lxsdk": "1833a4550c0c8-018b8851c1a86f-977173c-144000-1833a4550c1c8",
            "_hc.v": "4144fc4d-d7ed-b9b2-005b-e128516031d0.1663129965",
            "fspop": "test",
            "s_ViewType": "10",
            "WEBDFPID": "30y1u8659v31562v1w0yv52xzy4589768164901z1x29795893350074-1978864525967-1663504525378KAESEIQfd79fef3d01d5e9aadc18ccd4d0c95077393",
            "Hm_lvt_602b80cf8079ae6591966cc70a3940e7": "1663129965,1663504441,1663512298,1663571050",
            "_lx_utm": "utm_source^%^3Dbing^%^26utm_medium^%^3Dorganic",
            "cy": "1",
            "cye": "shanghai",
            "Hm_lpvt_602b80cf8079ae6591966cc70a3940e7": "1663571750",
            "_lxsdk_s": "183548fbd44-f46-b85-453^%^7C^%^7C59"
        }
        url = "https://www.dianping.com/shanghai/ch1"
        self.res = requests.get(url, headers=self.headers, cookies=cookies)
        self.basefont_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '店', '中', '美', '家', '馆', '小', '车', '大', '市', '公', '酒',
                     '行', '国', '品', '发', '电', '金', '心', '业', '商', '司', '超', '生', '装', '园', '场', '食', '有', '新', '限', '天', '面',
                     '工', '服', '海', '华', '水', '房', '饰', '城', '乐', '汽', '香', '部', '利', '子', '老', '艺', '花', '专', '东', '肉', '菜',
                     '学', '福', '饭', '人', '百', '餐', '茶', '务', '通', '味', '所', '山', '区', '门', '药', '银', '农', '龙', '停', '尚', '安',
                     '广', '鑫', '一', '容', '动', '南', '具', '源', '兴', '鲜', '记', '时', '机', '烤', '文', '康', '信', '果', '阳', '理', '锅',
                     '宝', '达', '地', '儿', '衣', '特', '产', '西', '批', '坊', '州', '牛', '佳', '化', '五', '米', '修', '爱', '北', '养', '卖',
                     '建', '材', '三', '会', '鸡', '室', '红', '站', '德', '王', '光', '名', '丽', '油', '院', '堂', '烧', '江', '社', '合', '星',
                     '货', '型', '村', '自', '科', '快', '便', '日', '民', '营', '和', '活', '童', '明', '器', '烟', '育', '宾', '精', '屋', '经',
                     '居', '庄', '石', '顺', '林', '尔', '县', '手', '厅', '销', '用', '好', '客', '火', '雅', '盛', '体', '旅', '之', '鞋', '辣',
                     '作', '粉', '包', '楼', '校', '鱼', '平', '彩', '上', '吧', '保', '永', '万', '物', '教', '吃', '设', '医', '正', '造', '丰',
                     '健', '点', '汤', '网', '庆', '技', '斯', '洗', '料', '配', '汇', '木', '缘', '加', '麻', '联', '卫', '川', '泰', '色', '世',
                     '方', '寓', '风', '幼', '羊', '烫', '来', '高', '厂', '兰', '阿', '贝', '皮', '全', '女', '拉', '成', '云', '维', '贸', '道',
                     '术', '运', '都', '口', '博', '河', '瑞', '宏', '京', '际', '路', '祥', '青', '镇', '厨', '培', '力', '惠', '连', '马', '鸿',
                     '钢', '训', '影', '甲', '助', '窗', '布', '富', '牌', '头', '四', '多', '妆', '吉', '苑', '沙', '恒', '隆', '春', '干', '饼',
                     '氏', '里', '二', '管', '诚', '制', '售', '嘉', '长', '轩', '杂', '副', '清', '计', '黄', '讯', '太', '鸭', '号', '街', '交',
                     '与', '叉', '附', '近', '层', '旁', '对', '巷', '栋', '环', '省', '桥', '湖', '段', '乡', '厦', '府', '铺', '内', '侧', '元',
                     '购', '前', '幢', '滨', '处', '向', '座', '下', '県', '凤', '港', '开', '关', '景', '泉', '塘', '放', '昌', '线', '湾', '政',
                     '步', '宁', '解', '白', '田', '町', '溪', '十', '八', '古', '双', '胜', '本', '单', '同', '九', '迎', '第', '台', '玉', '锦',
                     '底', '后', '七', '斜', '期', '武', '岭', '松', '角', '纪', '朝', '峰', '六', '振', '珠', '局', '岗', '洲', '横', '边', '济',
                     '井', '办', '汉', '代', '临', '弄', '团', '外', '塔', '杨', '铁', '浦', '字', '年', '岛', '陵', '原', '梅', '进', '荣', '友',
                     '虹', '央', '桂', '沿', '事', '津', '凯', '莲', '丁', '秀', '柳', '集', '紫', '旗', '张', '谷', '的', '是', '不', '了', '很',
                     '还', '个', '也', '这', '我', '就', '在', '以', '可', '到', '错', '没', '去', '过', '感', '次', '要', '比', '觉', '看', '得',
                     '说', '常', '真', '们', '但', '最', '喜', '哈', '么', '别', '位', '能', '较', '境', '非', '为', '欢', '然', '他', '挺', '着',
                     '价', '那', '意', '种', '想', '出', '员', '两', '推', '做', '排', '实', '分', '间', '甜', '度', '起', '满', '给', '热', '完',
                     '格', '荐', '喝', '等', '其', '再', '几', '只', '现', '朋', '候', '样', '直', '而', '买', '于', '般', '豆', '量', '选', '奶',
                     '打', '每', '评', '少', '算', '又', '因', '情', '找', '些', '份', '置', '适', '什', '蛋', '师', '气', '你', '姐', '棒', '试',
                     '总', '定', '啊', '足', '级', '整', '带', '虾', '如', '态', '且', '尝', '主', '话', '强', '当', '更', '板', '知', '己', '无',
                     '酸', '让', '入', '啦', '式', '笑', '赞', '片', '酱', '差', '像', '提', '队', '走', '嫩', '才', '刚', '午', '接', '重', '串',
                     '回', '晚', '微', '周', '值', '费', '性', '桌', '拍', '跟', '块', '调', '糕']

    def get_css(self):
        css_url = re.findall('href="(.*s3plus.*)"',self.res.text)
        #拿到字体的url
        woff_html = requests.get('http:'+css_url[0],headers=self.headers)
        woff_url = ['http:'+url for url in re.findall(",url\(\"(.*?)\"\);}",woff_html.text)]
        #拿到字体的名字
        woff_name = re.findall('font-family: "PingFangSC-Regular-(.*?)";',woff_html.text)
        #将字体名字和url一一对应起来
        woff_name_url = {}
        for i in range(len(woff_name)):
            if woff_name[i] !=  'reviewTag': #这样处理的原因是本例中用不到reviewTag这个字体文件，并且它是重复的，所以去掉它。
                woff_name_url[woff_name[i]] = woff_url[i]
        for key in woff_name_url:
            name = key
            url = woff_name_url[key]
            self.response = requests.get(url,headers=self.headers)
            with open('%s.woff'%name,'wb') as f:
                f.write(self.response.content)
                f.close()
        fonts = {}
        for key in woff_name_url:
            file_name = '{}.woff'.format(key)
            fonts[key] = TTFont(file_name)
        return  fonts


    def address_Dict(self):
        # 假设我们用address作为基准字典
        address_font = TTFont('address.woff')
        unicodes = address_font.getGlyphOrder()[2:]
        # 上面说的basefont_char的顺序就是这个getGlyphOrder的顺序
        # 这里[2:]是因为前两个字符是没有用的，从上图也可以看出来
        base_dict = {}
        for i in range(len(unicodes)):
            contour = hashlib.md5(
                bytes(str(self.fonts['address']['glyf'][unicodes[i]].coordinates),
                      encoding='utf-8')).hexdigest()
            base_dict[contour] = self.basefont_char[i]
        self.address_dict = base_dict

    def tagName_Dict(self):
        # 假设我们用address作为基准字典
        tagName_font = TTFont('tagName.woff')
        unicodes = tagName_font.getGlyphOrder()[2:]
        font = self.get_css()
        # 上面说的basefont_char的顺序就是这个getGlyphOrder的顺序
        # 这里[2:]是因为前两个字符是没有用的，从上图也可以看出来
        base_dict = {}
        for i in range(len(unicodes)):
            contour = hashlib.md5(
                bytes(str(font['tagName']['glyf'][unicodes[i]].coordinates),
                      encoding='utf-8')).hexdigest()
            base_dict[contour] = self.basefont_char[i]
        self.tagdict = base_dict

    def shopName_Dict(self):
        # 假设我们用address作为基准字典
        shopName_font = TTFont('shopNum.woff')
        unicodes = shopName_font.getGlyphOrder()[2:]
        font = self.get_css()
        # 上面说的basefont_char的顺序就是这个getGlyphOrder的顺序
        # 这里[2:]是因为前两个字符是没有用的，从上图也可以看出来
        base_dict = {}
        for i in range(len(unicodes)):
            contour = hashlib.md5(
                bytes(str(font['shopNum']['glyf'][unicodes[i]].coordinates),
                      encoding='utf-8')).hexdigest()
            base_dict[contour] = self.basefont_char[i]
        self.shopdict = base_dict


    def get_tag(self):
        address_font = TTFont('tagName.woff')
        addrs = re.findall('<span class="tag">(.*?)</span>', self.res.text)
        base_dict = self.tagdict
        for i in addrs:
            addr = i.replace('<svgmtsi class="tagName">', '').replace(
                '</svgmtsi>', '')
            str_need_replace = re.findall('&#x(.*?);', addr)

            for i in str_need_replace:
                unicode = 'uni' + i  # 拿到这个字对应的Unicode编码
                contour_code = hashlib.md5(
                    bytes(str(address_font['glyf'][unicode].coordinates),
                          encoding='utf-8')).hexdigest()
                old_str = '&#x' + i + ';'
                new_str = base_dict[contour_code]
                addr = addr.replace(old_str, new_str)
            print(addr)  # 长春西路60号

    def get_appraise(self):

        address_font = TTFont('shopNum.woff')
        addrs = re.findall('<svgmtsi class="shopNum">(.*?)</svgmtsi>', self.res.text)
        print(addrs)
        base_dict = self.shopdict
        for i in addrs:
            addr = i.replace('<svgmtsi class="shopNum">', '').replace(
                '</svgmtsi>', '')
            str_need_replace = re.findall('&#x(.*?);', addr)

            for i in str_need_replace:
                unicode = 'uni' + i  # 拿到这个字对应的Unicode编码
                contour_code = hashlib.md5(
                    bytes(str(address_font['glyf'][unicode].coordinates),
                          encoding='utf-8')).hexdigest()
                old_str = '&#x' + i + ';'
                new_str = base_dict[contour_code]
                addr = addr.replace(old_str, new_str)
            print(addr)  # 长春西路60号

    def get_prcie(self):
        font = self.get_css()
        base_dict = self.shopdict
        # 人均消费价格的提取
        # 人均消费价格由于有缺失值，所以需要单独处理
        avgprices_nodes = re.findall('shop_avgprice_click(.*?)<b>(.*?)</b>',
                                     self.res.text, flags=re.S)
        print(avgprices_nodes)
        avg_prices = []
        for i in range(len(avgprices_nodes)):
            if '￥' in avgprices_nodes[i][1]:
                avg_price = avgprices_nodes[i][1].replace(
                    '<svgmtsi class="shopNum">', '').replace('</svgmtsi>', '')
                str_need_replace = re.findall('&#x(.*?);', avg_price)
                for j in str_need_replace:
                    unicode = 'uni' + j
                    contour_code = hashlib.md5(bytes(
                        str(font['shopNum']['glyf'][unicode].coordinates),
                        encoding='utf-8')).hexdigest()
                    old_str = '&#x' + j + ';'
                    new_str = base_dict[contour_code]
                    avg_price = avg_price.replace(old_str, new_str)
                avg_prices.append(int(avg_price.strip('￥')))
            else:
                avg_prices.append('-')
            print(avg_price)



if __name__ == '__main__':
    s = Spider()
    s.get_css()
    # s.tagName_Dict()
    # s.get_tag()
    s.shopName_Dict()
    # s.get_appraise()
    s.get_prcie()
