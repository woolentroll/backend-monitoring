import sentry_sdk
from datetime import date

sentry_sdk.init(
    "https://622066a1a7bf49eca6d4b88372c69e94@o661591.ingest.sentry.io/5764778",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
None > date.today()
try:
    division_by_zero = 1 / 0
except:
    print('nipa')
