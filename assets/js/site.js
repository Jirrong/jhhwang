(() => {
  'use strict';
  const newPost = document.getElementById('new-post-link');
  if (newPost) {
    const dateParts = new Intl.DateTimeFormat('en', { timeZone: 'Asia/Seoul', year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(new Date());
    const part = type => dateParts.find(item => item.type === type).value;
    const today = `${part('year')}-${part('month')}-${part('day')}`;
    const content = `---\ntitle: "글 제목"\ndate: ${today} 00:00:00 +0900\ndescription: "이 글을 한두 문장으로 소개합니다."\ncategories: [Study notes]\ntags: [화학]\nlang: ko\nmath: true\ntoc: true\n---\n\n여기에 글의 도입을 씁니다.\n\n<!--more-->\n\n## 질문\n\n무엇을 알고 싶었나요?\n\n## 내용\n\n본문을 자유롭게 작성하세요.\n\n## 참고 문헌\n\n1. 저자, 제목, 연도, DOI 또는 URL.\n`;
    const target = new URL(newPost.href);
    target.searchParams.set('filename', `${today}-your-title.md`);
    target.searchParams.set('value', content);
    newPost.setAttribute('href', target.href);
  }
})();
