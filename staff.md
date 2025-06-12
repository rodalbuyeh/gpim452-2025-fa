---
layout: page
title: Staff
description: A listing of all the course staff members.
nav_order: 7
---

# Staff

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

<!-- ## Course Staff

{% assign staff = site.staffers | where: 'role', 'TA' %}
{% for staffer in staff %}
{{ staffer }}
{% endfor %}

{% assign staff = site.staffers | where: 'role', 'Tutor' %}
{% for staffer in staff %}
{{ staffer }}
{% endfor %} -->

