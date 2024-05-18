def chunk(array, size):
    chunked = []
    index = 0
    while (index < len(array)):
        chunked.append(array[index:index + size])
        index += size
    return chunked