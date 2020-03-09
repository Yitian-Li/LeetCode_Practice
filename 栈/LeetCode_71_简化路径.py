class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        def partition(path):
            index = [r for r in range(len(path)) if path[r] == '/']
            num_index = len(index)
            ret = []
            if num_index == 0:
                ret.append("")
            elif num_index == 1 and index[0]==0:
                ret.append(path[index[0]+1:])
            else:
                for i in range(num_index-1):
                    ret.append(path[ index[i]+1 : index[i+1] ])
                ret.append(path[index[num_index-1]+1:])
            return ret

        class stack(object):
            def __init__(self):
                self.stack = []
            def push(self, valve):
                self.stack.append(valve)
            def pop(self):
                if self.stack:
                    return self.stack.pop()
                else:
                    pass
            def is_empty(self):
                return bool(self.stack)

            def retrun_path(self):
                ret = "/"
                stack_len = len(self.stack)
                if stack_len == 0:
                    return ret
                else:
                    for i in range(stack_len-1):
                        ret += self.stack[i]
                        ret += '/'
                    ret += self.stack[-1]
                    return ret


        def stack_process(sub_paths):
            ret = ""
            my_stack = stack()
            for sub_path in sub_paths:
                if sub_path == '.' or len(sub_path)==0:
                    pass
                elif sub_path == '..':
                    my_stack.pop()
                else:
                    my_stack.push(sub_path)
            return my_stack.retrun_path()
        
        # test = '/.'
        sub_paths = partition(path)
        out = stack_process(sub_paths)
        return out