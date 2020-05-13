class func():
    def _init_(self, text, mode="std"):
        if mode == "std":
            sequence = self.standart(text)
        elif mode == "stairs":
            sequence = self.stairs(text)
        elif mode == "motion":
            sequence = self.motion(text)
        else:
            print("problems with mode choice")

        return sequence

    def standart(self, text):
        sequence = text.split(";")
        return sequence

    def stairs(self, text):
        def main(text):
            b = ''
            c = []
            for i in text:
                b+='{}'.format(i)
                c.append(b)
            x = len(b)
            x1 = 0
            while x>0:
                x-=1
                x1-=1
                c.append(b[:x1])
            c.remove('')
            c.pop()

            return c

        sequence = main(text)
        return sequence

    def motion(self, text):
        pass
