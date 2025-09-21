from flask import Blueprint, render_template, request

homepage_bp= Blueprint("homepage_bp", __name__)

@homepage_bp.route("/")
def home_view():
    return render_template("homepage.jinja2")