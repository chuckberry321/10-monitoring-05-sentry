
import sentry_sdk
sentry_sdk.init(
    "https://e28c985090bc4134bd04b046ab7c44e4@o1252832.ingest.sentry.io/6420184",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

print("start")
val = int(input("input number: "))
tmp = 10 / val
print(tmp)

divide_by_zero = 1/0
