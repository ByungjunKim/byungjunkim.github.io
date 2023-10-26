---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
I have authored research papers that are published in both Korean and English. My primary research domains encompass digital humanities and computational social science, with a particular emphasis on the analysis of expansive multilingual corpora, notably in Korean and English. You can also find my articles on <u><a href="https://scholar.google.com/citations?user=y-34CCwAAAAJ" target="_blank">my Google Scholar profile</a></u>.


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}