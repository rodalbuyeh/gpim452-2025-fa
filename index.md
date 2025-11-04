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
Students may elect to have one lab exercise scored as a perfect score (100%), regardless of actual performance. This election must be made by the end of week 9 and cannot be changed. Send Rod your election via email. 



[Jump to the current week](#week-4-gathering-and-wrangling-data){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}