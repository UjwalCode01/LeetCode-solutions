class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for token in path.split('/'):
            if token == '..':
                if stack:
                    stack.pop()
            elif token and token != '.':
                stack.append(token)
        return '/' + '/'.join(stack)