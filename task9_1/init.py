import logging
import properties


def setup_logger():

    logging.basicConfig(level=logging.INFO,
                        filename=properties.LOG_FILE,
                        filemode="w",
                        format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # set a format which is simpler for console use
    formatter = logging.Formatter(fmt='[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)