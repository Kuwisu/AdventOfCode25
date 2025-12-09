# Fun fact: If I used the Part 1 approach to solve Part 2, it would have called moveBeam upwards of 2.14675735e15 times

def countAllTimelines(rows, start):
    """
    Conduct a breadth-first search of the tachyon manifold to count the number of timelines that the beam can be in.
    This is done by updating a list of timeline counts, adding the value of the current timeline to adjacent columns
    for every splitter encountered.

    :param rows: a list of strings representing the tachyon manifold
    :param start: the starting column of the beam
    :return: the sum of all timelines that the beam can be in
    """
    # Initialise timeline count with 1 timeline counted in the starting location
    timelines = [0]*start + [1] + [0]*(len(rows[0]) - start - 1)
    for row in rows[1:]:
        for i in range(len(row)):
            if row[i] == "^":
                current_timelines = timelines[i]
                timelines[i+1] += current_timelines
                timelines[i-1] += current_timelines
                timelines[i] = 0

    return sum(timelines)
