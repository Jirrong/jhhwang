(() => {
  'use strict';
  const newPost = document.getElementById('new-post-link');
  if (newPost) {
    const dateParts = new Intl.DateTimeFormat('en', { timeZone: 'Asia/Seoul', year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(new Date());
    const part = type => dateParts.find(item => item.type === type).value;
    const today = `${part('year')}-${part('month')}-${part('day')}`;
    const content = `---\ntitle: "Post title"\ndate: ${today} 00:00:00 +0900\ndescription: "Summarize the question or main point."\ncategories: [Study notes]\ntags: [Chemistry]\nlang: en\nmath: true\ntoc: true\n---\n\nStart with the question or context.\n\n<!--more-->\n\n## Question\n\nWhat would you like to understand?\n\n## Notes\n\nWrite your post here.\n\n## References\n\n1. Authors, title, journal, year. DOI or original URL.\n`;
    const target = new URL(newPost.href);
    target.searchParams.set('filename', `${today}-your-title.md`);
    target.searchParams.set('value', content);
    newPost.setAttribute('href', target.href);
  }

  const prepareEntry = (id, filename, template) => {
    const link = document.getElementById(id);
    if (!link) return;
    const order = Number.parseInt(link.getAttribute('data-next-order'), 10) || 1;
    const target = new URL(link.href);
    target.searchParams.set('filename', filename);
    target.searchParams.set('value', template(order));
    link.setAttribute('href', target.href);
  };
  prepareEntry('new-research-link', 'project-title.md', order => `---
title: "Research project title"
order: ${order}
period: "Month Year–present"
program: ""
institution: ""
status: Ongoing
summary: "Describe the question, approach, and scope in one or two sentences."
topics: [Chemistry]
published: false
---

## Research question

What question does this project address?

## Approach

Describe the methods and your contribution.

## Progress

Add dated updates, figures, or results here as the work develops.

## References

Add papers, datasets, or related blog posts.
`);
  prepareEntry('new-resource-link', 'seminar-title.md', order => `---
title: "Seminar title"
order: ${order}
kind: Seminar
event: ""
event_date: ""
summary: "Describe the seminar topic and intended audience."
topics: [Chemistry]
files:
  - label: "Slides (PDF)"
    url: /assets/resources/your-seminar.pdf
published: false
---

## Overview

Introduce the seminar and what the audience can learn from it.

## Outline

1. Background
2. Main discussion
3. Further reading

## References

Add the sources used in the seminar.
`);
})();
