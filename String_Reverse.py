class Reverse:
    def __init__(self, text):
     self.text=text

    def reverse(self):
       return self.text[::-1]

og=Reverse("Hello Codingal")
print(og.reverse())