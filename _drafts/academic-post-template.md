---
title: "글 제목"
description: "이 글의 질문과 핵심 내용을 한두 문장으로 정리합니다."
categories: [Study notes]
tags: [화학, 논문 읽기]
lang: ko
math: true
toc: true
---
이 파일은 공개되지 않는 글쓰기 템플릿입니다. 게시하려면 `_posts/YYYY-MM-DD-your-title.md`로 옮기고, 날짜를 파일명에 맞춰 작성하세요.

<!--more-->

## 질문

무엇을 알고 싶었나요? 논문 결과와 자신의 해석을 구분해 적습니다.

## 배경과 조건

계산 방법, 단위, 소프트웨어 버전, 실험 또는 모델의 가정을 기록합니다.

## 수식 예시

아래는 작성 형식을 보여주는 일반적인 예시입니다.

$$
\Delta G = \Delta H - T\Delta S
$$

본문 수식은 $\Delta G$처럼 쓸 수 있습니다.

## 코드 예시

```python
# 형식 예시: kJ mol^-1 단위의 엔탈피와 엔트로피 항
enthalpy = -20.0
entropy = -0.05
temperature = 298.15
free_energy = enthalpy - temperature * entropy
print(f"ΔG = {free_energy:.2f} kJ mol^-1")
```

## 그림과 표

그림을 `assets/images/posts/`에 올리고 다음처럼 넣을 수 있습니다.

{% raw %}
<!-- 경로를 실제 파일명으로 바꾸고 주석을 해제하세요.
![그림 내용을 설명하는 대체 텍스트]({{ '/assets/images/posts/your-figure.png' | relative_url }})
-->
{% endraw %}

| 조건 | 방법 | 관찰 |
| :--- | :--- | :--- |
| 조건 A | 계산 또는 실험 방법 | 결과와 단위 |

## 해석과 남은 질문

확실한 내용과 아직 확인하지 못한 내용을 나누어 적습니다. 각주도 쓸 수 있습니다.[^note]

[^note]: 보충 설명이나 추가 출처를 여기에 적습니다.

## 참고 문헌

1. 저자, *논문 제목*, 저널, 연도. DOI 또는 원문 URL.
