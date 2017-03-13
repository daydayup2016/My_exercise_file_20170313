import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s-->line:%(lineno)s - %(levelname)s - %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    # datefmt='%Y-%m-%d %Y %H:%M:%S',
                    filename='12345.txt',
                    filemode='w'
                    )