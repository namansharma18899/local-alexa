#TODO: Should add a Listener for Audio, flask server with running svc endpoints
from services.service_pool import ServicePool



if __name__=="__main__":
    # Create a new service pool with predefined services and capacities
    service_pool = ServicePool(20)