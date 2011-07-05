import logging
from flexmock import flexmock
from should_dsl import should, matcher
from should_dsl.matchers import equal_to


@matcher
class LogMatcher(object):
    # pylint: disable=R0903
    """A should-dsl matcher that checks whether a log
    entry is being made at a certain log level.

    Additional Dependency:
        flexmock: <http://pypi.python.org/pypi/flexmock>
    
    Example:
        import unittest
        logging.basicConfig()
        logger = logging.getLogger('some.logger')
    
        def log_something():
            logger.error('A log message')
    
        class LogTest(unittest.TestCase):
            def test_log_something(self):
                logger | should | log('CRITICAL', 'A log message')
                log_something() # Will throw an exception because the log message
                                # has level 'ERROR' and not 'CRITICAL' as expected.
    
        suite = unittest.TestLoader().loadTestsFromTestCase(LogTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
    """

    name = 'log'

    def __init__(self):
        self._expected_level = ''
        self._expected_message = ''

    def __call__(self, expected_level, expected_message):
        self._expected_level = expected_level
        self._expected_message = expected_message
        return self

    def match(self, logger):
        """Implement should_dsl's match() method."""

        handler = flexmock(logging.Handler())
        def emit(record):
            """Hooks into the log handler."""
            try:
                # pylint: disable=E1121,W0106
                record.levelname | should | equal_to(self._expected_level)
                record.msg | should | equal_to(self._expected_message)
            finally:
                logger.removeHandler(handler)
        handler.should_receive('emit').replace_with(emit).once()
        logger.addHandler(handler)
        # Always return true and let flexmock take care of
        # actual matching.
        return True


if __name__ == '__main__':
    import unittest
    logging.basicConfig()
    logger = logging.getLogger('some.logger')

    def log_something():
        logger.error('A log message')

    class LogTest(unittest.TestCase):
        def test_log_something(self):
            logger | should | log('CRITICAL', 'A log message')
            log_something() # Will throw an exception because the log message
                            # has level 'ERROR' and not 'CRITICAL' as expected.

    suite = unittest.TestLoader().loadTestsFromTestCase(LogTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

