from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.stack = defaultdict(list)
        self.max_freq = 0
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.stack[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        val = self.stack[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.stack[self.max_freq]:
            self.max_freq -= 1

        return val


# m = FreqStack()