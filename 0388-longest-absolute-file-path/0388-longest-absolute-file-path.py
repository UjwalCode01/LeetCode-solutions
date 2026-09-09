class Solution(object):
    def lengthLongestPath(self, input):
        max_len = 0
        # Map depth to the total path length up to that depth
        # depth -1 initialized to -1 so the root path doesn't add an extra '/' prefix length
        path_len = {-1: -1}

        for line in input.split('\n'):
            # Depth corresponds to the number of tab characters
            depth = line.count('\t')
            # Extract actual folder/file name
            name = line.lstrip('\t')

            # Cumulative length = parent path length + name length + 1 (for '/')
            path_len[depth] = path_len[depth - 1] + len(name) + 1

            # If it's a file, check if it forms a new maximum length
            if '.' in name:
                max_len = max(max_len, path_len[depth])

        return max_len