from django.conf import settings
from meta.views import Meta


def meta_context(request):
    meta = Meta(
        title="Rating Rocker",
        description="Rating Rocker - Premium directory consumer reviews",
        extra_props={
            "author": "Rating Rocker",
            "viewport": "width=device-width, initial-scale=1, shrink-to-fit=no"
        },
        extra_custom_props=[
            ("http-equiv", "X-UA-COMPATIBLE", "IE=edge")
        ]
    )
    return {
        "meta": meta,
    }

def gtag_settings(request):
    return {
        "gtag_id": settings.GTAG_ID
    }