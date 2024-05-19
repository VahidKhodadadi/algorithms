def chunk(array, size):
    chunked = []
    index = 0
    while (index < len(array)):
        chunked.extend(array[index:index + size])
        index += size
    return chunked