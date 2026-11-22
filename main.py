import os

TEXT = (
    "Day 1 post a $30 Etsy rescue gig on Fiverr: rewrite title, 13 tags, "
    "alt-text for vintage sellers with no sales. Find buyers in r/EtsySellers "
    "posts asking why nothing sells, reply with one free fixed listing, link "
    "the gig. Spend $100 on Fiverr ads. 15 sales in 30 days = $450."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(TEXT)
