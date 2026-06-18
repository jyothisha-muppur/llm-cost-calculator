# LLM Cost Calculator

A simple Python CLI tool to estimate and compare LLM API costs across providers — OpenAI, Anthropic, and Google.

I built this while working on LLM cost optimization for production GenAI workloads. When you're running models at scale, small per-token price differences add up fast, and it helps to quickly see which model is most cost-effective for a given token workload before committing to it.

## Features

- Estimate cost for a single model given input/output token counts
- Compare the same workload across all supported models, sorted cheapest to most expensive
- Scale to batch or monthly estimates with a `--requests` multiplier
- Easy to extend — add new models by updating one pricing dictionary

## Usage

Compare all models for a given workload:

```bash
python llm_cost_calculator.py --input 1000 --output 500
```

Price a specific model across many requests (e.g. monthly volume):

```bash
python llm_cost_calculator.py --input 1000 --output 500 --model claude-sonnet-4 --requests 100000
```

## Supported models

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|--------------------:|---------------------:|
| gpt-4o | 2.50 | 10.00 |
| gpt-4o-mini | 0.15 | 0.60 |
| claude-opus-4 | 15.00 | 75.00 |
| claude-sonnet-4 | 3.00 | 15.00 |
| claude-haiku-4 | 0.80 | 4.00 |
| gemini-2.5-pro | 1.25 | 10.00 |
| gemini-2.5-flash | 0.30 | 2.50 |

## Note on pricing

Prices are approximate and change frequently. Always check the provider's current pricing page before relying on these numbers. Update the `PRICING` dictionary in `llm_cost_calculator.py` to keep them current.

## Built with

Python 3 · argparse (standard library, no external dependencies)
