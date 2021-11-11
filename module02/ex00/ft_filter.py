def ft_filter(function_to_apply, list_of_inputs):
	lst = []
	for x in list_of_inputs:
		if function_to_apply(x):
			lst.append(x)
	return lst