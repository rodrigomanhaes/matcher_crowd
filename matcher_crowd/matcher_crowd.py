from should_dsl import matcher

@matcher
def have_the_same_elements_as():
    def have_same(actual, expected):
        for element in actual:
            if element not in expected:
                return False
        return len(actual) == len(expected)
    return (have_same, '%r does %shave the same elements as %r')

