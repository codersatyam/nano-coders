from django.urls import path
from . import views
urlpatterns = [

    path("", views.solution, name="solution"),
    path("issue", views.issue, name="issue"),
    path("lr",views.lr,name="lr"),
    path("ml",views.ml,name="ml"),
    path("pr",views.pr,name="pr"),
    path("dt",views.dt,name="dt"),
    path("r2",views.r2,name="r2"),
    path("rf",views.rf,name="rf"),
    path("bestr",views.bestr,name="bestr"),
    path("preprocessing",views.preprocessing,name="preprocessing"),
    path("variables",views.variables,name="variables"),
    path("usefulfunctions",views.usefulfunctions,name="usefulfunctions"),
    path("calldataset",views.calldataset,name="calldataset"),
    path("ignoringrow",views.ignoringrow,name="ignoringrow"),
    path("missingdata",views.missingdata,name="missingdata"),
    path("mm",views.mm,name="mm"),
    path("mmc",views.mmc,name="mmc"),
    path("sklearn",views.sklearn,name="sklearn"),
    path("steps",views.steps,name="steps"),
    path("dpa",views.dpa,name="dpa"),
    path("introduction",views.introduction,name="introduction"),
    path("pvariables",views.pvariables,name="pvariables"),
    path("ptype",views.ptype,name="ptype"),
    path("poperators",views.poperators,name="poperators"),
    path("pconditional",views.pconditional,name="pconditional"),
    path("ploop",views.ploop,name="ploop"),
    path("pinput",views.pinput,name="pinput"),
    path("pstring",views.pstring,name="pstring"),
    path("plist",views.plist,name="plist"),
    path("pdictonary",views.pdictonary,name="pdictonary"),
    path("ptuples",views.ptuples,name="ptuples"),
    path("pset",views.pset,name="pset"),
    path("pfunctions",views.pfunctions,name="pfunctions")

    ]