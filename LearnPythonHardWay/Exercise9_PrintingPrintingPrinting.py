days = "mon tues wed thrs fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njuly\naug\nsep\noct\nnov\ndec"

print("here are the days:", days)

print("here are the months:", months)

print("""
there is something going on here.
with three double quotes, 
we will be able to type as much as we like
even 4 lines if we want, or 5, or 6
""")

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" %i),
  