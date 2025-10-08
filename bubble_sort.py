def bubblesort(values):

    for i in range(len(values)):
        # outer_pass += 1
        for j in range(len(values) -i - 1):
            # inner_pass += 1
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values
