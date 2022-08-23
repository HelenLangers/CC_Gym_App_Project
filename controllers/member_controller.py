from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/members.html", members = members)

@members_blueprint.route("/members", methods=['POST'])
def add_member():
    name = request.form['name']
    new_member = Member(name)
    member_repository.save(new_member)
    return redirect("/members")
    
@members_blueprint.route("/members/<id>")
def view_one(id):
    member = member_repository.select(id)
    lessons = member_repository.list_lessons_member_is_signed_up_for(member)
    return render_template("/members/onemember.html", member = member, lessons = lessons)

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/editmember.html", member = member) 

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    name = request.form['name']
    member = Member(name, id)
    member_repository.update(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")


