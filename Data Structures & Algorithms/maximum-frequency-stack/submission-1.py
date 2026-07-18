class FreqStack:

    def __init__(self):
        self.stack_freq = []
        self.freq_map = {}

    def push(self, val: int) -> None:
        #print(self.stack_freq, self.freq_map)
        freq = 0
        if val in self.freq_map:
            freq = self.freq_map[val]
            self.freq_map[val] += 1
        else:
            self.freq_map[val] = 1

        #print(freq)
        if len(self.stack_freq)< freq+1:
            self.stack_freq.append([val])
        else:
            self.stack_freq[freq].append(val)

    def pop(self) -> int:
        #print(self.stack_freq, self.freq_map)
        highest_freq_stack = self.stack_freq[len(self.stack_freq)-1]
        res = highest_freq_stack.pop()
        if not highest_freq_stack:
            self.stack_freq.pop()
        self.freq_map[res] -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()