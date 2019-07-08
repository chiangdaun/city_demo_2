# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2019/7/8 20:48
"""
from app import db


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(64))
    dept = db.relationship('Dept', back_populates='school')


class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(64))
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
    school = db.relationship('School', back_populates='dept')
    team = db.relationship('Team', back_populates='dept')


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64))
    dept_id = db.Column(db.Integer, db.ForeignKey('dept.id'))
    dept = db.relationship('Dept', back_populates='team')

