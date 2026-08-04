class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, status, timestamp_str = log.split(':')
            fn_id = int(fn_id_str)
            timestamp = int(timestamp_str)

            if status == "start":
                # Agar pehle se koi function stack par chal raha tha
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                # Function execution end ho raha hai
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res