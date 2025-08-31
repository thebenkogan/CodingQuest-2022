from PIL import Image

with Image.open("./data/10/in.png") as im:
    red = list(im.getdata(0))

msg = [r & 1 for r in red]
bs = bytearray()
for i in range(0, len(msg), 8):
    b = "".join(str(n) for n in msg[i : i + 8])
    bs.append(int(b, 2))

print(bs.decode("ascii"))
