#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging


class Point:
    def __init__(self, *args):
        self._tag = 'Point'
        try:
            if args._tag == 'Point':
                x,y = args[0],args[1]
        except:
            if len(args) == 2:
                if type(args[0]) == int and type(args[1]) == int:
                    x,y = args[0],args[1]
                else:
                    logging.error('参数中有非int值 x%s y%s',type(args[0]),type(args[1]))
            else:
                if not args:
                    x,y = 0,0
        self.x = x
        self.y = y

    def __str__(self):
        return '<Point [{}, {}]>'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        raise logging.error('目标对象不是Point类,请检查')

    def __sub__(self, other):
        if type(other) == Point:
            return Point(self.x - other.x, self.y - other.y)
        raise logging.error('目标对象不是Point类,请检查')

    def __mul__(self, other):
        if type(other) == int:
            return Point(self.x * other, self.y * other)
        raise logging.error('目标对象不是int类,请检查')

    def __truediv__(self, other):
        if type(other) == int:
            return Point(self.x / other, self.y / other)
        raise logging.error('目标对象不是int类,请检查')

    def __cmp__(self, other):
        if type(other) == Point:
            return (self.x == other.x) and (self.y == other.y)

Point.ZERO = Point()
Point.INVALID = Point(-1,-1)