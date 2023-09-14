from main import *

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 52
	assert work_calc(20, 3, 2) == 473
	assert work_calc(30, 4, 2) == 1808
	# new assertions
	assert work_calc(8, 2, 2) == 48
	assert work_calc(9, 3, 2) == 147
	assert work_calc(15, 3, 2) == 171

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 31
	assert work_calc(20, 1, 2, lambda n: n*n) == 531
	assert work_calc(30, 3, 2, lambda n: n) == 573

	# constant
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(100, 2, 2, lambda n: 1) == 127
	assert work_calc(1000, 2, 2, lambda n: 1) == 1023

    # logarithmic
	assert work_calc(10, 2, 2, lambda n: log(n)) == 174
	assert work_calc(100, 2, 2, lambda n: log(n)) == 19580
	assert work_calc(1000, 2, 2, lambda n: log(n)) == 1990744

	# linear
	assert work_calc(10, 2, 2, lambda n: n) == 36
	assert work_calc(100, 2, 2, lambda n: n) == 652
	assert work_calc(1000, 2, 2, lambda n: n) == 9120

def curry_work_calc(a, b, f):
	return lambda n: work_calc(n, a, b, f)

def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
    
	# create work_fn1
	work_fn1 = curry_work_calc(3, 2, lambda n: 1)
	# create work_fn2
	work_fn2 = curry_work_calc(4, 2, lambda n: n**2)

	result = compare_work(work_fn1, work_fn2)
	print_results(result)

def curry_span_calc(a, b, f):
	return lambda n: span_calc(n, a, b, f)

def test_compare_span():
	assert span_calc(10, 2, 2, lambda n: 1) == 4
	assert span_calc(20, 1, 4, lambda n: n * n) == 426
	assert span_calc(30, 3, 4, lambda n: n) == 38

	# create span_fn1
	span_fn1 = curry_span_calc(2, 2, lambda n: 1)

	# create span_fn2
	span_fn2 = curry_span_calc(2, 2, lambda n: n ** 2)

	result = compare_span(span_fn1, span_fn2)
	print_results(result)


