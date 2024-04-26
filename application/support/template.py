from flask import render_template as real_render_template

def render_template(*args, **kwargs):

    from application.jinja2.menu import render_menu

    return real_render_template(*args, **kwargs, render_menu=render_menu)
