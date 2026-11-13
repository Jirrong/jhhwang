수식이 있는 공부 노트, 짧은 논문 메모, 코드와 계산 기록을 모두 같은 방식으로 올릴 수 있습니다. 글 목록, 검색, 태그, RSS는 글을 추가하면 자동으로 갱신됩니다.

<div class="form-group" markdown="0"><a id="new-post-link" class="btn btn-primary" href="https://github.com/{{ site.repository }}/new/{{ site.github_branch }}/_posts?filename={{ site.time | date: '%Y-%m-%d' }}-your-title.md">새 글 쓰기 ↗</a><a class="btn btn-default" href="https://github.com/{{ site.repository }}/blob/{{ site.github_branch }}/_drafts/academic-post-template.md">전체 글 템플릿 ↗</a></div>
<p class="text-muted small">새 글 쓰기는 GitHub 편집기를 엽니다. 저장소 쓰기 권한이 있는 계정으로 로그인해 주세요.</p>

## 1. 파일 이름 정하기

`_posts/2026-11-13-my-first-note.md`처럼 **날짜 + 영문 슬러그 + `.md`** 형식으로 만듭니다. 글 제목과 본문은 한국어·영어 모두 가능합니다. 같은 날짜라도 슬러그가 다르면 여러 글을 쓸 수 있습니다.

## 2. 글 정보와 본문 쓰기

새 글 버튼을 누르면 아래 형식이 미리 채워집니다. 제목, 날짜, 설명, 태그를 바꾸고 본문을 작성하세요. 실제 작성일은 파일명과 `date`에 함께 반영합니다.

```yaml
---
title: "논문을 읽고 남은 질문"
date: 2026-11-13 00:00:00 +0900
description: "어떤 질문에서 출발한 글인지 짧게 소개합니다."
categories: [Paper notes]
tags: [유기화학, 반응 메커니즘]
lang: ko
math: true
toc: true
---
```

- `categories`는 큰 분류, `tags`는 검색에 쓸 세부 주제입니다.
- `math: true`로 두면 LaTeX 수식을 사용할 수 있습니다.
- `toc: true`이면 `##`와 `###` 제목으로 목차가 만들어집니다.
- `description`은 목록과 링크 미리보기에 쓰입니다.
- 날짜가 미래이면 발행 시점까지 숨겨집니다. GitHub Pages는 그 시각에 자동으로 다시 빌드하지 않으므로, 예약 글은 원하는 시점에 커밋하거나 다시 빌드해야 합니다.

첫 문단 뒤에 `<!--more-->`를 넣으면 글의 도입을 구분할 수 있습니다.

## 3. 수식, 코드, 참고 문헌 넣기

본문 수식은 `$\Delta G$`, 독립 수식은 아래처럼 씁니다.

```tex
$$
\Delta G = \Delta H - T\Delta S
$$
```

$$
\Delta G = \Delta H - T\Delta S
$$

코드는 백틱 세 개 뒤에 `python`, `bash`, `cpp` 같은 언어명을 붙여 작성합니다. 게시된 글에는 구문 강조와 복사 버튼이 나타납니다. 표, 인용문, 각주 `[^1]`도 사용할 수 있습니다.

그림은 `assets/images/posts/`에 올린 다음 아래 경로를 실제 파일명으로 바꿉니다.

{% raw %}
```liquid
![그림의 내용을 설명하는 문장]({{ '/assets/images/posts/figure.png' | relative_url }})
```
{% endraw %}

논문 메모에는 원문 링크나 DOI를 함께 남기면 나중에 다시 찾아가기 좋습니다.

## 4. 저장하고 발행하기

GitHub 편집기의 **Commit changes**에서 `gh-pages` 브랜치에 저장하면 사이트가 다시 빌드됩니다. 반영까지 잠시 걸릴 수 있습니다. 변경을 먼저 검토하고 싶다면 새 브랜치와 Pull Request로 저장하세요.

비공개 초안은 `_drafts/`에 두거나 글 정보에 `published: false`를 넣습니다. 초안은 사이트와 검색, RSS에 포함되지 않습니다. 다만 **이 저장소는 공개 저장소라 초안 파일 자체는 GitHub에서 보입니다.**

기존 글은 [글 폴더](https://github.com/{{ site.repository }}/tree/{{ site.github_branch }}/_posts)에서 파일을 선택하고 편집하면 됩니다.

[블로그 글 목록으로 돌아가기 →]({{ '/blog/' | relative_url }})

{% include notebook-math.html %}
<script src="{{ '/assets/js/site.js' | relative_url }}" defer></script>
