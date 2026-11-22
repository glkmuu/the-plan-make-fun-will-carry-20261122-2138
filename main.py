import os

TEXT = (
    "Day 1 list a $30 Fiverr gig: AI resume + LinkedIn rewrite in 2 hours, not days. "
    "Answer 10 buyer requests daily \u2014 resume gigs there carry 1,000+ reviews, "
    "demand is proven. Spend $0 on ads; $25 to boost it after 5 sales. "
    "20 orders in 30 days = $600, less Fiverr's 20% = $480 kept."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
