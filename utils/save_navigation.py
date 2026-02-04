AD_PATTERN=[
    "doubleclick.net",
    "googlesyndication.com",
    "googleadservices.com"
        ]
def block_ad(context):
    context.route("**/*", lambda route: route.abort()
    if any(ad in route.request.url for ad in AD_PATTERN)else route.continue_())
