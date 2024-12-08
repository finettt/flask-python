import multiprocessing
import logging

def pre_request(worker, req):
    logging.info("%s: %s" % (req.method, req.path))

bind = "127.0.0.1:8000"

max_requests = 1000
max_requests_jitter = 50

log_file = "-"
# workers =  multiprocessing.cpu_count() * 2 + 1