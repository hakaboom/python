#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging
from logzero import setup_logger
from cached_property import cached_property
logger = setup_logger("script", level=logging.DEBUG)

class Point:

    """
        Point.ZERO      :一个x,y均为0的Point
        Point.INVALID   :一个x,y均为-1的Point
        Point(void) :构造一个x,y均为0的Point
        Point(x:int , y:int)    :根据x,y构造一个Point
        Point(Point)    :根据point,拷贝一个新的Point
        Point.x :x坐标
        Point.y :y坐标
        支持 +,-,*,/,==操作
    """

    def __init__(self, *args):
        self._tag = 'Point'
        _len = len(args)
        if _len == 0:
            x, y = 0, 0
        elif _len == 1:
            try:
                if args[0]._tag == 'Point':
                    x, y = args[0].x, args[0].y
            except:
                logger.error('参数中错误 %s type:%s',args[0],type(args[0]))
        elif _len == 2:
            if type(args[0]) == int and type(args[1]) == int:
                x, y = args[0], args[1]
            else:
                logger.error('参数中有非int值 x%s y%s', type(args[0]), type(args[1]))
        elif _len > 2:
            logger.error('创建Point错误')

        self.x = x
        self.y = y

    def __str__(self):
        return '<Point [{}, {}]>'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        raise logger.error('目标对象不是Point类,请检查')

    def __sub__(self, other):
        if type(other) == Point:
            return Point(self.x - other.x, self.y - other.y)
        raise logger.error('目标对象不是Point类,请检查')

    def __mul__(self, other):
        if type(other) == int:
            return Point(self.x * other, self.y * other)
        raise logger.error('目标对象不是int类,请检查')

    def __truediv__(self, other):
        if type(other) == int:
            return Point(self.x / other, self.y / other)
        raise logger.error('目标对象不是int类,请检查')

    def __eq__(self, other):
        if type(other) == Point:
            return self.x == other.x and self.y == other.y
        else:
            logger.error('目标对象不是Point类,请检查')
            return False
Point.ZERO = Point()
Point.INVALID = Point(-1, -1)


class Size:
    """
        Size.ZERO      :一个width,height均为0的Size
        Size.INVALID   :一个width,height均为-1的Size
        Size(void) :构造一个width,height均为0的Size
        Size(width:int , height:int)    :根据width,height构造一个Size
        Size(Size)    :根据Size,拷贝一个新的Size
        Size.width  :Size的宽
        Size.height :Size的高
        支持 +,-,*,/,==操作
    """
    def __init__(self, *args):
        self._tag = 'Size'
        _len = len(args)
        if _len == 0:
            width,height = 0,0
        elif _len == 1:
            try:
                if args[0]._tag == 'Size':
                    width, height = args[0].width, args[0].height
            except:
                logger.error('参数中错误 %s type:%s',args[0],type(args[0]))
        elif _len == 2:
            args_0type,args_1type = type(args[0]),type(args[1])
            if args_0type == Point and args_1type == Point:
                width, height = min(args[0].x, args[1].x), max(args[0].y, args[1].y)
            elif args_0type == int and args_1type == int:
                width,height = args[0],args[1]
            else:
                logger.error('参数中有错误 {} {}',args_0type,args_1type)

        self.width = width
        self.height = height

    def __str__(self):
        return '<Size [{} x {}]>'.format(self.width,self.height)

    def __add__(self, other):
        if type(other) == Size:
            return Size(self.width + other.width, self.height + other.height)
        raise logger.error('目标对象不是Size类,请检查')

    def __sub__(self, other):
        if type(other) == Size:
            return Size(self.width - other.width, self.height - other.height)
        raise logger.error('目标对象不是Size类,请检查')

    def __mul__(self, other):
        if type(other) == int:
            return Size(self.width * other, self.height * other )
        raise logger.error('目标对象不是int类,请检查')

    def __truediv__(self, other):
        if type(other) == int:
            return Size(self.width / other, self.height / other )
        raise logger.error('目标对象不是int类,请检查')

    def __eq__(self, other):
        if type(other) == Point:
            return self.width == other.width and self.height == other.height
        else:
            logger.error('目标对象不是Size类,请检查')
            return False
Size.ZERO = Size()
Size.INVALID = Size(-1, -1)


class Rect:
    def __init__(self,*args):
        pass