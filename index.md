---
layout: home
title: Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{% assign instructors = site.staffersnobio | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
  {% include staffer.html staffer=staffer %}
{% endfor %}

<!-- Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis. -->

<!-- {: .success }
**This course site is under construction.** -->

[Jump to the current week](#week-1-foundations-and-motivation){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}