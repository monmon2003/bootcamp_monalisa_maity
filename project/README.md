
# Stock Price tracker
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Investors and finance students often want a quick, low-friction way to monitor how a stock (or small group of stocks) is performing over time without relying on paid terminals like Bloomberg or manually checking prices on a brokerage app throughout the day. This project addresses that gap by building a lightweight Python-based tool that pulls historical and near-real-time price data for a given set of tickers, visualizes trends, and surfaces basic descriptive statistics (e.g., daily returns, moving averages, volatility) so the user can quickly understand a stock's recent behavior at a glance.
## Stakeholder & User
The primary stakeholder is a self-directed retail investor or finance student, someone who wants situational awareness of a stock's performance, not a trading signal or investment recommendation.

## Useful Answer & Decision
s such, the useful output here is descriptive, not predictive or causal: the goal is to summarize what has happened to the price historically and present it clearly (via charts and summary metrics), rather than forecast what will happen next or explain why it happened.

## Assumptions & Constraints
- Free data source (e.g., yfinance) is sufficient — no need for paid/real-time terminal-grade data
- "Near-real-time" means delayed quotes (typically 15-min lag), not true live tick data
- User provides valid, publicly-traded ticker symbols (no OTC/crypto/forex handling required initially)
- Analysis is single-user, local/script-based — no need for multi-user auth or cloud deployment at this stage
- Historical lookback window is bounded (e.g., 1-5 years) to keep data pulls and plots fast/manageable
- User has basic Python environment set up (or Streamlit, if a dashboard UI is used)
- Internet connection required for data pulls — no offline/cached-only mode assumed

## Known Unknowns / Risks
- Reliability of free data APIs (rate limits, downtime, or ticker data gaps) is untested at this stage
- Corporate actions (splits, dividends) may distort raw price data if not adjusted for
- Behavior with invalid tickers, delisted stocks, or missing data ranges is undefined
- Whether moving averages/volatility windows should be user-configurable or fixed defaults is unresolved
- Unclear whether scope should stay single-stock or extend to multi-ticker comparison from the start
- Performance/latency if user requests very long historical ranges or many tickers at once

## Lifecycle Mapping
- Build a tool that gives retail investors quick, descriptive visibility into stock price behavior → Problem Framing & Scoping (Stage 01) → Scoping paragraph + assumptions/risks doc (this artifact) defining problem, stakeholder, and output type
## Repo Plan
data/, src/, notebooks/, docs/
