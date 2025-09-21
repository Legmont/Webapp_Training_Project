from flask import Blueprint, render_template, request

about_bp= Blueprint("about_bp", __name__)

@about_bp.route("/about")
def about_view():
    return render_template("about.jinja2")