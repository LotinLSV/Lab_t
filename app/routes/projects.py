from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .. import models, database
from .auth import get_current_user_required

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/", response_class=HTMLResponse)
async def projects_view(request: Request, db: Session = Depends(database.get_db)):
    user = get_current_user_required(request, db)
    projects = db.query(models.Project).filter(models.Project.owner_id == user.id).order_by(models.Project.created_at.desc()).all()
    
    from ..main import templates
    return templates.TemplateResponse("projects.html", {"request": request, "user": user, "projects": projects})
