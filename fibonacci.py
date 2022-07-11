import time


class Fib:
    def __init__(self):
        self.lookup = {0: 0, 1: 1}
        self.largest_known = [1, 1]

    # gets the nth term of the fibonacci sequence
    def get_nth_term(self, n):
        # checks to see if we already have the nth term
        if n in self.lookup:
            return self.lookup[n]
        # we don't already have the nth term
        else:
            # loop from the largest known index to nth term
            for i in range(self.largest_known[0], n + 1):
                # if the term is not already in the lookup table, calculate it
                if i not in self.lookup:
                    self.lookup[i] = self.lookup[i - 1] + self.lookup[i - 2]
                    # update the largest known index and term
                    if self.lookup[i] > self.largest_known[1]:
                        self.largest_known = [i, self.lookup[i]]
        return self.lookup[n]

    # prints all terms of sequence up to and including n
    def print_sequence(self, n=0):
        if n not in self.lookup:
            self.get_nth_term(n)
        x = n if n > 0 else self.largest_known[0]
        for i in range(x + 1):
            print(self.lookup[i])
        return

    # prints the nth fib term
    def print_nth(self, n=0):
        if n not in self.lookup:
            self.get_nth_term(n)
        print(self.lookup[n])

    def write_to_file(self):
        f = open("fibonacci.txt", "w")
        for i in range(self.largest_known[0]):
            f.write(
                f"{str(self.lookup[i])}"
                if i == self.largest_known
                else f"{str(self.lookup[i])}\n"
            )
        f.close()


fib = Fib()
# fib.print_nth(200)
# fib.write_to_file()


_n = int(input("Enter n to find nth fibonacci number: "))
start = time.time()
print(f"The answer is: {fib.get_nth_term(_n)}")
end = time.time()
print(f"The time of execution of program was: {(end - start):e} seconds")
