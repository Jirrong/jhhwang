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
})();
