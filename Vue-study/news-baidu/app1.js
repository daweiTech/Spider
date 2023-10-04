const http = require('http')
const https = require('https')
const cheerio = require('cheerio');

// 筛选数据
const filterData = (data) => {
  const $ = cheerio.load(data);
  const filterDataArr = []
  const arr = $('.section-phone-box .section-box-row .index-center-wrapper ul li')
  arr.each((index, el) => {
    console.log(index);
    const goodsName = $(el).find('.goods-name').text()
    const description = $(el).find('.goods-desc').text()
    const price = $(el).find('.goods-price').text()
    const goodsImg = $(el).find('.goods-img').data('src')
    const good = {
      goodsName,
      description,
      price,
      goodsImg,
    }
    filterDataArr.push(good)
  })
  console.log(filterDataArr);
}

const server = http.createServer((request, response) => {
  let data = ''
  https.get('https://www.meizu.com', (result) => {
    result.on('data', chunk => {
      data += chunk
    })
    result.on('end', () => {
      filterData(data)
    })
  })
})

server.listen(8080, () => {
  console.log('localhost:8080');
})
