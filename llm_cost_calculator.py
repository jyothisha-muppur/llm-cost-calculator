"""
LLM Cost Calculator
A simple CLI tool to estimate and compare LLM API costs across providers.

Prices are per 1 million tokens (USD) and are approximate — always check
the provider's current pricing page before relying on these numbers.
"""

import argparse

# Approximate pricing per 1M tokens (USD): (input_price, output_price)
# Update these as provider pricing changes.
PRICING = {
    "gpt-4o":            (2.50, 10.00),
    "gpt-4o-mini":       (0.15, 0.60),
    "claude-opus-4":     (15.00, 75.00),
    "claude-sonnet-4":   (3.00, 15.00),
    "claude-haiku-4":    (0.80, 4.00),
    "gemini-2.5-pro":    (1.25, 10.00),
    "gemini-2.5-flash":  (0.30, 2.50),
}


def calculate_cost(model, input_tokens, output_tokens):
    """Return the estimated cost in USD for a single request."""
    if model not in PRICING:
        raise ValueError(f"Unknown model '{model}'. Available: {', '.join(PRICING)}")

    input_price, output_price = PRICING[model]
    cost = (input_tokens / 1_000_000) * input_price
    cost += (output_tokens / 1_000_000) * output_price
    return cost


def compare_all(input_tokens, output_tokens):
    """Print the cost of the same request across every known model."""
    print(f"\nCost comparison for {input_tokens:,} input / {output_tokens:,} output tokens:\n")
    results = []
    for model in PRICING:
        cost = calculate_cost(model, input_tokens, output_tokens)
        results.append((model, cost))

    # Sort cheapest to most expensive
    results.sort(key=lambda x: x[1])
    for model, cost in results:
        print(f"  {model:<20} ${cost:.4f}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Estimate LLM API costs across providers."
    )
    parser.add_argument("--input", type=int, required=True,
                        help="Number of input (prompt) tokens")
    parser.add_argument("--output", type=int, required=True,
                        help="Number of output (completion) tokens")
    parser.add_argument("--model", type=str,
                        help="Specific model to price. Omit to compare all models.")
    parser.add_argument("--requests", type=int, default=1,
                        help="Number of requests (to estimate batch/monthly cost)")

    args = parser.parse_args()

    if args.model:
        per_request = calculate_cost(args.model, args.input, args.output)
        total = per_request * args.requests
        print(f"\nModel: {args.model}")
        print(f"Per request: ${per_request:.4f}")
        print(f"Total for {args.requests:,} requests: ${total:.2f}\n")
    else:
        compare_all(args.input, args.output)
        if args.requests > 1:
            print(f"(Multiply by {args.requests:,} for total batch cost.)\n")


if __name__ == "__main__":
    main()
