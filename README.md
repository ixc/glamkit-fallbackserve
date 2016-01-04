# Fallback Media Server

This is a drop-in replacement Django's `django.views.static.serve` to fetch
missing static files from a preconfigured URL.

In addition, it also provides a file storage engine as a thin proxy for
Django's default `FileSystemStorage`, again fetching missing static files.

# Settings

## FALLBACK_STATIC_PREFIXES

A list of prefixes relative to `MEDIA_URL` (without the leading slash). For
example:

    FALLBACK_STATIC_PREFIXES = (
        'uploads/',
    )

## FALLBACK_STATIC_URL

The URL from which to fetch missing static files.

## FALLBACK_STATIC_URL_USER

If the `FALLBACK_STATIC_URL` requires HTTP basic authentication, this sets the
username.

## FALLBACK_STATIC_URL_PASS

If the `FALLBACK_STATIC_URL` requires HTTP basic authentication, this sets the
password.

## FALLBACK_USER_AGENT

A custom user agent string for requests to `FALLBACK_STATIC_URL`.

# Notes

There is an issue when using with `easy-thumbnails`. For each thumbnail image
on the page you are attempting to load, `easy-thumbnails` will try to access
`/media/test`.

To stop this from happening, add an empty file to your media folder:

    $ touch path/to/public/media/test
