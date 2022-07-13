from django import template
from django.utils.safestring import mark_safe
import math

register = template.Library()

@register.filter()
def rating_to_star(value):
    #covert rating 1-5 to star
    #round value to the nearest half number
    def round_to_half():
        return round((value * 2)) / 2
    
    rating = round_to_half()
    rating_no_fill = math.floor(5 - rating)
    text = ""
    full_star_fill = '<i class="bi bi-star-fill"></i>'
    half_star_fill = '<i class="bi bi-star-half"></i>'
    empty_star = '<i class="bi bi-star"></i>'
    #fill stars accoring to the rating
    while rating != 0:
        if rating == 0.5:
            text += half_star_fill
            rating -= 0.5
        else:
            text += full_star_fill
            rating -= 1
            
    #fill the empty star so that the total length of
    #stars is 5
    for _ in range(rating_no_fill):
        text += empty_star
        
    return mark_safe(text)


    
        