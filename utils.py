import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def rollling_avg(arr):
    cumsum = np.cumsum(arr, axis=0)
    lengths = np.repeat(np.arange(1,arr.shape[0]+1, 1).reshape(1,-1), arr.shape[1], axis=0).T
    return cumsum/lengths


def vline_(obj):
	if not obj:
		return
	plt.axvline(obj['pos'], color='black', linestyle='--', marker=0, linewidth=2)
	plt.annotate(obj['msg'], 
	             xy=obj['xy'], 
	             xytext=obj['xytext'],
	             arrowprops=dict(facecolor='black', shrink=2))

def hline_(obj):
	if not obj:
		return
	plt.axhline(obj['pos'], color='black', linestyle='--', marker=0, linewidth=2)
	plt.annotate(obj['msg'], 
	             xy=obj['xy'], 
	             xytext=obj['xytext'],
	             arrowprops=dict(facecolor='black', shrink=2))


def labels(
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
			hline=None,
			rotate=False,
			x_range=None
		):
	num_trials = len(data)
	obj = plt.hist(data, bins=num_bins, range=x_range,
        edgecolor='black', linewidth=1.5, orientation='horizontal' if rotate else 'vertical')
	if not rotate:
		plt.xticks(
			ticks=obj[1].tolist(), 
			labels=list(map(lambda x: '{:.1f}'.format(x), obj[1].tolist())), 
			rotation=90)
		plt.yticks(ticks=range(num_trials//num_y_ticks,num_trials+num_trials//num_y_ticks, num_trials//num_y_ticks), 
		           labels=range(100//num_y_ticks,100+100//num_y_ticks, 100//num_y_ticks))
		plt.grid(True, axis='y')
	else:
		plt.yticks(
			ticks=obj[1].tolist(), 
			labels=list(map(lambda x: '{:.0f}'.format(x), obj[1].tolist())), 
			rotation=30)
		plt.xticks(ticks=range(num_trials//num_y_ticks,num_trials+num_trials//num_y_ticks, num_trials//num_y_ticks), 
		           labels=range(100//num_y_ticks,100+100//num_y_ticks, 100//num_y_ticks))
		plt.grid(True, axis='x')

	hline_(hline)
	labels(title=title, xlabel=xlabel, ylabel=ylabel)

def plot_bar(
		data=None,
		num_trials=None,
		num_y_ticks=10,
		title=None,
		xlabel=None,
		ylabel=None,
		hline=None,
		cap=1
	):
	if not num_trials:
		num_trials = len(data)
		_temp = Counter(data)
	else:
		_temp = data

	obj = plt.bar(_temp.keys(), _temp.values(),
        edgecolor='black', linewidth=1.5, tick_label=list(_temp.keys()))

	num_trials = int(cap*num_trials)

	plt.yticks(ticks=range(num_trials//num_y_ticks,num_trials+num_trials//num_y_ticks, num_trials//num_y_ticks), 
	           labels=range(int(100*cap)//num_y_ticks,int(100*cap)+int(100*cap)//num_y_ticks, int(100*cap)//num_y_ticks))
	plt.grid(True, axis='y')

	hline_(hline)
	labels(title=title, xlabel=xlabel, ylabel=ylabel)

def plot_line(
		data=None,
		title=None,
		xlabel=None,
		ylabel=None,
		hline=None,
		vline=None,
		thickness=1,
		label=None
	):
	num_trials = len(data)
	line = plt.plot(range(num_trials), data, '-', linewidth=thickness, label=label)
	hline_(hline)
	vline_(vline)
	labels(title=title, xlabel=xlabel, ylabel=ylabel)
	plt.grid(True)
	return line
