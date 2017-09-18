import logging

def foo(n):
    try:
        print('try...')
        r = 10 / int(n)
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
        raise ValueError('invalid value: %s' % n)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
        raise
    else:
        print('no error!')
    finally:
        print('finally...')


foo('2')

try:
    foo('0')
except BaseException as e:
    print('catch raise')
    logging.exception(e)

print('END')

try:
    foo('a')
except BaseException as e:
    print('catch raise')
    logging.exception(e)

print('END END')