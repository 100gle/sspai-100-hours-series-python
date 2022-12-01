{% extends "base.md" %}

{% block title %}
{{ title }}
{% endblock %}

{% block environment %}
    {% for item in setup %}
        - {{ item.name }}: {{ item.detail }}
    {% endfor %}
{% endblock %}

{% block description %}
{{ description }}
{% endblock %}
