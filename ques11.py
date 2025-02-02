#Create a class `Logger` with a method `log(message)`. 
# Implement method overloading to log different message types (`error`, `warning`, `info`)

class Logger:
    def log(self, message, message_type="info"):
        if message_type == "error":
            self._log_error(f'ERROR: {message}')
        elif message_type == "warning":
            self._log_warning(f'WARNING: {message}')
        else:
            self._log_info(f'INFO: {message}')

    def _log_error(self, message):
        print(message)

    def _log_warning(self, message):
        print(message)

    def _log_info(self, message):
        print(message)

l = Logger()
l.log("This is an info message")         
l.log("This is a warning message", "warning")  
l.log("This is an error message", "error") 
