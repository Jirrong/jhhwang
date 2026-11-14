# LinkedIn → blog

The home-page profile is https://www.linkedin.com/in/jirrong0116/.

The implementation uses LinkedIn's official Posts API. It does not scrape login pages or use browser cookies. Personal-post reading requires **approved `r_member_social` access**; LinkedIn restricts that permission. The self-service **Share on LinkedIn** product grants `w_member_social`, which is for posting and does not enable this reader. See the [official Posts API permissions](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api#permissions) and [Share on LinkedIn documentation](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin).

## Enable authorized automatic fetching

1. Obtain a LinkedIn OAuth access token from an application approved to read your personal posts with `r_member_social`. Do not use or send a LinkedIn password or session cookie.
2. In GitHub repository **Settings → Secrets and variables → Actions**, add a repository **secret** called `LINKEDIN_ACCESS_TOKEN`.
3. Add repository **variable** `LINKEDIN_AUTHOR_URN`, containing your own `urn:li:person:...` identifier supplied by the authorized LinkedIn integration. The public slug `jirrong0116` is not this identifier.
4. Optionally set `LINKEDIN_API_VERSION` to a supported `YYYYMM` version. The initial default is `202610`; keep it current with LinkedIn's version lifecycle.
5. Run **Actions → Sync LinkedIn posts → Run workflow** to verify your authorization. After configuration, it checks every six hours. Without the token and author URN, it reports that sync is inactive and makes no changes.

The workflow validates and builds the site before committing changes to `gh-pages`. It explicitly requests a GitHub Pages build because commits made with `GITHUB_TOKEN` do not start another push workflow. A non-fast-forward push fails without overwriting newer repository changes; a later run can retry.

## Import an existing API response

If you already have an authorized Posts API JSON response, put it in an untracked local file or the excluded `docs/` directory and run:

```sh
python3 scripts/sync_linkedin.py \
  --input /path/to/posts.json \
  --author 'urn:li:person:YOUR_PERSON_ID'
```

The input can be a post array or an object with an `elements` array. Posts with images also need an authorized `LINKEDIN_ACCESS_TOKEN` so the importer can retrieve their original media. The importer does not invent publication dates or complete a truncated screenshot. A standard LinkedIn CSV download is a different format and is not accepted by this JSON importer.

## What is preserved

- Original visible post text, paragraph breaks, hashtags, emoji, and publication timestamp; no translation or rewriting.
- Original single/multiple images, downloaded to `assets/linkedin/` with available alt text.
- Original LinkedIn link and any linked article.
- A stable blog file per LinkedIn post ID. Unchanged records are skipped; changed source posts update the same file. Missing image assets are downloaded again.

Only your own **public, published, original posts** are imported. Private posts, drafts, reshares, other authors, reactions, and comments are skipped. Video/document attachments link to the original rather than pretending to be a complete media copy. LinkedIn's interface, likes, and comments are not reproduced. Removing a post on LinkedIn does not automatically delete an existing blog file; delete that file in `_posts/` if needed.

Imported text is rendered literally rather than executing Markdown or Liquid contained in a social post. Math and automatic TOC are disabled for imported posts. Text/image imports participate in the normal blog list, search, and RSS when the site builds.

## Current status

The importer and workflow are present and covered by offline tests. This session has no approved read token or personal API identifier, so **live automatic fetching has not been enabled or tested against the owner's account**. Nothing is published from partial LinkedIn screenshots or search snippets.
