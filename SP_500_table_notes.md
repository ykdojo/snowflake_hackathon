## Notes on SP_500 Table

- The SP_500 table is located in the Snowflake database 'S__P_500_BY_DOMAIN_AND_AGGREGATED_BY_TICKERS_SAMPLE' and schema 'DATAFEEDS'.
- The table contains the following columns:
  - COMPANY_NAME
  - TICKER
  - DOMAIN
  - DATE
  - COUNTRY
  - DESKTOP_VISITS
  - DESKTOP_BOUNCE_RATE
  - DESKTOP_AVG_VISIT_DURATION
  - DESKTOP_PAGES_PER_VISIT
  - MOBILE_VISITS
  - MOBILE_BOUNCE_RATE
  - MOBILE_AVG_VISIT_DURATION
  - MOBILE_PAGES_PER_VISIT
  - TOTAL_VISITS
  - TOTAL_BOUNCE_RATE
  - TOTAL_AVG_VISIT_DURATION
  - TOTAL_PAGES_PER_VISIT
- The table contains data related to company visits, bounce rates, average visit durations, and pages per visit for both desktop and mobile platforms.
- The data is aggregated by company ticker and domain.

These notes provide a brief overview of the structure and content of the SP_500 table in the Snowflake database. Additional analysis and exploration may be conducted to gain further insights into the data.

## Notes on SP_500_ESTIMATED_TICKERS Table

- The SP_500_ESTIMATED_TICKERS table is located in the Snowflake database 'SP_500_COMPANY_ONLINE_PERFORMANCE_TICKER_AND_DOMAIN_LEVEL_DATA' and schema 'DATAFEEDS'.
- The table contains the following columns:
  - TICKER
  - COMPANY_NAME
  - COUNTRY
  - DESKTOP_VISITS
  - DESKTOP_BOUNCE_RATE
  - DESKTOP_AVG_VISIT_DURATION
  - DESKTOP_PAGES_PER_VISIT
  - MOBILE_VISITS
  - MOBILE_BOUNCE_RATE
  - MOBILE_AVG_VISIT_DURATION
  - MOBILE_PAGES_PER_VISIT
  - TOTAL_VISITS
  - TOTAL_BOUNCE_RATE
  - TOTAL_AVG_VISIT_DURATION
  - TOTAL_PAGES_PER_VISIT
  - DATE
- The table contains data related to company online performance at the ticker level. The columns include information such as the company ticker, company name, country, desktop and mobile visits, bounce rates, average visit durations, pages per visit, total visits, and the date of the data.

These notes provide a brief overview of the structure and content of the SP_500_ESTIMATED_TICKERS table in the Snowflake database. Additional analysis and exploration may be conducted to gain further insights into the data.

## Notes on SP_500_ESTIMATED_DOMAIN Table

- The SP_500_ESTIMATED_DOMAIN table is located in the Snowflake database 'SP_500_COMPANY_ONLINE_PERFORMANCE_TICKER_AND_DOMAIN_LEVEL_DATA' and schema 'DATAFEEDS'.
- The table contains the following columns:
  - TICKER
  - COMPANY_NAME
  - DOMAIN
  - COUNTRY
  - DESKTOP_VISITS
  - DESKTOP_BOUNCE_RATE
  - DESKTOP_AVG_VISIT_DURATION
  - DESKTOP_PAGES_PER_VISIT
  - MOBILE_VISITS
  - MOBILE_BOUNCE_RATE
  - MOBILE_AVG_VISIT_DURATION
  - MOBILE_PAGES_PER_VISIT
  - TOTAL_VISITS
  - TOTAL_BOUNCE_RATE
  - TOTAL_AVG_VISIT_DURATION
  - TOTAL_PAGES_PER_VISIT
  - DATE
- The table contains data related to company online performance at the domain level. The columns include information such as the company ticker, company name, domain, country, desktop and mobile visits, bounce rates, average visit durations, pages per visit, total visits, and the date of the data.

These notes provide a brief overview of the structure and content of the SP_500_ESTIMATED_DOMAIN table in the Snowflake database. Additional analysis and exploration may be conducted to gain further insights into the data.

## Notes on V_SUMMARY_BY_TOPIC_STOCK_15MIN View

- The V_SUMMARY_BY_TOPIC_STOCK_15MIN view is located in the Snowflake database 'SFACTOR_SOCIAL_SENTIMENT_DATA_FOR_US_EQUITIES' and schema 'PUBLIC'.
- The view contains the following columns:
  - TICKER
  - DATE
  - RAW_S
  - RAW_S_MEAN
  - RAW_VOLATILITY
  - RAW_SCORE
  - S
  - S_MEAN
  - S_VOLATILITY
  - S_SCORE
  - S_VOLUME
  - SV_MEAN
  - SV_VOLATILITY
  - SV_SCORE
  - S_DISPERSION
  - S_BUZZ
  - S_DELTA
  - CENTER_DATE
  - CENTER_TIME
  - CENTER_TIME_ZONE
- The view contains data related to social sentiment for US equities, summarized by topic and stock at 15-minute intervals. The columns include information such as the stock ticker, date, raw sentiment scores, sentiment mean, sentiment volatility, sentiment score, sentiment volume, and other related metrics.

These notes provide a brief overview of the structure and content of the V_SUMMARY_BY_TOPIC_STOCK_15MIN view in the Snowflake database. Additional analysis and exploration may be conducted to gain further insights into the data.