import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def _vline(obj):
	if not obj:
		return
	plt.axvline(obj['pos'], color='black', linestyle='--', marker=0, linewidth=5)
	plt.annotate(obj['msg'], 
	             xy=obj['xy'], 
	             xytext=obj['xytext'],
	             arrowprops=dict(facecolor='black', shrink=2))

def _hline(obj):
	if not obj:
		return
	plt.axhline(obj['pos'], color='black', linestyle='--', marker=0, linewidth=3)
	plt.annotate(obj['msg'], 
	             xy=obj['xy'], 
	             xytext=obj['xytext'],
	             arrowprops=dict(facecolor='black', shrink=2))


def _labels(
		title=None,
		xlabel=None,
		ylabel=None
	):

	plt.title(title, fontdict={'size': 20})
	plt.xlabel(xlabel, fontdict={'size': 15})
	plt.ylabel(ylabel, fontdict={'size': 15})


def plot_hist(
			data=None,
			num_bins=None,
			num_y_ticks=None,
			title=None,
			xlabel=None,
			ylabel=None,
			hline=None
		):
	num_trials = len(data)
	obj = plt.hist(data, bins=num_bins,
        edgecolor='black', linewidth=1.5)
	plt.xticks(
		ticks=obj[1].tolist(), 
		labels=list(map(lambda x: '{:.1f}'.format(x), obj[1].tolist())), 
		rotation=90)
	plt.yticks(ticks=range(num_trials//num_y_ticks,num_trials+num_trials//num_y_ticks, num_trials//num_y_ticks), 
	           labels=range(100//num_y_ticks,100+100//num_y_ticks, 100//num_y_ticks))
	plt.grid(True, axis='y')

	_hline(hline)
	_labels(title=title, xlabel=xlabel, ylabel=ylabel)

def plot_bar(
		data=None,
		num_y_ticks=None,
		title=None,
		xlabel=None,
		ylabel=None,
		hline=None
	):
	num_trials = len(data)
	_temp = Counter(data)

	obj = plt.bar(_temp.keys(), _temp.values(),
        edgecolor='black', linewidth=1.5)

	plt.yticks(ticks=range(num_trials//num_y_ticks,num_trials+num_trials//num_y_ticks, num_trials//num_y_ticks), 
	           labels=range(100//num_y_ticks,100+100//num_y_ticks, 100//num_y_ticks))
	plt.grid(True, axis='y')

	_hline(hline)
	_labels(title=title, xlabel=xlabel, ylabel=ylabel)

def plot_line(
		data=None,
		title=None,
		xlabel=None,
		ylabel=None,
		hline=None
	):
	num_trials = len(data)
	plt.plot(range(num_trials), data, '-')
	_hline(hline)
	_labels(title=title, xlabel=xlabel, ylabel=ylabel)
	plt.grid(True)
