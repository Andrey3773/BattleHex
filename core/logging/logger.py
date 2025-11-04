import logging


class Logger:

    def __init__(self, name=__name__, level=logging.INFO):
        logging.basicConfig(
            level=level,
            format='%(asctime)s: %(name) %(message)s',
            datefmt='%H:%M:%S'
        )

        self.logger = logging.getLogger(name)

        root_logger = logging.getLogger()
        for handler in root_logger.handlers:
            handler.setFormatter(Formatter())


    def info(self, message):
        self.logger.info(message)


    def warning(self, message):
        self.logger.warning(message)


    def error(self, message):
        self.logger.error(message)


    def debug(self, message):
        self.logger.debug(message)


class Formatter(logging.Formatter):
    def format(self, record):
        total_width = 50
        around_dash_place = 5

        logger_name = record.name

        # время: "HH:MM:SS" (8 символов) + ": " (2 символа) = 10 символов
        time_part_length = 10
        name_length = len(logger_name)

        dash_quantity = total_width - time_part_length - name_length - around_dash_place

        # Создаем разделитель динамической длины
        separator = ' ' * 3 + '-' * dash_quantity + ' ' * 2

        formatted_message = f"{logger_name}{separator}{record.getMessage()}"

        result = f"{self.formatTime(record, self.datefmt)}: {formatted_message}"

        return result
