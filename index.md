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

{: .success }
Final exam will only require conceptual knowledge of the lectures, not the labs or anything specific to R programming. Sample finals have been posted in campuswire.



[Jump to the current week](#week-4-gathering-and-wrangling-data){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}