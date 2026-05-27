# CLAUDE.md

## Project Overview

Static site for databloom.net — Jeremy Bloom's professional home page. Plain HTML + CSS, no build step.

- **URL:** https://databloom.net
- **Hosting:** S3 + CloudFront
- **Repo:** https://github.com/databloomnet/databloomnet-static

The dynamic apps (Streamlit, Gradio) live in a separate repo: [databloom_codes](https://github.com/databloomnet/databloom_codes), deployed on EC2 at https://apps.databloom.net.

## Structure

- `index.html` — home/landing page with "News & Posts" section
- `posts/*.html` — individual post pages
- `styles.css` — shared stylesheet
- Other top-level pages: `employment.html`, `consulting.html`, `certifications.html`, `about.html`, `contact.html`

## Adding a Post

1. Create `posts/<slug>.html` following the existing pattern (nav, `../styles.css`, footer, back link)
2. Add an entry to `index.html` under the appropriate year's `<ul class="posts">` section (newest first)

## Deployment

```bash
# Sync to S3
aws s3 sync . s3://databloom.net --exclude '.git/*' --exclude '.gitignore' --exclude '.DS_Store' --exclude '.claude/*' --exclude 'CLAUDE.md'

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id ENV8NHYBAT0ZU --paths "/*"
```

**Important:** The S3 bucket is `databloom.net`, NOT `www.databloom.net`. The `www` bucket is a redirect-only bucket.
