---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
My research articles have been published in Korean, focusing on digital humanities research pertaining to Korean language materials. Additionally, I have also published papers in English, namely in the field of computational social sciences, where I have explored topics such as social media and academic databases. You can also find my articles on <u><a href="https://scholar.google.com/citations?user=y-34CCwAAAAJ" target="_blank">my Google Scholar profile</a></u>.


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}