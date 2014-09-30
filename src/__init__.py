
import sys
from genie_assignment.lib import semantic_server as utils
from tornado.testing import get_unused_port


if __name__ == "__main__":
    try:
        port = get_unused_port()
        print("Run server on %s port"%port)
        utils.start_semantic_ui_server(port)
    except:
        raise sys.exc_info()