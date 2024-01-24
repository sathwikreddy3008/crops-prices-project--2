from django.contrib import admin

# Register your models here.
'''<footer>
        <p>Domain: Agriculture</p>
        <p>&copy; 2024 </p>
    </footer>'''

'''<nav>
        <a href="{% url 'homepage:home' %}">Home</a>
        <a href="{% url 'homepage:blog' %}">Blog</a>
        {% if user.is_authenticated %}
            <a href="{% url 'crop_prices:logout' %}" >Logout</a>
        {% else %}
        <a href="{% url 'crop_prices:login' %}" >Login</a>
            {% endif %}
            <a href="{% url 'crop_prices:prices' %}">Crop Prices</a>

    </nav>'''