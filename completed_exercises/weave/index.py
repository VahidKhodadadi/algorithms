from queue import Queue

def weave(sourceOne, sourceTwo):
  q = Queue()

  while (sourceOne.peek() or sourceTwo.peek()):
    if (sourceOne.peek()):
      q.add(sourceOne.remove())

    if (sourceTwo.peek()):
      q.add(sourceTwo.remove())

  return q