class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        
        # Path ko '/' ke basis par split karenge
        components = path.split('/')
        
        for portion in components:
            # Agar empty string hai ya '.' hai, toh ignore karenge
            if portion == "" or portion == ".":
                continue
            # Agar '..' hai, toh ek step piche jaane ke liye pop karenge
            elif portion == "..":
                if stack:
                    stack.pop()
            # Baki kisi bhi valid naam ko stack mein add karenge
            else:
                stack.append(portion)
                
        # Last mein stack ke elements ko '/' se join karke return karenge
        return "/" + "/".join(stack)