from src.analytics.ranking import generate_ranking


def main():

    ranking = generate_ranking("nifty100.db")

    print("=" * 60)
    print("TOP 20 COMPANIES")
    print("=" * 60)

    print(ranking.head(20))


if __name__ == "__main__":
    main()