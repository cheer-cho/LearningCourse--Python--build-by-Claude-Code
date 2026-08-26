import logging
from io import StringIO

from ex05_logging import audit, make_logger


def test_make_logger_writes_formatted_line():
    stream = StringIO()
    logger = make_logger("ex05-app", logging.INFO, stream)
    logger.info("hello")
    assert stream.getvalue() == "INFO:ex05-app:hello\n"


def test_make_logger_respects_level():
    stream = StringIO()
    logger = make_logger("ex05-level", logging.WARNING, stream)
    logger.info("should not appear")
    logger.warning("should appear")
    assert stream.getvalue() == "WARNING:ex05-level:should appear\n"


def test_make_logger_does_not_propagate_to_root():
    stream = StringIO()
    logger = make_logger("ex05-noprop", logging.INFO, stream)
    assert logger.propagate is False


def test_make_logger_rebuild_does_not_duplicate_handlers():
    stream1 = StringIO()
    make_logger("ex05-rebuild", logging.INFO, stream1)
    stream2 = StringIO()
    logger = make_logger("ex05-rebuild", logging.INFO, stream2)
    logger.info("once")
    assert stream2.getvalue() == "INFO:ex05-rebuild:once\n"
    assert stream1.getvalue() == ""


def test_audit_ok_logs_info():
    stream = StringIO()
    logger = make_logger("ex05-audit-ok", logging.INFO, stream)
    audit(logger, "login", True)
    assert stream.getvalue() == "INFO:ex05-audit-ok:OK: login\n"


def test_audit_not_ok_logs_error():
    stream = StringIO()
    logger = make_logger("ex05-audit-fail", logging.INFO, stream)
    audit(logger, "login", False)
    assert stream.getvalue() == "ERROR:ex05-audit-fail:FAILED: login\n"
