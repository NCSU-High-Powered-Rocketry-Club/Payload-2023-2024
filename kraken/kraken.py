from enum import Enum, auto
import time
from .servoutils import PwmDriver


class LaunchState(Enum):
    STANDBY = auto()
    ARMED = auto()
    DEPLOYED = auto()
    FLARE = auto()
    RECOVER = auto()


class PayloadSystem:

    # Don't deploy until this altitude is reached
    MAX_DEPLOY_ALTITUDE = 790

    def __init__(self):

        self.state = LaunchState.STANDBY

        self.init_time = time.time()

        self.ready_to_shutdown = False

    def update(self):

        currentState = self.state

        if currentState is LaunchState.STANDBY:
            # Do standby stuff
            pass

        elif currentState is LaunchState.ARMED:
            # The receiver has been switched, get ready to deploy
            pass

        elif currentState is LaunchState.DEPLOYED:
            # Deploy / spin motors
            pass

        elif currentState is LaunchState.FLARE:
            # Flare up speed before landing
            pass

        else:
            # Should be in recover mode, shutdown in main
            self.ready_to_shutdown = True
            pass

    def shutdown(self):
        # Cleanup any running threads here
        pass
