def guarded_process(data, log):
    log.append("start")
    result = None
    try:
        result = 100 / data["divisor"]
    except (KeyError, ZeroDivisionError):
        log.append("error")
        return None
    else:
        log.append("ok")
        return result
    finally:
        log.append("cleanup")
