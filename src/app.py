"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "A club for students who enjoy playing chess.",
        "participants": []
    },
    "Robotics Team": {
        "description": "A team that builds and programs robots for competitions.",
        "participants": []
    },
    "Drama Club": {
        "description": "A club for students interested in acting and theater production.",
        "participants": []
    },
    "Soccer Team": {
        "description": "A team for students who enjoy playing and competing in soccer.",
        "participants": []
    },
    "Basketball Team": {
        "description": "A team for students who enjoy playing and competing in basketball.",
        "participants": []
    },
    "Volleyball Team": {
        "description": "A team for students who enjoy playing and competing in volleyball.",
        "participants": []
    },
    "Track and Field Team": {
        "description": "A team for students who enjoy running, jumping, and throwing in track and field events.",
        "participants": []
    },
    "Art Club": {
        "description": "A club for students interested in drawing, painting, and other visual arts.",
        "participants": []
    },
    "Photography Club": {
        "description": "A club for students interested in learning photography and creating visual stories.",
        "participants": []
    },
    "Creative Writing Club": {
        "description": "A club for students interested in writing poetry, stories, and other creative works.",
        "participants": []
    },
    "Music Club": {
        "description": "A club for students interested in performing and exploring music.",
        "participants": []
    },
    "Debate Club": {
        "description": "A club for students who enjoy researching topics and building arguments.",
        "participants": []
    },
    "Math Club": {
        "description": "A club for students interested in solving challenging mathematical problems and puzzles.",
        "participants": []
    },
    "Science Club": {
        "description": "A club for students interested in exploring scientific ideas and experiments.",
        "participants": []
    },
    "Computer Science Club": {
        "description": "A club for students interested in learning programming and exploring computer technology.",
        "participants": []
    }
}

@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
