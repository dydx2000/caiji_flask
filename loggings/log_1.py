import logging

logging.basicConfig (
    filename='log1.log',
    level=logging.ERROR,
                     format='%(asctime)s -%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

a = 2

# if a ==1:
#     logging.info("这时可以输出日志")

if a == 3:
    logging.info ("输出警告信息")

if a == 2:
    logging.error("出现了错误喔.")
else:
    logging.critical ("出现了很严重的故障喔.")
logging.info ('I am info')
logging.debug ('I am debug')
logging.warning ('I am warning')
logging.critical ('I am critical')
