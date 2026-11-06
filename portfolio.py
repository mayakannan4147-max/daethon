#!/usr/bin/env python3

import csv
from pathlib import Path

DEFAULT_PRICES = {
    "AAPL": 214.63,
    "MSFT": 428.72,
    "GOOGL": 178.25,
    "AMZN": 193.82,
    "NVDA": 116.30,
    "TSLA": 228.15,
    "META": 524.81,
    "JPM": 195.34,
    "V": 274.22,
    "XOM": 110.96,
}


def load_reference_prices(csv_path=None):
    prices = DEFAULT_PRICES.copy()
    if csv_path is None:
        csv_path = Path("ticker_prices.csv")

    try:
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                symbol = (row.get("symbol") or row.get("Ticker") or row.get("ticker") or "").strip().upper()
                price_value = row.get("price") or row.get("Price") or row.get("close") or row.get("Close")
                if symbol and price_value:
                    try:
                        prices[symbol] = float(price_value)
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass

    return prices


def get_portfolio():
    return {
        "AAPL": {"shares": 25, "buy_price": 178.40},
        "MSFT": {"shares": 12, "buy_price": 395.10},
        "NVDA": {"shares": 18, "buy_price": 98.25},
        "V": {"shares": 30, "buy_price": 245.80},
    }


def calculate_position_metrics(portfolio, prices):
    rows = []
    total_invested = 0.0
    total_market_value = 0.0

    for ticker, info in portfolio.items():
        shares = float(info["shares"])
        buy_price = float(info["buy_price"])
        current_price = float(prices.get(ticker, buy_price))
        invested = shares * buy_price
        market_value = shares * current_price
        change = market_value - invested
        percent_change = ((current_price - buy_price) / buy_price) * 100 if buy_price else 0.0

        total_invested += invested
        total_market_value += market_value

        rows.append(
            {
                "symbol": ticker,
                "shares": shares,
                "buy_price": buy_price,
                "current_price": current_price,
                "invested": invested,
                "market_value": market_value,
                "change": change,
                "percent_change": percent_change,
            }
        )

    total_change = total_market_value - total_invested
    total_percent_change = ((total_market_value - total_invested) / total_invested) * 100 if total_invested else 0.0

    return rows, {
        "total_invested": total_invested,
        "total_market_value": total_market_value,
        "total_change": total_change,
        "total_percent_change": total_percent_change,
    }


def print_portfolio_summary(rows, totals):
    print("\nInvestment Portfolio Summary")
    print("=" * 92)
    print(f"{'Ticker':<8}{'Shares':>8}{'Buy Price':>12}{'Current':>12}{'Invested':>14}{'Value':>14}{'% Gain/Loss':>14}{'Gain/Loss':>14}")
    print("-" * 92)

    for item in rows:
        print(
            f"{item['symbol']:<8}"
            f"{item['shares']:>8.2f}"
            f"{item['buy_price']:>12.2f}"
            f"{item['current_price']:>12.2f}"
            f"${item['invested']:>12.2f}"
            f"${item['market_value']:>12.2f}"
            f"{item['percent_change']:>12.2f}%"
            f"${item['change']:>12.2f}"
        )

    print("-" * 92)
    print(
        f"{'TOTAL':<8}"
        f"{'':>8}"
        f"{'':>12}"
        f"{'':>12}"
        f"${totals['total_invested']:>12.2f}"
        f"${totals['total_market_value']:>12.2f}"
        f"{totals['total_percent_change']:>12.2f}%"
        f"${totals['total_change']:>12.2f}"
    )
    print("=" * 92)


def write_summary_csv(rows, totals, output_path="portfolio_summary.csv"):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["symbol", "shares", "buy_price", "current_price", "invested", "market_value", "percent_change", "gain_loss"])

        for item in rows:
            writer.writerow(
                [
                    item["symbol"],
                    f"{item['shares']:.2f}",
                    f"{item['buy_price']:.2f}",
                    f"{item['current_price']:.2f}",
                    f"{item['invested']:.2f}",
                    f"{item['market_value']:.2f}",
                    f"{item['percent_change']:.2f}",
                    f"{item['change']:.2f}",
                ]
            )

        writer.writerow([])
        writer.writerow(["total_invested", f"{totals['total_invested']:.2f}"])
        writer.writerow(["total_market_value", f"{totals['total_market_value']:.2f}"])
        writer.writerow(["total_change", f"{totals['total_change']:.2f}"])
        writer.writerow(["total_percent_change", f"{totals['total_percent_change']:.2f}"])

    print(f"\nPortfolio summary exported to {output_path}")


def main():
    prices = load_reference_prices()
    portfolio = get_portfolio()
    rows, totals = calculate_position_metrics(portfolio, prices)
    print_portfolio_summary(rows, totals)
    write_summary_csv(rows, totals)


if __name__ == "__main__":
    main()
