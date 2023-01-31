import bot_controller as controller
import logging
import properties

logging.basicConfig(level=logging.INFO, filename=properties.LOG_FILE, filemode="w")

controller.start()
