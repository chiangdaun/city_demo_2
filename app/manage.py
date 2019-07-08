# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2019/7/8 20:29
"""
import json

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from app import app
from flask import render_template, request, jsonify
from models import School, Dept, Team


class RegisterForm(FlaskForm):
    school = SelectField('学院', coerce=int, render_kw={"class": "form-control"})
    department = SelectField('系', coerce=int, render_kw={"class": "form-control"})
    submit = SubmitField('提交', render_kw={"class": "form-control"})

    # 初始化下拉表单值，直接给出了学院的所有值
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # 第一个值给空是防止第一个选择就是想要的，下拉表单感受不到变化
        self.school.choices = [(0, '-请选择-')]
        for school in School.query.order_by(School.id).all():
            self.school.choices.append((school.id, school.school_name))
        self.department.choices = [(0, '-请选择-')]
        for department in Dept.query.order_by(Dept.id).all():
            self.department.choices.append((department.id, department.dept_name))


@app.route('/select_school/', methods=['GET', 'POST'])
def selected_school():
    school_id = request.args.get('selected_id')
    school_id = int(json.loads(school_id))
    depts = [(dept.id, dept.dept_name) for dept in Dept.query.filter_by(school_id=school_id).all()]
    return jsonify(depts)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    # print(form.data)
    if form.validate_on_submit():
        data = form.data
        print(data)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
