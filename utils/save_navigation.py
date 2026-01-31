AD_PATTERNS=["**/*google_vignette*","**/*adservice*"]

def block_ad(context):
   for pattern in AD_PATTERNS:
       context.route(pattern,lambda route:route.abort())