signin = '''{
    "id" : "main-stage",
    "type" : "ClutterStage",
    "color" : "white",
    "width" : 800,
    "height" : 600,
    "title": "Sign in",
    "children" : [
      {
        "id" : "signin-label",
        "type" : "ClutterText",
        "x" : 400,
        "y" : 300,
        "text" : "Sign in",
        "color" : "black",
        "font-name" : "Sans 48px"
      }
    ],
    "signals" : [
      { 
        "name" : "destroy", 
        "handler" : "clutter_main_quit"
      }
    ]
}
'''
