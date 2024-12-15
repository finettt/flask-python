import multiprocessing
import logging

def pre_request(worker, req):
    logging.info("[%s:%s] %s: %s" % (req.remote_addr[0], req.remote_addr[1], req.method, req.path))
    for k, v in req.headers:
        logging.info("[%s:%s] %s: %s" % (req.remote_addr[0], req.remote_addr[1], k, v))

bind = "127.0.0.1:8000"

max_requests = 1000
max_requests_jitter = 50
log_file = "-"
#workers =  multiprocessing.cpu_count() * 2 + 1