import random


class func():
    def _init_(self, text, mode="std"):
        if mode == "std":
            sequence = self.standart(text)
        elif mode == "stairs":
            sequence = self.stairs(text)
        elif mode == "running_line":
            sequence = self.running_line(text)
        elif mode == "wave":
            sequence = self.wave(text)
        elif mode == "random":
            sequence = None
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
                b += '{}'.format(i)
                c.append(b)
            x = len(b)
            x1 = 0
            while x > 0:
                x -= 1
                x1 -= 1
                c.append(b[:x1])
            c.remove('')
            c.pop()

            return c

        sequence = main(text)
        return sequence

    def running_line(self, text):
        main = []

        def show(text, maximum, symbol=" "):
            text = symbol * maximum + text
            for i in range(len(text)):
                a = '{0}'.format(text[i:i + maximum])
                main.append(a)
                return main
        return show(text, len(text))

    def wave(self, text):
        main = []
        for i in range(len(text)):
            may = []
            for b in range(len(text)):
                may.append(text[b])
            if may[i] != " ":
                may[i] = text[i].upper()
                may = str(may)
                may = may.replace(',', ''
                        ).replace("['", ''
                        ).replace("']", ''
                        ).replace("' '", ''
                        ).replace(" ", '   '
                        ).replace("   ", ' ')
                main.append(may)
            else:
                pass

        return main

    def rand(self, text):
        xd = []
        for i in text:
            xd.append(i)

        seq = ''
        for i in range(len(xd)):
            seq += xd[random.randint(0, len(xd)-1)]
        return seq
