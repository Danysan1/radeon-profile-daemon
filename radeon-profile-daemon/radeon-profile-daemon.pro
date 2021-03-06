#-------------------------------------------------
#
# Project created by QtCreator 2014-05-10T15:06:55
#
#-------------------------------------------------

QT       += core network

QT       -= gui

TARGET = radeon-profile-daemon
CONFIG   += console
CONFIG   -= app_bundle

#   https://forum.qt.io/topic/10178/solved-qdebug-and-debug-release/2
#   http://doc.qt.io/qt-5/qtglobal.html#QtMsgType-enum
#   qDebug will work only when compiled for Debug
#   QtWarning, QtCritical and QtFatal will work also on Release

CONFIG(release, debug|release):DEFINES += QT_NO_DEBUG_OUTPUT


TEMPLATE = app


SOURCES += main.cpp \
    rpdthread.cpp

HEADERS += \
    rpdthread.h
